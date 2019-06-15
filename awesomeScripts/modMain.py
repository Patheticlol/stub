# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
import server.extraServerApi as serverApi
from awesomeScripts.modCommon import modConfig
from awesomeScripts import logger

@Mod.Binding(name = modConfig.ModName, version = modConfig.ModVersion)
class HugoFpsMod(object):

    def __init__(self):
        logger.info("===== init hugo fps mod =====")

    @Mod.InitServer()
    def HugoFpsServerInit(self):
        logger.info("===== init hugo fps server =====")
        serverApi.RegisterSystem(modConfig.ModName, modConfig.ServerSystemName, modConfig.ServerSystemClsPath)

    @Mod.DestroyServer()
    def HugoFpsServerDestroy(self):
        logger.info("===== destroy hugo fps server =====")
    
    @Mod.InitClient()
    def HugoFpsClientInit(self):
        logger.info("===== init hugo fps client =====")
        clientApi.RegisterComponent(modConfig.ModName, modConfig.ClientShootComponent, modConfig.ClientShootCompClsPath)
        clientApi.RegisterSystem(modConfig.ModName, modConfig.ClientSystemName, modConfig.ClientSystemClsPath)
    
    @Mod.DestroyClient()
    def HugoFpsClientDestroy(self):
        logger.info("===== destroy hugo fps client =====")
