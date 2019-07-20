# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
from awesomeScripts.modCommon import modConfig
# 用来打印规范的log
from awesomeScripts.modClient import logger
# 用来执行一些延迟函数，yield 负数为帧数，正数为秒数
from awesomeScripts.modClient.clientManager.coroutineMgrGac import CoroutineMgr

class FpsClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        logger.info("===== Client Listen =====")
        self.ListenEvent()
        # 保存ui界面节点
        self.mFpsBattleUINode = None
        # 拼接ShootComponent的Key
        self.mShootKey = modConfig.ModName + ":" + modConfig.ClientShootComponent
        # 获取客户端本地玩家的playerId
        self.mPlayerId = clientApi.GetLocalPlayerId()
        # 用于保存在击中后需要释放的实体
        self.mHitDestroyIdList = {}

    # 监听引擎和服务端脚本的事件
    def ListenEvent(self):
        self.DefineEvent(modConfig.ShootEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.PlayShootAnimEvent, self, self.OnPlayShootAnim)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletFlyFrameEvent, self, self.OnBulletFlyFrame)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletHitEvent, self, self.OnBulletHit)

    # 取消监听引擎和服务端脚本事件
    def UnListenEvent(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.PlayShootAnimEvent, self, self.OnPlayShootAnim)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletFlyFrameEvent, self, self.OnBulletFlyFrame)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletHitEvent, self, self.OnBulletHit)

    # 监听引擎初始化完成事件，在这个事件后创建我们的战斗UI
    def OnUIInitFinished(self, args):
        logger.info("OnUIInitFinished : %s", args)
        # 注册UI 详细解释参照《UI API》
        clientApi.RegisterUI(modConfig.ModName, modConfig.FpsBattleUIName, modConfig.FpsBattleUIPyClsPath, modConfig.FpsBattleUIScreenDef)
        # 创建UI 详细解释参照《UI API》
        clientApi.CreateUI(modConfig.ModName, modConfig.FpsBattleUIName, {"isHud" : 1})
        self.mFpsBattleUINode = clientApi.GetUI(modConfig.ModName, modConfig.FpsBattleUIName)
        if self.mFpsBattleUINode:
            self.mFpsBattleUINode.Init()
        else:
            logger.error("create ui %s failed!" % modConfig.FpsBattleUIScreenDef)
        logger.info("change model datiangou")
        # 客户端换上模型大天狗并循环播放动作大天狗跑步
        modelComp = self.CreateComponent(self.mPlayerId, modConfig.Minecraft, modConfig.ModelCompClient)
        modelComp.modelName = modConfig.DatiangouModel
        modelComp.aniName = modConfig.DatiangouRunAnim
        modelComp.isLoop = True
        self.NeedsUpdate(modelComp)

    # 监听引擎ScriptTickClientEvent事件，引擎会执行该tick回调，1秒钟30帧
    def OnTickClient(self):
        """
        Driven by event, One tick way
        """
        CoroutineMgr.Tick()

    # 监听来自服务端的事件，客户端在这里开始播放服务端通知的相应的射击动作
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
        # 延迟恢复播放大天狗跑步
        CoroutineMgr.StartCoroutine(self.DelayPlayAnimRun())

    # 在播放完大天狗风袭动作之后，播放大天狗跑步动作，延迟的帧数是风袭动作的播放帧数
    def DelayPlayAnimRun(self):
        yield - modConfig.DatiangouFengxiAnimFrames
        logger.info("Delay play run anim")
        modelComp = self.GetComponent(self.mPlayerId, modConfig.Minecraft, modConfig.ModelCompClient)
        modelComp.modelName = modConfig.DatiangouModel
        modelComp.aniName = modConfig.DatiangouRunAnim
        modelComp.isLoop = True
        self.NeedsUpdate(modelComp)

    # 在子弹开始飞的时候，给子弹绑定上特效
    def OnBulletFlyFrame(self, data):
        logger.info("OnBulletFlyFrame: %s" , data)
        bindId = data.get("bindId", "-1")
        # 同服务端的解释，tempEntity保存来自各个Component的数据
        tempEntity = self.CreateTempEntity()
        typeComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.ScriptTypeCompClient)
        typeComp.type = clientApi.GetMinecraftEnum().EntityConst.TYPE_SFX
        pathComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.PathComponent)
        pathComp.path = modConfig.BulletFlyFrameSfx
        # 创建真正的特效SFX实体绑定在子弹上
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
        # 将特效实体Id保存在self.mHitDestroyIdList中，后续更新中会清除
        bindList = self.mHitDestroyIdList.setdefault(bindId, [])
        bindList.append(frameEntityId)

    # 当子弹射中后，服务端通知客户端并返回一些数据后
    def OnBulletHit(self, data):
        logger.info("OnBulletHit %s", data)
        bulletId = data.get("bulletId", "-1")
        targetId = data.get("targetId", "-1")
        hitFace = data.get("hitFace", -1)
        pos = data.get("pos", (0, 0, 0))
        pos = tuple(pos)
        # 添加播放声音的Component
        audioComp = self.CreateComponent(self.mPlayerId, modConfig.Minecraft, modConfig.AudioComponent)
        audioComp.name = modConfig.BulletHitSound
        audioComp.pos = pos
        audioComp.volume = 1.0
        audioComp.pitch = 1.0
        audioComp.needPlay = True
        self.NeedsUpdate(audioComp)
        # 添加击中后在原地产生的爆炸粒子特效
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
        # 爆炸的粒子特效延迟销毁
        CoroutineMgr.StartCoroutine(self.DelayCloseParticleControl(ctrlComp))
        # 在每次射中后删除绑定在子弹上的特效
        destroyList = self.mHitDestroyIdList.get(bulletId, None)
        if destroyList:
            for entityId in destroyList:
                self.DestroyEntity(entityId)

    # 在延后modConfig.ParticleControlFrames这么多帧后开始执行销毁
    def DelayCloseParticleControl(self, ctrlComp):
        yield - modConfig.ParticleControlFrames
        ctrlComp.open = False
        self.NeedsUpdate(ctrlComp)

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        self.UpdateShoot()

    # 更新自定义的ClientShootComponent，提交ClientShootComponent更新操作的是fpsBattle.py UI类中
    # Component需要经过System更新后才能生效，自定义的Component需要自己写相应的更新函数
    # 引擎的Component则在NeedsUpdate之后，由引擎来更新
    def UpdateShoot(self):
        needUpdateEntities = self.GetNeedUpdate().get(self.mShootKey, {})
        for entityId in needUpdateEntities:
            comp = self.GetComponent(entityId, modConfig.ModName, modConfig.ClientShootComponent)
            if comp and comp.shoot:
                shootData = self.CreateEventData()
                shootData["id"] = self.mPlayerId
                # 向服务端发送事件，玩家为playerId的人发送了射击事件
                self.NotifyToServer(modConfig.ShootEvent, shootData)
                # 发送后将Component置为不需要更新
                comp.shoot = False

    # 在清楚该system的时候调用取消监听事件
    def Destroy(self):
        logger.info("===== Fps Client System Destroy =====")
        self.UnListenEvent()