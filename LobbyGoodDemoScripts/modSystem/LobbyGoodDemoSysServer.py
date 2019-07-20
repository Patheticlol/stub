# -*- coding: utf-8 -*-
#
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class LobbyGoodDemoServer(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)

		self.DefineEvent('DeliverbbParticle')
		self.ListenForEvent('LobbyGoodDemo', 'LobbyGoodDemoClient', 'RequestbbParticle', self, self.OnRequestbbParticle)

		self.mCompKey = "LobbyGoodDemo" + ':' + "deliverbbComp"

	def CheckbbParticle(self, eid):
		comp = self.GetComponent(eid, "LobbyGoodDemo", "deliverbbComp")
		if comp and comp.own:
			return True
		return False

	def OnRequestbbParticle(self, args):
		eid = args['eid']
		if self.CheckbbParticle(eid):
			deliverArgs = self.CreateEventData()
			deliverArgs['eid'] = eid
			self.NotifyToClient(args['from'], 'DeliverbbParticle', deliverArgs)

	def Update(self):
		needUpdateEntities = self.GetNeedUpdate().get(self.mCompKey, {})
		for entityId in needUpdateEntities:
			comp = self.GetComponent(entityId, "LobbyGoodDemo", "deliverbbComp")
			if comp.broadcast:
				deliverArgs = self.CreateEventData()
				deliverArgs['eid'] = entityId
				self.BroadcastToAllClient("DeliverbbParticle", deliverArgs)
				comp.broadcast = None
				comp.own = True


	def Destroy(self):
		self.UnListenForEvent('LobbyGoodDemo', 'LobbyGoodDemoClient', 'RequestbbParticle', self, self.OnRequestbbParticle)
