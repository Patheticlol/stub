# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ComponentCls = clientApi.GetComponentCls()

class ShootComponentClient(ComponentCls):
    def __init__(self, entityId):
        ComponentCls.__init__(self, entityId)
        self.mShoot = False

    @property
    def shoot(self):
        return self.mShoot

    @shoot.setter
    def shoot(self, val):
        self.mShoot = val