from common.mod import Mod
import client.extraClientApi as clientApi
import server.extraServerApi as serverApi

@Mod.Binding(name = "LobbyGoodDemo", version = "0.1")
class LobbyGoodDemoMain(object):
	def __init__(self):
		pass

	@Mod.InitServer()
	def init_server(self):
		# RegisterComponent before RegisterSystem
		serverApi.RegisterComponent("LobbyGoodDemo", "deliverbbComp", "LobbyGoodDemoScripts.modComp.deliverCompServer.DeliverCompServer")

		serverApi.RegisterSystem("LobbyGoodDemo", "LobbyGoodDemoServer", "LobbyGoodDemoScripts.modSystem.LobbyGoodDemoSysServer.LobbyGoodDemoServer")

	@Mod.DestroyServer()
	def destroy_server(self):
		pass


	@Mod.InitClient()
	def init_client(self):
		clientApi.RegisterSystem("LobbyGoodDemo", "LobbyGoodDemoClient", "LobbyGoodDemoScripts.modSystem.LobbyGoodDemoSysClient.LobbyGoodDemoClient")

	@Mod.DestroyClient()
	def destroy_client(self):
		pass
