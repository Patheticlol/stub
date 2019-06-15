# -*- coding: utf-8 -*-


def GetMinecraftEnum():
    class __MinecraftEnum(object):
        class EntityType(object):
            Undefined = 1
            TypeMask = 0x000000ff
            Mob = 0x00000100
            PathfinderMob = 0x00000200 | Mob
            Monster = 0x00000800 | PathfinderMob
            Animal = 0x00001000 | PathfinderMob
            TamableAnimal = 0x00004000 | Animal
            Ambient = 0x00008000 | Mob
            UndeadMob = 0x00010000 | Monster
            ZombieMonster = 0x00020000 | UndeadMob
            Arthropod = 0x00040000 | Monster
            Minecart = 0x00080000
            SkeletonMonster = 0x00100000 | UndeadMob
            EquineAnimal = 0x00200000 | TamableAnimal
            Projectile = 0x00400000
            AbstractArrow = 0x00800000
            WaterAnimal = 0x00002000 | PathfinderMob
            Chicken = 10 | Animal
            Cow = 11 | Animal
            Pig = 12 | Animal
            Sheep = 13 | Animal
            Wolf = 14 | TamableAnimal
            Villager = 15 | PathfinderMob
            MushroomCow = 16 | Animal
            Squid = 17 | WaterAnimal
            Rabbit = 18 | Animal
            Bat = 19 | Ambient
            IronGolem = 20 | PathfinderMob
            SnowGolem = 21 | PathfinderMob
            Ocelot = 22 | TamableAnimal
            Horse = 23 | EquineAnimal
            PolarBear = 28 | Animal
            Llama = 29 | Animal
            Parrot = 30 | TamableAnimal
            Dolphin = 31 | WaterAnimal
            Donkey = 24 | EquineAnimal
            Mule = 25 | EquineAnimal
            SkeletonHorse = 26 | EquineAnimal | UndeadMob
            ZombieHorse = 27 | EquineAnimal | UndeadMob
            Zombie = 32 | ZombieMonster
            Creeper = 33 | Monster
            Skeleton = 34 | SkeletonMonster
            Spider = 35 | Arthropod
            PigZombie = 36 | UndeadMob
            Slime = 37 | Monster
            EnderMan = 38 | Monster
            Silverfish = 39 | Arthropod
            CaveSpider = 40 | Arthropod
            Ghast = 41 | Monster
            LavaSlime = 42 | Monster
            Blaze = 43 | Monster
            ZombieVillager = 44 | ZombieMonster
            Witch = 45 | Monster
            Stray = 46 | SkeletonMonster
            Husk = 47 | ZombieMonster
            WitherSkeleton = 48 | SkeletonMonster
            Guardian = 49 | Monster
            ElderGuardian = 50 | Monster
            Npc = 51 | Mob
            WitherBoss = 52 | UndeadMob
            Dragon = 53 | Monster
            Shulker = 54 | Monster
            Endermite = 55 | Arthropod
            Agent = 56 | Mob
            Vindicator = 57 | Monster
            Phantom = 58 | UndeadMob
            ArmorStand = 61 | Mob
            TripodCamera = 62 | Mob
            Player = 63 | Mob
            ItemEntity = 64
            PrimedTnt = 65
            FallingBlock = 66
            MovingBlock = 67
            ExperiencePotion = 68 | Projectile
            Experience = 69
            EyeOfEnder = 70
            EnderCrystal = 71
            FireworksRocket = 72
            Trident = 73 | Projectile | AbstractArrow
            Turtle = 74 | Animal
            Cat = 75 | TamableAnimal
            ShulkerBullet = 76 | Projectile
            FishingHook = 77
            Chalkboard = 78
            DragonFireball = 79 | Projectile
            Arrow = 80 | Projectile | AbstractArrow
            Snowball = 81 | Projectile
            ThrownEgg = 82 | Projectile
            Painting = 83
            LargeFireball = 85 | Projectile
            ThrownPotion = 86 | Projectile
            Enderpearl = 87 | Projectile
            LeashKnot = 88
            WitherSkull = 89 | Projectile
            BoatRideable = 90
            WitherSkullDangerous = 91 | Projectile
            LightningBolt = 93
            SmallFireball = 94 | Projectile
            AreaEffectCloud = 95
            LingeringPotion = 101 | Projectile
            LlamaSpit = 102 | Projectile
            EvocationFang = 103 | Projectile
            EvocationIllager = 104 | Monster
            Vex = 105 | Monster
            MinecartRideable = 84 | Minecart
            MinecartHopper = 96 | Minecart
            MinecartTNT = 97 | Minecart
            MinecartChest = 98 | Minecart
            MinecartFurnace = 99 | Minecart
            MinecartCommandBlock = 100 | Minecart
            IceBomb = 106 | Projectile
            Balloon = 107
            Pufferfish = 108 | WaterAnimal
            Salmon = 109 | WaterAnimal
            Drowned = 110 | ZombieMonster
            Tropicalfish = 111 | WaterAnimal
            Fish = 112 | WaterAnimal
            Panda = 113 | Animal
            Pillager = 114 | Monster
            EntityExtension = 255
            MAX_ENTITY_ID = 256

        class BlockType(object):
            stone = 1
            grass = 2
            dirt = 3
            cobblestone = 4
            planks = 5
            sapling = 6
            bedrock = 7
            flowing_water = 8
            water = 9
            flowing_lava = 10
            lava = 11
            sand = 12
            gravel = 13
            gold_ore = 14
            iron_ore = 15
            coal_ore = 16
            log = 17
            leaves = 18
            sponge = 19
            glass = 20
            lapis_ore = 21
            lapis_block = 22
            dispenser = 23
            sandstone = 24
            noteblock = 25
            bed = 26
            golden_rail = 27
            detector_rail = 28
            sticky_piston = 29
            web = 30
            tallgrass = 31
            deadbush = 32
            piston = 33
            pistonArmCollision = 34
            wool = 35
            yellow_flower = 37
            red_flower = 38
            brown_mushroom = 39
            red_mushroom = 40
            gold_block = 41
            iron_block = 42
            stone_slab = 44
            double_stone_slab = 43
            brick_block = 45
            tnt = 46
            bookshelf = 47
            mossy_cobblestone = 48
            obsidian = 49
            torch = 50
            mob_spawner = 52
            oak_stairs = 53
            chest = 54
            redstone_wire = 55
            diamond_ore = 56
            diamond_block = 57
            crafting_table = 58
            wheat = 59
            farmland = 60
            furnace = 61
            lit_furnace = 62
            standing_sign = 63
            wooden_door = 64
            ladder = 65
            rail = 66
            stone_stairs = 67
            wall_sign = 68
            lever = 69
            stone_pressure_plate = 70
            iron_door = 71
            wooden_pressure_plate = 72
            redstone_ore = 73
            lit_redstone_ore = 74
            unlit_redstone_torch = 75
            redstone_torch = 76
            stone_button = 77
            snow_layer = 78
            ice = 79
            snow = 80
            cactus = 81
            clay = 82
            reeds = 83
            jukebox = 84
            fence = 85
            pumpkin = 86
            netherrack = 87
            soul_sand = 88
            glowstone = 89
            portal = 90
            lit_pumpkin = 91
            cake = 92
            unpowered_repeater = 93
            powered_repeater = 94
            invisibleBedrock = 95
            trapdoor = 96
            monster_egg = 97
            stonebrick = 98
            brown_mushroom_block = 99
            red_mushroom_block = 100
            iron_bars = 101
            glass_pane = 102
            melon_block = 103
            pumpkin_stem = 104
            melon_stem = 105
            vine = 106
            fence_gate = 107
            brick_stairs = 108
            stone_brick_stairs = 109
            mycelium = 110
            waterlily = 111
            nether_brick = 112
            nether_brick_fence = 113
            nether_brick_stairs = 114
            nether_wart = 115
            enchanting_table = 116
            brewing_stand = 117
            cauldron = 118
            end_portal = 119
            end_portal_frame = 120
            end_stone = 121
            dragon_egg = 122
            redstone_lamp = 123
            lit_redstone_lamp = 124
            dropper = 125
            activator_rail = 126
            cocoa = 127
            sandstone_stairs = 128
            emerald_ore = 129
            ender_chest = 130
            tripwire_hook = 131
            tripWire = 132
            emerald_block = 133
            spruce_stairs = 134
            birch_stairs = 135
            jungle_stairs = 136
            command_block = 137
            beacon = 138
            cobblestone_wall = 139
            flower_pot = 140
            carrots = 141
            potatoes = 142
            wooden_button = 143
            skull = 144
            anvil = 145
            trapped_chest = 146
            light_weighted_pressure_plate = 147
            heavy_weighted_pressure_plate = 148
            unpowered_comparator = 149
            powered_comparator = 150
            daylight_detector = 151
            redstone_block = 152
            quartz_ore = 153
            hopper = 154
            quartz_block = 155
            quartz_stairs = 156
            wooden_slab = 158
            double_wooden_slab = 157
            stained_hardened_clay = 159
            stained_glass_pane = 160
            leaves2 = 161
            log2 = 162
            acacia_stairs = 163
            dark_oak_stairs = 164
            slime = 165
            iron_trapdoor = 167
            prismarine = 168
            seaLantern = 169
            hay_block = 170
            carpet = 171
            hardened_clay = 172
            coal_block = 173
            packed_ice = 174
            double_plant = 175
            standing_banner = 176
            wall_banner = 177
            daylight_detector_inverted = 178
            red_sandstone = 179
            red_sandstone_stairs = 180
            stone_slab2 = 182
            double_stone_slab2 = 181
            spruce_fence_gate = 183
            birch_fence_gate = 184
            jungle_fence_gate = 185
            dark_oak_fence_gate = 186
            acacia_fence_gate = 187
            repeating_command_block = 188
            chain_command_block = 189
            spruce_door = 193
            birch_door = 194
            jungle_door = 195
            acacia_door = 196
            dark_oak_door = 197
            grass_path = 198
            frame = 199
            chorus_flower = 200
            purpur_block = 201
            purpur_stairs = 203
            undyed_shulker_box = 205
            end_bricks = 206
            frosted_ice = 207
            end_rod = 208
            end_gateway = 209
            magma = 213
            nether_wart_block = 214
            red_nether_brick = 215
            bone_block = 216
            shulker_box = 218
            purple_glazed_terracotta = 219
            white_glazed_terracotta = 220
            orange_glazed_terracotta = 221
            magenta_glazed_terracotta = 222
            light_blue_glazed_terracotta = 223
            yellow_glazed_terracotta = 224
            lime_glazed_terracotta = 225
            pink_glazed_terracotta = 226
            gray_glazed_terracotta = 227
            silver_glazed_terracotta = 228
            cyan_glazed_terracotta = 229
            blue_glazed_terracotta = 231
            brown_glazed_terracotta = 232
            green_glazed_terracotta = 233
            red_glazed_terracotta = 234
            black_glazed_terracotta = 235
            concrete = 236
            concretePowder = 237
            chorus_plant = 240
            stained_glass = 241
            podzol = 243
            beetroot = 244
            stonecutter = 245
            glowingobsidian = 246
            netherreactor = 247
            info_update = 248
            info_update2 = 249
            movingBlock = 250
            observer = 251
            structure_block = 252
            reserved6 = 255
            prismarine_stairs = 257
            dark_prismarine_stairs = 258
            prismarine_bricks_stairs = 259
            stripped_spruce_log = 260
            stripped_birch_log = 261
            stripped_jungle_log = 262
            stripped_acacia_log = 263
            stripped_dark_oak_log = 264
            stripped_oak_log = 265
            blue_ice = 266
            fire = 51
            chemistry_table = 238
            underwater_torch = 239
            hard_glass = 253
            hard_stained_glass = 254
            hard_glass_pane = 190
            hard_stained_glass_pane = 191
            chemical_heat = 192
            colored_torch_rg = 202
            colored_torch_bp = 204
            mod_ore = 230
            element_0 = 36
            coral = 386
            coral_block = 387
            coral_fan = 388
            coral_fan_dead = 389
            coral_fan_hang = 390
            coral_fan_hang2 = 391
            coral_fan_hang3 = 392
            kelp = 393
            dried_kelp_block = 394
            seagrass = 385
            acacia_button = 395
            birch_button = 396
            dark_oak_button = 397
            jungle_button = 398
            spruce_button = 399
            acacia_trapdoor = 400
            birch_trapdoor = 401
            dark_oak_trapdoor = 402
            jungle_trapdoor = 403
            spruce_trapdoor = 404
            acacia_pressure_plate = 405
            birch_pressure_plate = 406
            dark_oak_pressure_plate = 407
            jungle_pressure_plate = 408
            spruce_pressure_plate = 409
            carved_pumpkin = 410
            sea_pickle = 411
            conduit = 412
            bubble_column = 415
            turtle_egg = 414
            barrier = 416
            scaffolding = 420
            bamboo = 418
            bamboo_sapling = 419
            stone_slab3 = 417
            stone_slab4 = 421
            double_stone_slab3 = 422
            double_stone_slab4 = 423
            granite_stairs = 424
            diorite_stairs = 425
            andesite_stairs = 426
            polished_granite_stairs = 427
            polished_diorite_stairs = 428
            polished_andesite_stairs = 429
            mossy_stone_brick_stairs = 430
            smooth_red_sandstone_stairs = 431
            smooth_sandstone_stairs = 432
            end_brick_stairs = 433
            mossy_cobblestone_stairs = 434
            normal_stone_stairs = 435
            smooth_stone = 438
            red_nether_brick_stairs = 439
            smooth_quartz_stairs = 440
            spruce_standing_sign = 436
            spruce_wall_sign = 437
            birch_standing_sign = 441
            birch_wall_sign = 442
            jungle_standing_sign = 443
            jungle_wall_sign = 444
            acacia_standing_sign = 445
            acacia_wall_sign = 446
            darkoak_standing_sign = 447
            darkoak_wall_sign = 448
            grindstone = 450
            blast_furnace = 451
            smoker = 453
            cartography_table = 455
            fletching_table = 456
            smithing_table = 457
            barrel = 458
            bell = 461
            lantern = 463
            lava_cauldron = 465

        class SysSoundType(object):
            ItemUseOn = 0
            Hit = 1
            Step = 2
            Fly = 3
            Jump = 4
            Break = 5
            Place = 6
            HeavyStep = 7
            Gallop = 8
            Fall = 9
            Ambient = 10
            AmbientBaby = 11
            AmbientInWater = 12
            Breathe = 13
            Death = 14
            DeathInWater = 15
            DeathToZombie = 16
            Hurt = 17
            HurtInWater = 18
            Mad = 19
            Boost = 20
            Bow = 21
            SquishBig = 22
            SquishSmall = 23
            FallBig = 24
            FallSmall = 25
            Splash = 26
            Fizz = 27
            Flap = 28
            Swim = 29
            Drink = 30
            Eat = 31
            Takeoff = 32
            Shake = 33
            Plop = 34
            Land = 35
            Saddle = 36
            Armor = 37
            ArmorPlace = 38
            AddChest = 39
            Throw = 40
            Attack = 41
            AttackNoDamage = 42
            AttackStrong = 43
            Warn = 44
            Shear = 45
            Milk = 46
            Thunder = 47
            Explode = 48
            Fire = 49
            Ignite = 50
            Fuse = 51
            Stare = 52
            Spawn = 53
            Shoot = 54
            BreakBlock = 55
            Launch = 56
            Blast = 57
            LargeBlast = 58
            Twinkle = 59
            Remedy = 60
            Unfect = 61
            LevelUp = 62
            BowHit = 63
            BulletHit = 64
            ExtinguishFire = 65
            ItemFizz = 66
            ChestOpen = 67
            ChestClosed = 68
            ShulkerBoxOpen = 69
            ShulkerBoxClosed = 70
            EnderChestOpen = 71
            EnderChestClosed = 72
            PowerOn = 73
            PowerOff = 74
            Attach = 75
            Detach = 76
            Deny = 77
            Tripod = 78
            Pop = 79
            DropSlot = 80
            Note = 81
            Thorns = 82
            PistonIn = 83
            PistonOut = 84
            Portal = 85
            Water = 86
            LavaPop = 87
            Lava = 88
            Burp = 89
            BucketFillWater = 90
            BucketFillLava = 91
            BucketEmptyWater = 92
            BucketEmptyLava = 93
            EquipChain = 94
            EquipDiamond = 95
            EquipGeneric = 96
            EquipGold = 97
            EquipIron = 98
            EquipLeather = 99
            EquipElytra = 100
            Record13 = 101
            RecordCat = 102
            RecordBlocks = 103
            RecordChirp = 104
            RecordFar = 105
            RecordMall = 106
            RecordMellohi = 107
            RecordStal = 108
            RecordStrad = 109
            RecordWard = 110
            Record11 = 111
            RecordWait = 112
            RecordNull = 113
            Flop = 114
            GuardianCurse = 115
            MobWarning = 116
            MobWarningBaby = 117
            Teleport = 118
            ShulkerOpen = 119
            ShulkerClose = 120
            Haggle = 121
            HaggleYes = 122
            HaggleNo = 123
            HaggleIdle = 124
            ChorusGrow = 125
            ChorusDeath = 126
            Glass = 127
            PotionBrewed = 128
            CastSpell = 129
            PrepareAttackSpell = 130
            PrepareSummon = 131
            PrepareWololo = 132
            Fang = 133
            Charge = 134
            TakePicture = 135
            PlaceLeashKnot = 136
            BreakLeashKnot = 137
            AmbientGrowl = 138
            AmbientWhine = 139
            AmbientPant = 140
            AmbientPurr = 141
            AmbientPurreow = 142
            DeathMinVolume = 143
            DeathMidVolume = 144
            ImitateBlaze = 145
            ImitateCaveSpider = 146
            ImitateCreeper = 147
            ImitateElderGuardian = 148
            ImitateEnderDragon = 149
            ImitateEnderman = 150
            ImitateEndermite = 151
            ImitateEvocationIllager = 152
            ImitateGhast = 153
            ImitateHusk = 154
            ImitateIllusionIllager = 155
            ImitateMagmaCube = 156
            ImitatePolarBear = 157
            ImitateShulker = 158
            ImitateSilverfish = 159
            ImitateSkeleton = 160
            ImitateSlime = 161
            ImitateSpider = 162
            ImitateStray = 163
            ImitateVex = 164
            ImitateVindicationIllager = 165
            ImitateWitch = 166
            ImitateWither = 167
            ImitateWitherSkeleton = 168
            ImitateWolf = 169
            ImitateZombie = 170
            ImitateZombiePigman = 171
            ImitateZombieVillager = 172
            EnderEyePlaced = 173
            EndPortalCreated = 174
            AnvilUse = 175
            BottleDragonBreath = 176
            PortalTravel = 177
            TridentHit = 178
            TridentReturn = 179
            TridentRiptide_1 = 180
            TridentRiptide_2 = 181
            TridentRiptide_3 = 182
            TridentThrow = 183
            TridentThunder = 184
            TridentHitGround = 185
            Default = 186
            ElemConstructOpen = 188
            IceBombHit = 189
            BalloonPop = 190
            LTReactionIceBomb = 191
            LTReactionBleach = 192
            LTReactionElephantToothpaste = 193
            LTReactionElephantToothpaste2 = 194
            LTReactionGlowStick = 195
            LTReactionGlowStick2 = 196
            LTReactionLuminol = 197
            LTReactionSalt = 198
            LTReactionFertilizer = 199
            LTReactionFireball = 200
            LTReactionMagnesiumSalt = 201
            LTReactionMiscFire = 202
            LTReactionFire = 203
            LTReactionMiscExplosion = 204
            LTReactionMiscMystical = 205
            LTReactionMiscMystical2 = 206
            LTReactionProduct = 207
            SparklerUse = 208
            GlowStickUse = 209
            SparklerActive = 210
            ConvertToDrowned = 211
            BucketFillFish = 212
            BucketEmptyFish = 213
            BubbleColumnUpwards = 214
            BubbleColumnDownwards = 215
            BubblePop = 216
            BubbleUpInside = 217
            BubbleDownInside = 218
            HurtBaby = 219
            DeathBaby = 220
            StepBaby = 221
            SpawnBaby = 222
            Born = 223
            TurtleEggBreak = 224
            TurtleEggCrack = 225
            TurtleEggHatched = 226
            LayEgg = 227
            TurtleEggAttacked = 228
            BeaconActivate = 229
            BeaconAmbient = 230
            BeaconDeactivate = 231
            BeaconPower = 232
            ConduitActivate = 233
            ConduitAmbient = 234
            ConduitAttack = 235
            ConduitDeactivate = 236
            ConduitShort = 237
            Swoop = 238
            BambooSaplingPlace = 239
            PreSneeze = 240
            Sneeze = 241
            AmbientTame = 242
            Scared = 243
            ScaffoldingClimb = 244
            CrossbowLoadingStart = 245
            CrossbowLoadingMiddle = 246
            CrossbowLoadingEnd = 247
            CrossbowShoot = 248
            CrossbowQuickChargeStart = 249
            CrossbowQuickChargeMiddle = 250
            CrossbowQuickChargeEnd = 251
            AmbientAggressive = 252
            AmbientWorried = 253
            CantBreed = 254
            Undefined = 255

        class EntityConst(object):
            TYPE_LVOBJ = "lvobj"
            TYPE_ENTITY = "entity"
            TYPE_MONSTER = "monster"
            TYPE_PLAYER = "player"
            TYPE_BULLET = "bullet"
            TYPE_SFX = "sfx"
            TYPE_BUFF = "buff"
            TYPE_PARTICLE = "particle"
            TYPE_FONT = "font"
            TYPE_TEAM = "team"
            TYPE_ITEM_ENTITY = "item_entity"
            TYPE_NPC = "npc"
            TYPE_MOD_ENTITY = "mod_entity"

        class BiomeType(object):
            plains = 1
            desert = 2
            extreme_hills = 3
            forest = 4
            taiga = 5
            swampland = 6
            river = 7
            hell = 8
            the_end = 9
            legacy_frozen_ocean = 10
            frozen_river = 11
            ice_plains = 12
            ice_mountains = 13
            mushroom_island = 14
            mushroom_island_shore = 15
            beach = 16
            desert_hills = 17
            forest_hills = 18
            taiga_hills = 19
            extreme_hills_edge = 20
            jungle = 21
            jungle_hills = 22
            jungle_edge = 23

            stone_beach = 25
            cold_beach = 26
            birch_forest = 27
            birch_forest_hills = 28
            roofed_forest = 29
            cold_taiga = 30
            cold_taiga_hills = 31
            mega_taiga = 32
            mega_taiga_hills = 33
            extreme_hills_plus_trees = 34
            savanna = 35
            savanna_plateau = 36
            mesa = 37
            mesa_plateau_stone = 38
            mesa_plateau = 39
            ocean = 0
            deep_ocean = 24
            warm_ocean = 40
            deep_warm_ocean = 41
            lukewarm_ocean = 42
            deep_lukewarm_ocean = 43
            cold_ocean = 44
            deep_cold_ocean = 45
            frozen_ocean = 46
            deep_frozen_ocean = 47

        class Change(object):
            Add = 0
            Remove = 1
    return __MinecraftEnum


