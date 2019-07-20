# -*- coding: utf-8 -*-
# 客户端事件名称可以通过我获取
""" 示例代码
from simpleApi.clientEvent import clientEvent
    self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), clientEvent.AddPlayerEvent, self, self.OnAddPlayer)
"""

# Player
AddPlayerEvent = "AddPlayerEvent"
ApproachEntityClientEvent = "ApproachEntityClientEvent"
LeaveEntityClientEvent = "LeaveEntityClientEvent"

# Entity
OnGroundClientEvent = "OnGroundClientEvent"
AttackAnimBeginClientEvent = "AttackAnimBeginClientEvent"
AttackAnimEndClientEvent = "AttackAnimEndClientEvent"
JumpAnimBeginClientEvent = "JumpAnimBeginClientEvent"
WalkAnimBeginClientEvent = "WalkAnimBeginClientEvent"
WalkAnimEndClientEvent = "WalkAnimEndClientEvent"
AddEntityEvent = "AddEntityEvent"
RemoveEntityPacketEvent = "RemoveEntityPacketEvent"

# UI
PushScreenEvent = "PushScreenEvent"
PopScreenEvent = "PopScreenEvent"
UiInitFinished = "UiInitFinished"

# Item
OnModItemUseClientEvent = "OnModItemUseClientEvent"
OnModItemUseOnClientEvent = "OnModItemUseOnClientEvent"
OnCarriedNewItemChangedClientEvent = "OnCarriedNewItemChangedClientEvent"

# Level
ClientLevelCreateBeginEvent = "ClientLevelCreateBeginEvent"
ClientLevelCreateFinishedEvent = "ClientLevelCreateFinishedEvent"
OnScriptTickClient = "OnScriptTickClient"
LoadClientAddonScriptsAfter = "LoadClientAddonScriptsAfter"
UnLoadClientAddonScriptsBefore = "UnLoadClientAddonScriptsBefore"

# Action
OnKeyPressInGame = "OnKeyPressInGame"
OnClickInGame = "OnClickInGame"
ClientJumpButtonPressDownEvent = "ClientJumpButtonPressDownEvent"
ClientJumpButtonReleaseEvent = "ClientJumpButtonReleaseEvent"
OnClientPlayerStartMove = "OnClientPlayerStartMove"
OnClientPlayerStopMove = "OnClientPlayerStopMove"
