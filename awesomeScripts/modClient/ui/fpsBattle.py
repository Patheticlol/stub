# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
from awesomeScripts.modClient import logger
from awesomeScripts.modCommon import modConfig

class FpsBattleScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.mOriginalFov = 1.0
        self.mShowSight = False
        self.mPlayerId = clientApi.GetLocalPlayerId()

    def Create(self):
        logger.info("===== FpsBattleScreen Create =====")
        self.mButtonPanel = "/buttonPanel"
        self.mAimButton = self.mButtonPanel + "/aimButton"
        self.mShootButtonRight = self.mButtonPanel + "/shootButtonRight"
        self.mChangeButton = self.mButtonPanel + "/changeButton"
        self.mShootButtonLeft = self.mButtonPanel + "/shootButtonLeft"
        self.mAimPanel = "/aimPanel"
        self.mAimImage = self.mAimPanel + "/aimImage"
        self.mAimingImage = self.mAimPanel + "/aimingImage"

    def Init(self):
        # hide native cross hair
        self.SetCrossHair(False)
        # hide aiming sight
        self.SetVisible(self.mAimingImage, False)
        # get field of view
        cameraComp = clientApi.CreateComponent(clientApi.GetLevelId(), modConfig.Minecraft, modConfig.CameraComponent)
        self.mOriginalFov = cameraComp.fov
        clientApi.CreateComponent(self.mPlayerId, modConfig.ModName, modConfig.ClientShootComponent)

    def Update(self):
        """
        node tick function
        """
        pass

# Start Binding
    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def OnAimButtonClick(self, args):
        logger.info("OnAimButtonClick Up")
        self.Aim()
        return ViewRequest.Refresh

    @ViewBinder.binding(ViewBinder.BF_ButtonClick)
    def OnChangeButtonClick(self, args):
        if args["ButtonState"]:
            logger.info("OnChangeButtonClick down")
        else:
            logger.info("OnChangeButtonClick up")
        return ViewRequest.Refresh

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def OnShootButtonLeftClick(self, args):
        logger.info("OnShootButtonLeftClick Up")
        self.Shoot()
        return ViewRequest.Refresh

    @ViewBinder.binding(ViewBinder.BF_ButtonClickCancel, binding_name = "OnShootButtonLeftClick")
    def OnShootButtonLeftClickCancel(self, args):
        logger.info("OnShootButtonLeftClickCancel Cancel")

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def OnShootButtonRightClick(self, args):
        logger.info("OnShootButtonRightClick Up")
        self.Shoot()
        return ViewRequest.Refresh

    @ViewBinder.binding(ViewBinder.BF_ButtonClickCancel, binding_name = "OnShootButtonRightClick")
    def OnShootButtonRightClickCancel(self, args):
        logger.info("OnShootButtonRightClickCancel Cancel")

    def Aim(self):
        if self.mShowSight:
            self.mShowSight = False
            self.SetVisible(self.mAimImage, True)
            self.SetVisible(self.mAimingImage, False)
            cameraComp = clientApi.GetComponent(clientApi.GetLevelId(), modConfig.Minecraft, modConfig.CameraComponent)
            cameraComp.fov = self.mOriginalFov
            clientApi.NeedsUpdate(cameraComp)
        else:
            self.mShowSight = True
            self.SetVisible(self.mAimImage, False)
            self.SetVisible(self.mAimingImage, True)
            cameraComp = clientApi.GetComponent(clientApi.GetLevelId(), modConfig.Minecraft, modConfig.CameraComponent)
            cameraComp.fov = self.mOriginalFov + modConfig.SightFieldOfView
            clientApi.NeedsUpdate(cameraComp)

    def Shoot(self):
        shootComp = clientApi.GetComponent(self.mPlayerId, modConfig.ModName, modConfig.ClientShootComponent)
        shootComp.shoot = True
        clientApi.NeedsUpdate(shootComp)

# End Binding