def GetViewViewRequestCls():
    class __ViewRequest(object):
        Nothing = 0
        Refresh = 1 << 0
        PointerHeldEventsRequest = 1 << 1
        PointerHeldEventsCancel = 1 << 2
        Exit = 1 << 3
    return __ViewRequest


def GetViewBinderCls():
    class __ViewBinder(object):
        ButtonFilter = 0x10000000
        BF_ButtonClickUp = 0 | ButtonFilter
        BF_ButtonClickDown = 1 | ButtonFilter
        BF_ButtonClick = 2 | ButtonFilter
        BF_ButtonClickCancel = 3
        BF_InteractButtonClick = 4
        BindFilter = 0x01000000
        BF_BindBool = 5 | BindFilter
        BF_BindInt = 6 | BindFilter
        BF_BindFloat = 7 | BindFilter
        BF_BindString = 8 | BindFilter
        BF_BindGridSize = 9 | BindFilter
        BF_BindColor = 10 | BindFilter
        EditFilter = 0x00100000
        BF_EditChanged = 11 | EditFilter
        BF_EditFinished = 12 | EditFilter

        @staticmethod
        def binding(bind_flag, binding_name=None):
            pass

        @staticmethod
        def binding_collection(bind_flag, collection_name, binding_name=None):
            pass
    return __ViewBinder


