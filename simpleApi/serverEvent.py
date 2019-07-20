# -*- coding: utf-8 -*-
# 服务端事件名称可以通过我获取
""" 示例代码
from simpleApi.serverEvent import serverEvent
    self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), serverEvent.ProjectileDoHitEffectEvent, self, self.OnProjectileDoHitEffect)
"""

# Projectile
ProjectileDoHitEffectEvent = "ProjectileDoHitEffectEvent"
ProjectileCritHitEvent = "ProjectileCritHitEvent"

# Player
PlayerHurtEvent = "PlayerHurtEvent"
PlayerTouchModItemEvent = "PlayerTouchModItemEvent"
PlayerTeleportEvent = "PlayerTeleportEvent"
PlayerDieEvent = "PlayerDieEvent"
PlayerAttackEntityEvent = "PlayerAttackEntityEvent"
AddExpEvent = "AddExpEvent"
AddLevelEvent = "AddLevelEvent"
DelServerPlayerEvent = "DelServerPlayerEvent"
AddServerPlayerEvent = "AddServerPlayerEvent"
ServerChatEvent = "ServerChatEvent"
PlayerRespawnEvent = "PlayerRespawnEvent"

# Entity
EntityRemoveEvent = "EntityRemoveEvent"
OnKnockBackServerEvent = "OnKnockBackServerEvent"
MobDieEvent = "MobDieEvent"
EntityLoadScriptEvent = "EntityLoadScriptEvent"
EntityStartRidingEvent = "EntityStartRidingEvent"
EntityStopRidingEvent = "EntityStopRidingEvent"
AttackAnimBeginServerEvent = "AttackAnimBeginServerEvent"
AttackAnimEndServerEvent = "AttackAnimEndServerEvent"
JumpAnimBeginServerEvent = "JumpAnimBeginServerEvent"
WalkAnimBeginServerEvent = "WalkAnimBeginServerEvent"
WalkAnimEndServerEvent = "WalkAnimEndServerEvent"

# Block
ServerEntityTryPlaceBlockEvent = "ServerEntityTryPlaceBlockEvent"
ServerPlayerTryDestroyBlockEvent = "ServerPlayerTryDestroyBlockEvent"
DestroyBlockEvent = "DestroyBlockEvent"
ServerPreBlockPatternEvent = "ServerPreBlockPatternEvent"
ServerPostBlockPatternEvent = "ServerPostBlockPatternEvent"
ModBlockUseEvent = "ModBlockUseEvent"

# Item
OnModItemUseServerEvent = "OnModItemUseServerEvent"
OnModItemUseOnServerEvent = "OnModItemUseOnServerEvent"

# Level
ServerLevelCreateBeginEvent = "ServerLevelCreateBeginEvent"
ServerLevelCreateFinishedEvent = "ServerLevelCreateFinishedEvent"
ServerLevelSaveDataEvent = "ServerLevelSaveDataEvent"
OnScriptTickServer = "OnScriptTickServer"
LoadServerAddonScriptsAfter = "LoadServerAddonScriptsAfter"
UnLoadServerAddonScriptsBefore = "UnLoadServerAddonScriptsBefore"

# Mob
ExplosionHurtEvent = "ExplosionHurtEvent"
OnFireHurtEvent = "OnFireHurtEvent"
DamageEvent = "DamageEvent"
ServerSpawnMobEvent = "ServerSpawnMobEvent"
