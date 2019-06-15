# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
from awesomeScripts.modCommon import modConfig
from awesomeScripts.modClient import logger
from awesomeScripts.modClient.clientManager.coroutineMgrGac import CoroutineMgr

class FpsClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        logger.info("===== Client Listen =====")
        self.ListenEvent()
        self.mFpsBattleUINode = None
        self.mShootKey = modConfig.ModName + ":" + modConfig.ClientShootComponent
        self.mPlayerId = clientApi.GetLocalPlayerId()
        self.mHitDestroyIdList = {}

    def ListenEvent(self):
        self.DefineEvent(modConfig.ShootEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.PlayShootAnimEvent, self, self.OnPlayShootAnim)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletFlyFrameEvent, self, self.OnBulletFlyFrame)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletHitEvent, self, self.OnBulletHit)

    def UnListenEvent(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.PlayShootAnimEvent, self, self.OnPlayShootAnim)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletFlyFrameEvent, self, self.OnBulletFlyFrame)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletHitEvent, self, self.OnBulletHit)

    def OnUIInitFinished(self, args):
        logger.info("OnUIInitFinished : %s", args)
        clientApi.RegisterUI(modConfig.ModName, modConfig.FpsBattleUIName, modConfig.FpsBattleUIPyClsPath, modConfig.FpsBattleUIScreenDef)
        clientApi.CreateUI(modConfig.ModName, modConfig.FpsBattleUIName, {"isHud" : 1})
        self.mFpsBattleUINode = clientApi.GetUI(modConfig.ModName, modConfig.FpsBattleUIName)
        if self.mFpsBattleUINode:
            self.mFpsBattleUINode.Init()
        else:
            logger.error("create ui %s failed!" % modConfig.FpsBattleUIScreenDef)
        logger.info("change model datiangou")
        modelComp = self.CreateComponent(self.mPlayerId, modConfig.Minecraft, modConfig.ModelCompClient)
        modelComp.modelName = modConfig.DatiangouModel
        modelComp.aniName = modConfig.DatiangouRunAnim
        modelComp.isLoop = True
        self.NeedsUpdate(modelComp)

    def OnTickClient(self):
        """
        Driven by event, One tick way
        """
        CoroutineMgr.Tick()

    def OnPlayShootAnim(self, data):
        """
        Play shoot anim
        """
        entityId = data.get("entityId", "-1")
        anim = data.get("anim", "")
        isLoop = data.get("isLoop", False)
        modelComp = self.GetComponent(entityId, modConfig.Minecraft, modConfig.ModelCompClient)
        if not modelComp:
            logger.warning("do not have model comp!")
            return
        modelComp.aniName = anim
        modelComp.isLoop = isLoop
        self.NeedsUpdate(modelComp)
        CoroutineMgr.StartCoroutine(self.DelayPlayAnimRun())

    def DelayPlayAnimRun(self):
        yield - modConfig.DatiangouFengxiAnimFrames
        logger.info("Delay play run anim")
        modelComp = self.GetComponent(self.mPlayerId, modConfig.Minecraft, modConfig.ModelCompClient)
        modelComp.modelName = modConfig.DatiangouModel
        modelComp.aniName = modConfig.DatiangouRunAnim
        modelComp.isLoop = True
        self.NeedsUpdate(modelComp)

    def OnBulletFlyFrame(self, data):
        logger.info("OnBulletFlyFrame: %s" , data)
        bindId = data.get("bindId", "-1")
        tempEntity = self.CreateTempEntity()
        typeComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.ScriptTypeCompClient)
        typeComp.type = clientApi.GetMinecraftEnum().EntityConst.TYPE_SFX
        pathComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.PathComponent)
        pathComp.path = modConfig.BulletFlyFrameSfx
        frameEntityId = self.CreateEntity(tempEntity)
        entityBindComp = self.CreateComponent(frameEntityId, modConfig.Minecraft, modConfig.FrameAniBindComponent)
        entityBindComp.bindEntityId = bindId
        entityBindComp.offset = (-1, 0, 0)
        entityBindComp.rot = (0, 0, 0)
        self.NeedsUpdate(entityBindComp)
        playerPosComp = self.GetComponent(self.mPlayerId, modConfig.Minecraft, modConfig.PosComponent)
        transComp = self.CreateComponent(frameEntityId, modConfig.Minecraft, modConfig.FrameAniTransComponent)
        transComp.pos = playerPosComp.pos
        self.NeedsUpdate(transComp)
        ctrlComp = self.CreateComponent(frameEntityId, modConfig.Minecraft, modConfig.FrameAniCtrlComponent)
        ctrlComp.open = True
        ctrlComp.loop = True
        ctrlComp.faceCamera = True
        self.NeedsUpdate(ctrlComp)
        # record something to destroy when hit
        bindList = self.mHitDestroyIdList.setdefault(bindId, [])
        bindList.append(frameEntityId)

    def OnBulletHit(self, data):
        logger.info("OnBulletHit %s", data)
        bulletId = data.get("bulletId", "-1")
        targetId = data.get("targetId", "-1")
        hitFace = data.get("hitFace", -1)
        pos = data.get("pos", (0, 0, 0))
        pos = tuple(pos)
        audioComp = self.CreateComponent(self.mPlayerId, modConfig.Minecraft, modConfig.AudioComponent)
        audioComp.name = modConfig.BulletHitSound
        audioComp.pos = pos
        audioComp.volume = 1.0
        audioComp.pitch = 1.0
        audioComp.needPlay = True
        self.NeedsUpdate(audioComp)
        tempEntity = self.CreateTempEntity()
        typeComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.ScriptTypeCompClient)
        typeComp.type = clientApi.GetMinecraftEnum().EntityConst.TYPE_PARTICLE
        pathComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.PathComponent)
        pathComp.path = modConfig.BulletHitEffect
        transComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.ParticleTransComponent)
        transComp.pos = pos
        particleEntityId = self.CreateEntity(tempEntity)
        ctrlComp = self.CreateComponent(particleEntityId, modConfig.Minecraft, modConfig.ParticleControlComponent)
        ctrlComp.open = True
        self.NeedsUpdate(ctrlComp)
        CoroutineMgr.StartCoroutine(self.DelayCloseParticleControl(ctrlComp))
        # destroy something when bullet hit
        destroyList = self.mHitDestroyIdList.get(bulletId, None)
        if destroyList:
            for entityId in destroyList:
                self.DestroyEntity(entityId)

    def DelayCloseParticleControl(self, ctrlComp):
        yield - modConfig.ParticleControlFrames
        ctrlComp.open = False
        self.NeedsUpdate(ctrlComp)


    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        self.UpdateShoot()

    def UpdateShoot(self):
        needUpdateEntities = self.GetNeedUpdate().get(self.mShootKey, {})
        for entityId in needUpdateEntities:
            comp = self.GetComponent(entityId, modConfig.ModName, modConfig.ClientShootComponent)
            if comp and comp.shoot:
                shootData = self.CreateEventData()
                shootData["id"] = self.mPlayerId
                self.NotifyToServer(modConfig.ShootEvent, shootData)
                comp.shoot = False

    def Destroy(self):
        logger.info("===== Fps Client System Destroy =====")
        self.UnListenEvent()