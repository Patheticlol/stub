# -*- coding: utf-8 -*-
#
import server.extraServerApi as serverApi
ComponentCls = serverApi.GetComponentCls()

class DeliverCompServer(ComponentCls):
	def __init__(self, entityId):
		ComponentCls.__init__(self, entityId)
		self.own = None
		self.broadcast = None
