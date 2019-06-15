# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
from awesomeScripts.modCommon import modConfig
from awesomeScripts.modServer import logger
from awesomeScripts.modServer.serverManager.coroutineMgrGas import CoroutineMgr

class FpsServerSystem(ServerSystem):

    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        logger.info("===== Server Listen =====")
        self.ListenEvent()

    def ListenEvent(self):
        self.DefineEvent(modConfig.PlayShootAnimEvent)
        self.DefineEvent(modConfig.BulletFlyFrameEvent)
        self.DefineEvent(modConfig.BulletHitEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerChatEvent, self, self.OnServerChat)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ScriptTickServerEvent, self, self.OnTickServer)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.AddServerPlayerEvent, self, self.OnPlayerAdd)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ProjectileDoHitEffectEvent, self, self.OnProjectileHit)
        self.ListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.ShootEvent, self, self.OnShoot)

    def UnListenEvent(self):
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerChatEvent, self, self.OnServerChat)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ScriptTickServerEvent, self, self.OnTickServer)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.AddServerPlayerEvent, self, self.OnPlayerAdd)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ProjectileDoHitEffectEvent, self, self.OnProjectileHit)
        self.UnListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.ShootEvent, self, self.OnShoot)

    def OnServerChat(self, args):
        logger.info("ServerChatMessage : %s", args)
        args["message"] = "§l§e HelloWorld!"
        args["username"] = "§l§e Hugo"

    def OnTickServer(self):
        """
        Driven by event, One tick way
        """
        CoroutineMgr.Tick()

    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        pass

    def OnShoot(self, data):
        playerId = data.get("id", "-1")
        logger.info("OnShoot playerId: %s" % playerId)
        # create arrow
        tempEntity = self.CreateTempEntity()
        typeComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.ScriptTypeCompServer)
        typeComp.type = serverApi.GetMinecraftEnum().EntityConst.TYPE_BULLET
        engineTypeComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.EngineTypeComponent)
        engineTypeComp.engineType = serverApi.GetMinecraftEnum().EntityType.Arrow
        playerPosComp = self.GetComponent(playerId, modConfig.Minecraft, modConfig.PosComponent)
        playerRotComp = self.GetComponent(playerId, modConfig.Minecraft, modConfig.RotComponent)
        posComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.PosComponent)
        posComp.pos = playerPosComp.pos
        bulletComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.BulletComponent)
        bulletComp.shooterId = playerId
        bulletComp.direction = serverApi.GetDirFromRot(playerRotComp.rot)
        bulletComp.power = modConfig.BulletPower
        bulletComp.gravity = modConfig.BulletGravity
        bulletComp.targetId = "-1"
        bulletId = self.CreateEntity(tempEntity)
        frameInfo = self.CreateEventData()
        frameInfo["bindId"] = bulletId
        self.BroadcastToAllClient(modConfig.BulletFlyFrameEvent, frameInfo)
        animInfo = self.CreateEventData()
        animInfo["entityId"] = playerId
        animInfo["anim"] = modConfig.DatiangouFengxiAnim
        animInfo["isLoop"] = False
        self.BroadcastToAllClient(modConfig.PlayShootAnimEvent, animInfo)

    def OnPlayerAdd(self, data):
        logger.info("OnPlayerAdd : %s", data)
        playerId = data.get("id", "-1")
        if playerId == "-1":
            return
        modelComp = self.CreateComponent(playerId, modConfig.Minecraft, modConfig.ModelCompServer)
        modelComp.modelName = modConfig.DatiangouModel
        self.NeedsUpdate(modelComp)

    def OnProjectileHit(self, data):
        logger.info("OnProjectileHit : %s", data)
        bulletId = data.get("id", "-1")
        targetType = data.get("hitTargetType", "")
        targetId = data.get("targetId", "")
        hitFace = data.get("hitFace", -1)
        x = data.get("x", 0.0)
        y = data.get("y", 0.0)
        z = data.get("z", 0.0)
        blockPosX = data.get("blockPosX", 0)
        blockPosY = data.get("blockPosY", 0)
        blockPosZ = data.get("blockPosZ", 0)
        hitInfo = self.CreateEventData()
        hitInfo["bulletId"] = bulletId
        hitInfo["pos"] = (x, y, z)
        hitInfo["targetId"] = targetId
        hitInfo["targeType"] = targetType
        hitInfo["hitFace"] = hitFace
        self.BroadcastToAllClient(modConfig.BulletHitEvent, hitInfo)
        self.DestroyEntity(bulletId)

    def Destroy(self):
        logger.info("===== Fps Server System Destroy =====")
        self.UnListenEvent()