def GetClientSystemCls():
    class __ClientSystem(object):
        class __NeedUpdate(object):
            def __init__(self):
                pass

            def get(self, key, defaultValue):
                pass

        class _Component(object):
            def __init__(self):
                self.pos = None
                self.frontColor = None
                self.backColor = None
                self.showHealth = None
                self.rot = None
                self.path = None
                self.engineType = None
                self.auxValue = None
                self.name = None
                self.volume = None
                self.pitch = None
                self.needPlay = None
                self.soundId = None
                self.entityType = None
                self.blockId = None
                self.isBaby = None
                self.isGlobal = None
                self.scale = None
                self.open = None
                self.faceCamera = None
                self.loop = None
                self.bindEntityId = None
                self.offset = None
                self.modelName = None
                self.boneName = None
                self.aniName = None
                self.isLoop = None
                self.weapon = None
                self.modelId = None
                self.bodyAniName = None
                self.bodyIsLoop = None
                self.legAniName = None
                self.legIsLoop = None
                self.texture = None
                self.skin = None
                self.speed = None
                self.aniPlayingName = None
                self.relative = None
                self.ownerId = None
                self.textId = None
                self.size = None
                self.textColor = None
                self.tagColor = None
                self.depthTest = None
                self.needUpdatePos = None
                self.offhandItem = None
                self.carriedItem = None
                self.slotId = None
                self.itemId = None
                self.count = None
                self.showInHand = None
                self.modId = None
                self.modItemId = None
                self.fov = None
                self.lockPos = None
                self.lockRot = None
                self.lockCamera = None
                self.fpHeight = None
                self.showHealthBar = None
                self.nameDeeptest = None
                self.screenSize = None
                self.renderLocalPlayer = None
                self.showName = None
                self.move = None
                self.jump = None
                self.attack = None
                self.walkmode = None
                self.perspective = None
                self.pause = None
                self.chat = None
                self.screenshot = None
                self.openinv = None
                self.drag = None
                self.inair = None
                self.all = None
                self.moveLock = None
                self.is_hook = None
                self.motion = None
                self.inputMoveVector = None
                self.type = None

        def __init__(self, namespace, systemName):
            pass

        def CreateComponent(self, entityId, nameSpace, name):
            return self._Component()

        def GetComponent(self, entityId, nameSpace, name):
            return self._Component()

        def DestroyComponent(self, entityId, nameSpace, name):
            pass

        def GetCompData(self, comp, moduleName, funcName, *args):
            pass

        def CreateTempEntity(self):
            pass

        def CreateEntity(self, tempEntity):
            pass

        def DestroyEntity(self, entityId):
            pass

        def DefineEvent(self, eventName):
            pass

        def UnDefineEvent(self, eventName):
            pass

        def CreateEventData(self):
            pass

        def ListenForEvent(self, namespace, systemName, eventName, instance, func):
            pass

        def UnListenForEvent(self, namespace, systemName, eventName, instance, func):
            pass

        def BroadcastEvent(self, eventName, eventData):
            pass

        def NotifyToServer(self, eventName, eventData):
            pass

        def NeedsUpdate(self, comp):
            pass

        def GetNeedUpdate(self):
            return self.__NeedUpdate()

        def Update(self):
            pass

        def Destroy(self):
            pass
    return __ClientSystem


