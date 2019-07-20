# -*- coding: utf-8 -*-

# 获取引擎服务端API的模块
import server.extraServerApi as serverApi
# 获取引擎服务端System的基类，System都要继承于ServerSystem来调用相关函数
ServerSystem = serverApi.GetServerSystemCls()

# 在modMain中注册的Server System类
class TutorialServerSystem(ServerSystem):

    # ServerSystem的初始化函数
    def __init__(self, namespace, systemName):
        # 首先调用父类的初始化函数
        super(TutorialServerSystem, self).__init__(namespace, systemName)
        print "===== TutorialServerSystem init ====="
        # 初始时调用监听函数监听事件
        self.ListenEvent()

    # 监听函数，用于定义和监听函数。函数名称除了强调的其他都是自取的，这个函数也是。
    def ListenEvent(self):
        # 在自定义的ServerSystem中监听引擎的事件ServerChatEvent，回调函数为OnServerChat
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)

    # 反监听函数，用于反监听事件，在代码中有创建注册就对应了销毁反注册是一个好的编程习惯，不要依赖引擎来做这些事。
    def UnListenEvent(self):
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)

    # 监听ServerChatEvent的回调函数
    def OnServerChat(self, args):
        print "==== OnServerChat ==== ", args
        # 生成掉落物品
        # 当我们输入的信息等于右边这个值时，创建相应的物品
        if args["message"] == "钻石剑":
            # 创建Component，用来完成特定的功能，这里是为了创建Item物品
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            # 给这个Component赋值，参数参考《MODSDK文档》
            comp.addItems = [("minecraft:diamond_sword", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            # 这一步很重要，它告诉系统需要更新这个Component，继而完成响应的功能
            self.NeedsUpdate(comp)
        elif args["message"] == "钻石镐":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_pickaxe", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        elif args["message"] == "钻石头盔":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_helmet", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        elif args["message"] == "钻石胸甲":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_chestplate", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        elif args["message"] == "钻石护腿":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_leggings", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        elif args["message"] == "钻石靴子":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_boots", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        else:
            print "==== Sorry man ===="

    # 函数名为Destroy才会被调用，在这个System被引擎回收的时候会调这个函数来销毁一些内容
    def Destroy(self):
        print "===== TutorialServerSystem Destroy ====="
        # 调用上面的反监听函数来销毁
        self.UnListenEvent()
