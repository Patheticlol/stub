# -*- coding: utf-8 -*-
#
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()

class LobbyGoodDemoClient(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.DefineEvent('RequestbbParticle')
		self.ListenForEvent('LobbyGoodDemo', 'LobbyGoodDemoServer', 'DeliverbbParticle', self, self.OnDeliverbbParticle)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "AddPlayerEvent",
		                    self, self.RequestbbParticle)


	def OnDeliverbbParticle(self, args):
		eid = args['eid']
		# 获取位置 并检查是否存在
		posComp = self.CreateComponent(eid, "Minecraft", "pos")
		if not posComp.pos:
			return
		# 创建粒子
		tempEntityEffect = self.CreateTempEntity()
		typeComp = self.CreateComponent(tempEntityEffect.mId, 'Minecraft', 'type')
		typeComp.type = clientApi.GetMinecraftEnum().EntityConst.TYPE_PARTICLE
		pathComp = self.CreateComponent(tempEntityEffect.mId, 'Minecraft', 'path')
		pathComp.path = "effects/bb.json"
		transComp = self.CreateComponent(tempEntityEffect.mId, 'Minecraft', 'particleTrans')
		transComp.pos = posComp.pos
		particleEntityId = self.CreateEntity(tempEntityEffect)
		# 播放
		ctrlComp = self.CreateComponent(particleEntityId, 'Minecraft', 'particleControl')
		ctrlComp.open = True
		self.NeedsUpdate(ctrlComp)
		#绑定粒子
		bindComp = self.CreateComponent(particleEntityId, "Minecraft", "particleEntityBind")
		bindComp.bindEntityId = eid
		bindComp.offset = (0.0, 0.0, 0.0)
		bindComp.rot = (0.0, 0.0, 0.0)
		self.NeedsUpdate(bindComp)

	def RequestbbParticle(self, args):
		eid = args.get("id")
		if eid:
			checkArgs = self.CreateEventData()
			checkArgs['from'] = clientApi.GetLocalPlayerId()
			checkArgs['eid'] = eid
			self.NotifyToServer("RequestbbParticle", checkArgs)

	def Update(self):
		pass


	def Destroy(self):
		self.UnListenForEvent('LobbyGoodDemo', 'LobbyGoodDemoServer', 'DeliverbbParticle', self, self.OnDeliverbbParticle)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "AddPlayerEvent",
		                    self, self.RequestbbParticle)