def GetScreenNodeCls():
    class __ScreenNode(object):
        def __init__(self, namespace, name, param):
            pass

        def Create(self):
            pass

        def Init(self):
            pass

        def Update(self):
            pass
    return __ScreenNode


def GetComponentCls():
    class __ComponentCls(object):
        def __init__(self, entityId):
            pass
    return __ComponentCls


def GetUI(myModName, key):
    class __uiNode(object):
        def SetScreenVisible(self, visible):
            pass

        def SetVisible(self, componentPath, visible):
            pass

        def GetPosition(self, componentPath):
            pass

        def SetPosition(self, componentPath, pos):
            pass

        def GetSize(self, componentPath):
            pass

        def SetSize(self, componentPath, size):
            pass

        def SetTouchEnable(self, componentPath, enable):
            pass

        def Clone(self, componentPath, parentPath, newName):
            pass

        def SetRemove(self):
            pass

        def RemoveComponent(self, componentPath, parentPath):
            pass

        def SetCrossHair(self, invisible):
            pass

        def GetTextColor(self, componentPath):
            pass

        def SetTextColor(self, componentPath, color):
            pass

        def SetText(self, componentPath, text):
            pass

        def SetEditTextMaxLength(self, componentPath, maxLength):
            pass

        def SetSprite(self, componentPath, texturePath):
            pass

        def SetSpriteGray(self, componentPath, gray):
            pass

        def SetSpriteBright(self, componentPath, bright):
            pass
    return __uiNode


def RegisterComponent(nameSpace, name, clsPath):
    pass


def RegisterSystem(nameSpace, systemName, clsPath):
    pass


def GetLocalPlayerId():
    pass


def GetEngineNamespace():
    pass


def GetEngineSystemName():
    pass


def GetLevelId():
    pass


def NeedsUpdate(comp):
    pass


def HideHudGUI(hide):
    pass


def SetResponse(response):
    pass


def SetInputMode(mode):
    pass


def GetInputVector():
    pass


def SetTextDefaultFont(font):
    pass


def RegisterUI(myModName, key, clsPath, uiDef):
    pass


def CreateUI(myModName, key, paramDict=None):
    pass


def GenerateColor(color):
    pass


def GetTouchPos():
    pass


# TODO: find out what this is
def CreateComponent(levelId, nameSpace, name):
    return GetClientSystemCls()._Component()


# TODO: find out what this is
def GetComponent(levelId, nameSpace, name):
    return GetClientSystemCls()._Component()
