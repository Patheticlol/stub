from common.modGoods import ModGoods
import server.extraServerApi as serverApi

@ModGoods.Binding(name = "LobbyGoodDemo", version = "0.1")
class LobbyGoodDemoGoodsMain(object):
	def __init__(self):
		pass

	@ModGoods.DeliverGoods()
	def deliver_bb(self, entityId, type, iid):
		comp = serverApi.CreateComponent(entityId, 'LobbyGoodDemo', 'deliverbbComp')
		comp.broadcast = True
		serverApi.NeedsUpdate(comp)
