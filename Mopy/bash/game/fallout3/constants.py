# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#  This file is part of Wrye Bash.
#
#  Wrye Bash is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  Wrye Bash is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Wrye Bash; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  Wrye Bash copyright (C) 2005-2009 Wrye, 2010-2014 Wrye Bash Team
#  https://github.com/wrye-bash
#
# =============================================================================

#--Game ESM/ESP/BSA files
#  These filenames need to be in lowercase,
bethDataFiles = set((
    #--Vanilla
    ur'fallout3.esm',
    ur'fallout - menuvoices.bsa',
    ur'fallout - meshes.bsa',
    ur'fallout - misc.bsa',
    ur'fallout - sound.bsa',
    ur'fallout - textures.bsa',
    ur'fallout - voices.bsa',
    #-- DLC
    ur'anchorage.esm',
    ur'anchorage - main.bsa',
    ur'anchorage - sounds.bsa',
    ur'thepitt.esm',
    ur'thepitt - main.bsa',
    ur'thepitt - sounds.bsa',
    ur'brokensteel.esm',
    ur'brokensteel - main.bsa',
    ur'brokensteel - sounds.bsa',
    ur'pointlookout.esm',
    ur'pointlookout - main.bsa',
    ur'pointlookout - sounds.bsa',
    ur'zeta.esm',
    ur'zeta - main.bsa',
    ur'zeta - sounds.bsa',
    ))

#--Every file in the Data directory from Bethsoft
allBethFiles = set((
    # Section 1: Vanilla files
    ur'Credits.txt',
    ur'CreditsWacky.txt',
    ur'Fallout3.esm',
    ur'Fallout - MenuVoices.bsa',
    ur'Fallout - Meshes.bsa',
    ur'Fallout - Misc.bsa',
    ur'Fallout - Sound.bsa',
    ur'Fallout - Textures.bsa',
    ur'Fallout - Voices.bsa',
    ur'LODSettings\aaaForgotten1.DLODSettings',
    ur'LODSettings\aaaForgotten4.DLODSettings',
    ur'LODSettings\aaaForgotten5.DLODSettings',
    ur'Music\Base\Base_01.mp3',
    ur'Music\Base\Base_02.mp3',
    ur'Music\Base\Base_03.mp3',
    ur'Music\Base\Base_04.mp3',
    ur'Music\Battle\Battle_01.mp3',
    ur'Music\Battle\Battle_02.mp3',
    ur'Music\Battle\Battle_03.mp3',
    ur'Music\Battle\Battle_04.mp3',
    ur'Music\Battle\Battle_05.mp3',
    ur'Music\Battle\Battle_06.mp3',
    ur'Music\Battle\Battle_07.mp3',
    ur'Music\Battle\Finale\Battle_01.mp3',
    ur'Music\Battle\Finale\Battle_02.mp3',
    ur'Music\Battle\Finale\Battle_03.mp3',
    ur'Music\Battle\Finale\Battle_04.mp3',
    ur'Music\Battle\Finale\Battle_05.mp3',
    ur'Music\Battle\Finale\Battle_06.mp3',
    ur'Music\Battle\Finale\Battle_07.mp3',
    ur'Music\Dungeon\Dungeon_01.mp3',
    ur'Music\Dungeon\Dungeon_02.mp3',
    ur'Music\Dungeon\Dungeon_03.mp3',
    ur'Music\Dungeon\Dungeon_04.mp3',
    ur'Music\Dungeon\Dungeon_05.mp3',
    ur'Music\Endgame\Endgame_01.mp3',
    ur'Music\Endgame\Endgame_02.mp3',
    ur'Music\Endgame\Endgame_03.mp3',
    ur'Music\Endgame\Endgame_04.mp3',
    ur'Music\Endgame\Endgame_05.mp3',
    ur'Music\Endgame\Endgame_06.mp3',
    ur'Music\Endgame\Endgame_07.mp3',
    ur'Music\Endgame\Endgame_08.mp3',
    ur'Music\Endgame\Endgame_09.mp3',
    ur'Music\Endgame\Endgame_11.mp3',
    ur'Music\Endgame\Endgame_12.mp3',
    ur'Music\Endgame\Endgame_14.mp3',
    ur'Music\Endgame\Endgame_15.mp3',
    ur'Music\Endgame\Endgame_17.mp3',
    ur'Music\Endgame\Endgame_18.mp3',
    ur'Music\Endgame\Endgame_19.mp3',
    ur'Music\Explore\Explore_01.mp3',
    ur'Music\Explore\Explore_02.mp3',
    ur'Music\Explore\Explore_03.mp3',
    ur'Music\Explore\Explore_04.mp3',
    ur'Music\Explore\Explore_05.mp3',
    ur'Music\Explore\Explore_06.mp3',
    ur'Music\Explore\Explore_07.mp3',
    ur'Music\Public\Public_01.mp3',
    ur'Music\Public\Public_02.mp3',
    ur'Music\Public\Public_03.mp3',
    ur'Music\Public\Public_04.mp3',
    ur'Music\Public\Public_05.mp3',
    ur'Music\Special\Death.mp3',
    ur'Music\Special\ExitTheVault.mp3',
    ur'Music\Special\MainTitle.mp3',
    ur'Music\Special\Success.mp3',
    ur'Music\Tension\Tension_01.mp3',
    ur'Music\TranquilityLane\MUS_TranquilityLane_01_LP.mp3',
    ur'Music\TranquilityLane\MUS_TranquilityLane_02_LP.mp3',
    ur'Shaders\shaderpackage002.sdp',
    ur'Shaders\shaderpackage003.sdp',
    ur'Shaders\shaderpackage004.sdp',
    ur'Shaders\shaderpackage006.sdp',
    ur'Shaders\shaderpackage007.sdp',
    ur'Shaders\shaderpackage009.sdp',
    ur'Shaders\shaderpackage010.sdp',
    ur'Shaders\shaderpackage011.sdp',
    ur'Shaders\shaderpackage012.sdp',
    ur'Shaders\shaderpackage013.sdp',
    ur'Shaders\shaderpackage014.sdp',
    ur'Shaders\shaderpackage015.sdp',
    ur'Shaders\shaderpackage016.sdp',
    ur'Shaders\shaderpackage017.sdp',
    ur'Shaders\shaderpackage018.sdp',
    ur'Shaders\shaderpackage019.sdp',
    ur'Video\1 year later.bik',
    ur'Video\2 weeks later.bik',
    ur'Video\3 years later.bik',
    ur'Video\6 years later.bik',
    ur'Video\9 years later.bik',
    ur'Video\B01.bik',
    ur'Video\B02.bik',
    ur'Video\B03.bik',
    ur'Video\B04.bik',
    ur'Video\B05.bik',
    ur'Video\B06.bik',
    ur'Video\B07.bik',
    ur'Video\B08.bik',
    ur'Video\B09.bik',
    ur'Video\B10.bik',
    ur'Video\B11.bik',
    ur'Video\B12.bik',
    ur'Video\B13.bik',
    ur'Video\B14.bik',
    ur'Video\B15.bik',
    ur'Video\B16.bik',
    ur'Video\B17.bik',
    ur'Video\B18.bik',
    ur'Video\B19.bik',
    ur'Video\B20.bik',
    ur'Video\B21.bik',
    ur'Video\B22.bik',
    ur'Video\B23.bik',
    ur'Video\B24.bik',
    ur'Video\B25.bik',
    ur'Video\B26.bik',
    ur'Video\B27.bik',
    ur'Video\B28.bik',
    ur'Video\B29.bik',
    ur'Video\Fallout INTRO Vsk.bik',
    # Section 2: DLCs
    ur'anchorage.esm',
    ur'anchorage - main.bsa',
    ur'anchorage - sounds.bsa',
    ur'thepitt.esm',
    ur'thepitt - main.bsa',
    ur'thepitt - sounds.bsa',
    ur'brokensteel.esm',
    ur'brokensteel - main.bsa',
    ur'brokensteel - sounds.bsa',
    ur'pointlookout.esm',
    ur'pointlookout - main.bsa',
    ur'pointlookout - sounds.bsa',
    ur'zeta.esm',
    ur'zeta - main.bsa',
    ur'zeta - sounds.bsa',
    ur'DLCList.txt',
    ))
# Function Info ---------------------------------------------------------------
conditionFunctionData = ( #--0: no param; 1: int param; 2: formid param
    (  1, 'GetDistance', 2, 0),
    (  5, 'GetLocked', 0, 0),
    (  6, 'GetPos', 1, 0),
    (  8, 'GetAngle', 1, 0),
    ( 10, 'GetStartingPos', 1, 0),
    ( 11, 'GetStartingAngle', 1, 0),
    ( 12, 'GetSecondsPassed', 0, 0),
    ( 14, 'GetActorValue', 1, 0),
    ( 18, 'GetCurrentTime', 0, 0),
    ( 24, 'GetScale', 0, 0),
    ( 25, 'IsMoving', 0, 0),
    ( 26, 'IsTurning', 0, 0),
    ( 27, 'GetLineOfSight', 2, 0),
    ( 32, 'GetInSameCell', 2, 0),
    ( 35, 'GetDisabled', 0, 0),
    ( 36, 'MenuMode', 1, 0),
    ( 39, 'GetDisease', 0, 0),
    ( 40, 'GetVampire', 0, 0),
    ( 41, 'GetClothingValue', 0, 0),
    ( 42, 'SameFaction', 2, 0),
    ( 43, 'SameRace', 2, 0),
    ( 44, 'SameSex', 2, 0),
    ( 45, 'GetDetected', 2, 0),
    ( 46, 'GetDead', 0, 0),
    ( 47, 'GetItemCount', 2, 0),
    ( 48, 'GetGold', 0, 0),
    ( 49, 'GetSleeping', 0, 0),
    ( 50, 'GetTalkedToPC', 0, 0),
    ( 53, 'GetScriptVariable', 2, 1),
    ( 56, 'GetQuestRunning', 2, 0),
    ( 58, 'GetStage', 2, 0),
    ( 59, 'GetStageDone', 2, 1),
    ( 60, 'GetFactionRankDifference', 2, 2),
    ( 61, 'GetAlarmed', 0, 0),
    ( 62, 'IsRaining', 0, 0),
    ( 63, 'GetAttacked', 0, 0),
    ( 64, 'GetIsCreature', 0, 0),
    ( 65, 'GetLockLevel', 0, 0),
    ( 66, 'GetShouldAttack', 2, 0),
    ( 67, 'GetInCell', 2, 0),
    ( 68, 'GetIsClass', 2, 0),
    ( 69, 'GetIsRace', 2, 0),
    ( 70, 'GetIsSex', 1, 0),
    ( 71, 'GetInFaction', 2, 0),
    ( 72, 'GetIsID', 2, 0),
    ( 73, 'GetFactionRank', 2, 0),
    ( 74, 'GetGlobalValue', 2, 0),
    ( 75, 'IsSnowing', 0, 0),
    ( 76, 'GetDisposition', 2, 0),
    ( 77, 'GetRandomPercent', 0, 0),
    ( 79, 'GetQuestVariable', 2, 1),
    ( 80, 'GetLevel', 0, 0),
    ( 81, 'GetArmorRating', 0, 0),
    ( 84, 'GetDeadCount', 2, 0),
    ( 91, 'GetIsAlerted', 0, 0),
    ( 98, 'GetPlayerControlsDisabled', 0, 0),
    ( 99, 'GetHeadingAngle', 2, 0),
    (101, 'IsWeaponOut', 0, 0),
    (102, 'IsTorchOut', 0, 0),
    (103, 'IsShieldOut', 0, 0),
    (106, 'IsFacingUp', 0, 0),
    (107, 'GetKnockedState', 0, 0),
    (108, 'GetWeaponAnimType', 0, 0),
    (109, 'IsWeaponSkillType', 1, 0),
    (110, 'GetCurrentAIPackage', 0, 0),
    (111, 'IsWaiting', 0, 0),
    (112, 'IsIdlePlaying', 0, 0),
    (116, 'GetMinorCrimeCount', 0, 0),
    (117, 'GetMajorCrimeCount', 0, 0),
    (122, 'GetCrime', 2, 1),
    (123, 'IsGreetingPlayer', 0, 0),
    (125, 'IsGuard', 0, 0),
    (127, 'HasBeenEatan', 0, 0),
    (128, 'GetFatiguePercentage', 0, 0),
    (129, 'GetPCIsClass', 2, 0),
    (130, 'GetPCIsRace', 2, 0),
    (131, 'GetPCIsSex', 1, 0),
    (132, 'GetPCInFaction', 2, 0),
    (133, 'SameFactionAsPC', 0, 0),
    (134, 'SameRaceAsPC', 0, 0),
    (135, 'SameSexAsPC', 0, 0),
    (136, 'GetIsReference', 2, 0),
    (141, 'IsTalking', 0, 0),
    (142, 'GetWalkSpeed', 0, 0),
    (143, 'GetCurrentAIProcedure', 0, 0),
    (144, 'GetTrespassWarningLevel', 0, 0),
    (145, 'IsTrespassing', 0, 0),
    (146, 'IsInMyOwnedCell', 0, 0),
    (147, 'GetWindSpeed', 0, 0),
    (148, 'GetCurrentWeatherPercent', 0, 0),
    (149, 'GetIsCurrentWeather', 2, 0),
    (150, 'IsContinuingPackagePCNear', 0, 0),
    (153, 'CanHaveFlames', 0, 0),
    (154, 'HasFlames', 0, 0),
    (157, 'GetOpenState', 0, 0),
    (159, 'GetSitting', 0, 0),
    (160, 'GetFurnitureMarkerID', 0, 0),
    (161, 'GetIsCurrentPackage', 2, 0),
    (162, 'IsCurrentFurnitureRef', 2, 0),
    (163, 'IsCurrentFurnitureObj', 2, 0),
    (170, 'GetDayOfWeek', 0, 0),
    (172, 'GetTalkedToPCParam', 2, 0),
    (175, 'IsPCSleeping', 0, 0),
    (176, 'IsPCAMurderer', 0, 0),
    (180, 'GetDetectionLevel', 2, 0),
    (182, 'GetEquipped', 2, 0),
    (185, 'IsSwimming', 0, 0),
    (190, 'GetAmountSoldStolen', 0, 0),
    (193, 'GetPCExpelled', 2, 0),
    (195, 'GetPCFactionMurder', 2, 0),
    (197, 'GetPCEnemyofFaction', 2, 0),
    (199, 'GetPCFactionAttack', 2, 0),
    (203, 'GetDestroyed', 0, 0),
    (214, 'HasMagicEffect', 2, 0),
    (215, 'GetDefaultOpen', 0, 0),
    (219, 'GetAnimAction', 0, 0),
    (223, 'IsSpellTarget', 2, 0),
    (224, 'GetVATSMode', 0, 0),
    (225, 'GetPersuasionNumber', 0, 0),
    (226, 'GetSandman', 0, 0),
    (227, 'HasCannibal', 0, 0),
    (228, 'GetIsClassDefault', 2, 0),
    (229, 'GetClassDefaultMatch', 0, 0),
    (230, 'GetInCellParam', 2, 2),
    (235, 'GetVatsTargetHeight', 0, 0),
    (237, 'GetIsGhost', 0, 0),
    (242, 'GetUnconscious', 0, 0),
    (244, 'GetRestrained', 0, 0),
    (246, 'GetIsUsedItem', 2, 0),
    (247, 'GetIsUsedItemType', 1, 0),
    (254, 'GetIsPlayableRace', 0, 0),
    (255, 'GetOffersServicesNow', 0, 0),
    (258, 'GetUsedItemLevel', 0, 0),
    (259, 'GetUsedItemActivate', 0, 0),
    (264, 'GetBarterGold', 0, 0),
    (265, 'IsTimePassing', 0, 0),
    (266, 'IsPleasant', 0, 0),
    (267, 'IsCloudy', 0, 0),
    (274, 'GetArmorRatingUpperBody', 0, 0),
    (277, 'GetBaseActorValue', 1, 0),
    (278, 'IsOwner', 2, 0),
    (280, 'IsCellOwner', 2, 2),
    (282, 'IsHorseStolen', 0, 0),
    (285, 'IsLeftUp', 0, 0),
    (286, 'IsSneaking', 0, 0),
    (287, 'IsRunning', 0, 0),
    (288, 'GetFriendHit', 2, 0),
    (289, 'IsInCombat', 0, 0),
    (300, 'IsInInterior', 0, 0),
    (304, 'IsWaterObject', 0, 0),
    (306, 'IsActorUsingATorch', 0, 0),
    (309, 'IsXBox', 0, 0),
    (310, 'GetInWorldspace', 2, 0),
    (312, 'GetPCMiscStat', 1, 0),
    (313, 'IsActorEvil', 0, 0),
    (314, 'IsActorAVictim', 0, 0),
    (315, 'GetTotalPersuasionNumber', 0, 0),
    (318, 'GetIdleDoneOnce', 0, 0),
    (320, 'GetNoRumors', 0, 0),
    (323, 'WhichServiceMenu', 0, 0),
    (327, 'IsRidingHorse', 0, 0),
    (332, 'IsInDangerousWater', 0, 0),
    (338, 'GetIgnoreFriendlyHits', 0, 0),
    (339, 'IsPlayersLastRiddenHorse', 0, 0),
    (353, 'IsActor', 0, 0),
    (354, 'IsEssential', 0, 0),
    (358, 'IsPlayerMovingIntoNewSpace', 0, 0),
    (361, 'GetTimeDead', 0, 0),
    (362, 'GetPlayerHasLastRiddenHorse', 0, 0),
    (365, 'IsChild', 0, 0),
    (368, 'IsPlayerActionActive', 1, 0),
    (372, 'IsInList', 2, 0),
    (382, 'GetHasNote', 2, 1),
    (391, 'GetHitLocation', 0, 0),
    (392, 'IsPC1stPerson', 0, 0),
    (397, 'GetCauseofDeath', 0, 0),
    (398, 'IsLimbGone', 1, 0),
    (399, 'IsWeaponInList', 2, 0),
    (408, 'GetVATSValue', 1, 2),
    (411, 'GetFactionCombatReaction', 2, 2),
    (415, 'Exists', 2, 0),
    (416, 'GetGroupMemberCount', 0, 0),
    (417, 'GetGroupTargetCount', 0, 0),
    (420, 'GetObjectiveCompleted', 2, 1),
    (421, 'GetObjectiveDisplayed', 2, 1),
    (427, 'GetIsVoiceType', 2, 0),
    (428, 'GetPlantedExplosive', 0, 0),
    (430, 'IsActorTalkingThroughActivator', 0, 0),
    (431, 'GetHealthPercentage', 0, 0),
    (433, 'GetIsObjectType', 1, 0),
    (435, 'GetDialogueEmotion', 0, 0),
    (438, 'GetIsCreatureType', 1, 0),
    (446, 'GetInZone', 2, 1),
    (449, 'HasPerk', 2, 1),
    (450, 'GetFactionRelation', 1, 0),
    (451, 'IsLastIdlePlayed', 2, 0),
    (454, 'GetPlayerTeammate', 0, 0),
    (455, 'GetPlayerTeammateCount', 0, 0),
    (460, 'GetActorFactionPlayerEnemy', 0, 0),
    (471, 'GetDestructionStage', 0, 0),
    (474, 'GetIsAlignment', 1, 0),
    (480, 'GetIsUsedItemEquipType', 1, 0),
    (492, 'GetMapMakerVisible', 1, 1),
    (495, 'GetPermanentActorValue', 1, 0),
    (500, 'GetWeaponHealthPerc', 0, 0),
    (503, 'GetRadiationLevel', 0, 0),
    (510, 'GetLastHitCritical', 0, 0),
    (515, 'IsCombatTarget', 2, 0),
    (522, 'GetIsLockBroken', 0, 0),
    (523, 'IsPS3', 0, 0),
    (524, 'IsWin32', 0, 0),
    (546, 'GetQuestCompleted', 2, 0),
    (550, 'IsGoreDisabled', 0, 0),

    # extended by FOSE
    (1024, 'GetFOSEVersion', 0, 0),
    (1025, 'GetFOSERevision', 0, 0),
    (1213, 'GetFOSEBeta', 0, 0),
    (1082, 'IsKeyPressed', 1, 0),
    (1166, 'IsControlPressed', 1, 0),
    (1028, 'GetWeight', 2, 0),
    (1165, 'GetWeaponHasScope', 0, 0),
    )
allConditions = set(entry[0] for entry in conditionFunctionData)
fid1Conditions = set(entry[0] for entry in conditionFunctionData if entry[2] == 2)
fid2Conditions = set(entry[0] for entry in conditionFunctionData if entry[3] == 2)

#--List of GMST's in the main plugin (Skyrim.esm) that have 0x00000000
#  as the form id.  Any GMST as such needs it Editor Id listed here.
gmstEids = ['fPlayerDeathReloadTime','iMapMarkerVisibleDistance','fVanityModeWheelMax','fChase3rdPersonZUnitsPerSecond',
    'fAutoAimMaxDegreesMiss','iHoursToRespawnCell','fEssentialDeathTime','fJumpHeightMin','fPlayerPipBoyLightTimer',
    'iAINumberActorsComplexScene','iHackingMaxWords','fGunShellLifetime','fGunShellCameraDistance','fGunDecalCameraDistance',
    'iDebrisMaxCount','iHackingDumpRate','iHackingInputRate','iHackingOutputRate','iHackingFlashOffDuration',
    'iHackingFlashOnDuration','iComputersDisplayRateMenus','iComputersDisplayRateNotes','iInventoryAskQuantityAt',
    'iNumberActorsInCombatPlayer','iNumberActorsAllowedToFollowPlayer','iRemoveExcessDeadCount','iRemoveExcessDeadTotalActorCount',
    'iRemoveExcessDeadComplexTotalActorCount','iRemoveExcessDeadComplexCount', 'fRemoveExcessDeadTime','fRemoveExcessComplexDeadTime',
    'iLevItemLevelDifferenceMax','fMoveWeightMax',
    ]
"""Constants used by the patchers."""

#--GLOB record tweaks used by patcher.patchers.multitweak_settings.GmstTweaker
#  Each entry is a tuple in the following format:
#    (DisplayText, MouseoverText, GLOB EditorID, Option1, Option2, Option3, ..., OptionN)
#    -EditorID can be a plain string, or a tuple of multiple Editor IDs.  If it's a tuple,
#     then Value (below) must be a tuple of equal length, providing values for each GLOB
#  Each Option is a tuple:
#    (DisplayText, Value)
#    - If you enclose DisplayText in brackets like this: _(u'[Default]'), then the patcher
#      will treat this option as the default value.
#    - If you use _(u'Custom') as the entry, the patcher will bring up a number input dialog
#  To make a tweak Enabled by Default, enclose the tuple entry for the tweak in a list, and make
#  a dictionary as the second list item with {'defaultEnabled':True}.  See the UOP Vampire face
#  fix for an example of this (in the GMST Tweaks)
GlobalsTweaks = [
    (_(u'Timescale'),_(u'Timescale will be set to:'),
        u'timescale',
        (u'1',         1),
        (u'8',         8),
        (u'10',       10),
        (u'12',       12),
        (u'20',       20),
        (u'24',       24),
        (u'[30]',     30),
        (u'40',       40),
        (_(u'Custom'), 30),
        ),
    ]

#--GMST record tweaks used by patcher.patchers.multitweak_settings.GmstTweaker
#  Each entry is a tuple in the following format:
#    (DisplayText, MouseoverText, GMST EditorID, Option1, Option2, Option3, ..., OptionN)
#    -EditorID can be a plain string, or a tuple of multiple Editor IDs.  If it's a tuple,
#     then Value (below) must be a tuple of equal length, providing values for each GMST
#  Each Option is a tuple:
#    (DisplayText, Value)
#    - If you enclose DisplayText in brackets like this: _(u'[Default]'), then the patcher
#      will treat this option as the default value.
#    - If you use _(u'Custom') as the entry, the patcher will bring up a number input dialog
#  To make a tweak Enabled by Default, enclose the tuple entry for the tweak in a list, and make
#  a dictionary as the second list item with {'defaultEnabled':True}.  See the UOP Vampire face
#  fix for an example of this (in the GMST Tweaks)
GmstTweaks = [
    (_(u'Camera: Chase Distance'),_(u"Distance camera can be moved away from PC using mouse wheel."),
        ('fVanityModeWheelMax', 'fChase3rdPersonZUnitsPerSecond'),
        (_('x 1.5'),600.0*1.5, 800.0*1.5),
        (_('x 2'),  600.0*2.0, 800.0*2),
        (_('x 3'),  600.0*3.0, 800.0*3),
        (_('x 5'),  600.0*5.0, 800.0*5),
        (_('x 10'), 600.0*10,  5000),
        (_(u'Custom'),600,      800),
        ),
    (_(u'Compass: POI Recognition'),_(u"Distance at which POI markers begin to show on compass."),
        ('iMapMarkerVisibleDistance',),
        (_('x 0.05'),1000),
        (_('x 0.25'),5000),
        (_('x 0.50'),10000),
        (_('x 0.75'),15000),
        (_(u'Custom (base 1200)'),1200),
        ),
    (_(u'Essential NPC Unconsciousness'),_(u"Time which essential NPCs stay unconscious."),
        ('fEssentialDeathTime',),
        (_(u'[10 Seconds]'),10.0),
        (_(u'20 Seconds'),20.0),
        (_(u'30 Seconds'),30.0),
        (_(u'1 Minute'),60.0),
        (_(u'1 1/2 Minutes'),1.5*60.0),
        (_(u'2 Minutes'),2*60.0),
        (_(u'3 Minutes'),3*60.0),
        (_(u'5 Minutes'),5*60.0),
        (_(u'Custom (in seconds)'),10),
        ),
    (_(u'Jump Higher'),_(u"Height player can jump to."),
        ('fJumpHeightMin',),
        (_('x 1.1'),64.0*1.1),
        (_('x 1.2'),64.0*1.2),
        (_('x 1.4'),64.0*1.4),
        (_('x 1.6'),64.0*1.6),
        (_('x 1.8'),64.0*1.8),
        (_('x 2.0'),64.0*2.0),
        (_('x 3.0'),64.0*3.0),
        (_(u'Custom'),64),
        ),
    (_(u'Camera: PC Death Time'),_(u"Time after player's death before reload menu appears."),
        ('fPlayerDeathReloadTime',),
        (_(u'15 Seconds'),15.0),
        (_(u'30 Seconds'),30.0),
        (_(u'1 Minute'),60.0),
        (_(u'5 Minute'),300.0),
        (_(u'Unlimited'),9999999.0),
        (_(u'Custom'),15),
        ),
    (_(u'Cell Respawn Time'),_(u"Time before unvisited cell respawns. But longer times increase save sizes."),
        ('iHoursToRespawnCell',),
        (_(u'1 Day'),24*1),
        (_(u'[3 Days]'),24*3),
        (_(u'5 Days'),24*5),
        (_(u'10 Days'),24*10),
        (_(u'20 Days'),24*20),
        (_(u'1 Month'),24*30),
        (_(u'6 Months'),24*182),
        (_(u'1 Year'),24*365),
        (_(u'Custom (in hours)'),72),
        ),
    (_(u'Cost Multiplier: Repair'),_(u"Cost factor for repairing items."),
        ('fItemRepairCostMult',),
        ('1.0',1.0),
        ('1.25',1.25),
        ('1.5',1.5),
        ('1.75',1.75),
        ('[2.0]',2.0),
        ('2.5',2.5),
        ('3.0',3.0),
        (_(u'Custom'),2.0),
        ),
    (_(u'Combat: Max Actors'),_(u"Maximum number of actors that can actively be in combat with the player."),
        ('iNumberActorsInCombatPlayer',),
        ('[10]',10),
        ('15',15),
        ('20',20),
        ('30',30),
        ('40',40),
        ('50',50),
        ('80',80),
        (_(u'Custom'),10),
        ),
    (_(u'AI: Max Active Actors'),_(u"Maximum actors whose AI can be active. Must be higher than Combat: Max Actors"),
        ('iAINumberActorsComplexScene',),
        ('20',20),
        ('[25]',25),
        ('30',30),
        ('35',35),
        (_(u'MMM Default: 40'),40),
        ('50',50),
        ('60',60),
        ('100',100),
        (_(u'Custom'),25),
        ),
    (_(u'Companions: Max Number'),_(u"Maximum number of actors following the player"),
        ('iNumberActorsAllowedToFollowPlayer',),
        ('2',2),
        ('4',4),
        ('[6]',6),
        ('8',8),
        ('10',10),
        (_(u'Custom'),6),
        ),
    (_(u'AI: Max Dead Actors'),_(u"Maximum number of dead actors allowed before they're removed."),
        ('iRemoveExcessDeadCount', 'iRemoveExcessDeadTotalActorCount','iRemoveExcessDeadComplexTotalActorCount',
         'iRemoveExcessDeadComplexCount', 'fRemoveExcessDeadTime','fRemoveExcessComplexDeadTime'),
        (_('[x 1]'),int(15*1)  , int(20*1)  , int(20*1)  , int(3*1), 10.0*1.0, 2.5*1.0),
        (_('x 1.5'),int(15*1.5), int(20*1.5), int(20*1.5), int(3*2), 10.0*3.0, 2.5*3.0),
        (_('x 2'),  int(15*2)  , int(20*2)  , int(20*2)  , int(3*3), 10.0*5.0, 2.5*5.0),
        (_('x 2.5'),int(15*2.5), int(20*2.5), int(20*2.5), int(3*4), 10.0*7.0, 2.5*7.0),
        (_('x 3'),  int(15*3)  , int(20*3)  , int(20*3)  , int(3*5), 10.0*9.0, 2.5*9.0),
        (_('x 3.5'),int(15*3.5), int(20*3.5), int(20*3.5), int(3*6), 10.0*11.0, 2.5*11.0),
        (_('x 4'),  int(15*4)  , int(20*4)  , int(20*4)  , int(3*7), 10.0*13.0, 2.5*13.0),
        (_(u'Custom'),15,20,20,3,10,2.5),
        ),
    (_(u'Inventory Quantity Prompt'),_(u"Number of items in a stack at which point Fallout prompts for a quantity."),
        ('iInventoryAskQuantityAt',),
        ('1',1),
        ('2',2),
        ('[3]',3),
        ('4',4),
        ('10',10),
        (_(u'No Prompt'),99999),
        (_(u'Custom'),3),
        ),
    (_(u'Gore: Combat Dismember Part Chance'),_(u"The chance that body parts will be dismembered."),
        ('iCombatDismemberPartChance',),
        ('0',0),
        ('25',25),
        ('[50]',50),
        ('80',80),
        ('100',100),
        (_(u'Custom'),50),
        ),
    (_(u'Gore: Combat Explode Part Chance'),_(u"The chance that body parts will be explode."),
        ('iCombatExplodePartChance',),
        ('0',0),
        ('25',25),
        ('50',50),
        ('[75]',75),
        ('100',100),
        (_(u'Custom'),75),
        ),
    (_(u'Leveled Item Max level difference'),_(u"Maximum difference to player level for leveled items."),
        ('iLevItemLevelDifferenceMax',),
        ('1',1),
        ('5',5),
        ('[8]',8),
        ('10',10),
        ('20',20),
        (_(u'Unlimited'),9999),
        (_(u'Custom'),8),
        ),
    (_(u'Movement Base Speed'),_(u"Base Movement speed."),
        ('fMoveBaseSpeed',),
        ('[77.0]',77.0),
        ('90.0',90.0),
        (_(u'Custom'),77.0),
        ),
    (_(u'Movement Sneak Multiplier'),_(u"Movement speed is multiplied by this when the actor is sneaking."),
        ('fMoveSneakMult',),
        ('[0.57]',0.57),
        ('0.66',0.66),
        (_(u'Custom'),0.57),
        ),
    (_(u'Combat: Player Damage Multiplier in VATS'),_(u"Multiplier of damage that player receives in VATS."),
        ('fVATSPlayerDamageMult',),
        (_('0.10'),0.1),
        (_('0.25'),0.25),
        (_('0.50'),0.5),
        (_('[0.75]'),0.75),
        (_('1.00'),1.0),
        (_(u'Custom'),0.75),
        ),
    (_(u'Combat: Auto Aim Fix'),_(u"Increase Auto Aim settings to a level at which Snipers can benefit from them."),
        ('fAutoAimMaxDistance', 'fAutoAimScreenPercentage', 'fAutoAimMaxDegrees', 'fAutoAimMissRatioLow', 'fAutoAimMissRatioHigh', 'fAutoAimMaxDegreesMiss'),
        (_(u'Harder'),50000.00, -180.00, 1.10, 1.00, 1.30, 3.00),
        ),
    (_(u'PipBoy Light Keypress-Delay'),_(u"Seconds of delay until the PipBoy Light switches on."),
        ('fPlayerPipBoyLightTimer',),
        (_('0.3'),0.3),
        (_('0.4'),0.4),
        (_('0.5'),0.5),
        (_('0.6'),0.6),
        (_('0.7'),0.7),
        (_('[0.8]'),0.8),
        (_('1.0'),1.0),
        (_(u'Custom'),0.8),
        ),
    (_(u'VATS Playback Delay'),_(u"Seconds of delay after the VATS Camera finished playback."),
        ('fVATSPlaybackDelay',),
        (_('0.01'),0.01),
        (_('0.05'),0.05),
        (_('0.10'),0.1),
        (_('[0.17]'),0.17),
        (_('0.25'),0.25),
        (_(u'Custom'),0.17),
        ),
    (_(u'NPC-Death XP Threshold (Followers)'),_(u"Percentage of total damage you have to inflict in order to get XP"),
        ('iXPDeathRewardHealthThreshold',),
        (_('0%'),0),
        (_('25%'),25),
        (_('[40%]'),40),
        (_('50%'),50),
        (_('75%'),75),
        (_(u'Custom'),40),
        ),
    (_(u'Hacking: Maximum Number of words'),_(u"The maximum number of words appearing in the terminal hacking mini-game."),
        ('iHackingMaxWords',),
        (_('1'),1),
        (_('4'),4),
        (_('8'),8),
        (_('12'),12),
        (_('16'),16),
        (_('[20]'),20),
        (_(u'Custom'),20),
        ),
    (_(u'Shell Camera Distance'),_(u"Maximum distance at which gun arisings (shell case, particle, decal) show from camera."),
        ('fGunParticleCameraDistance', 'fGunShellCameraDistance', 'fGunDecalCameraDistance'),
        (_('x 1.5'),2048.0*1.5, 512.0*1.5, 2048.0*1.5),
        (_('x 2'),  2048.0*2.0, 512.0*2.0, 2048.0*2.0),
        (_('x 3'),  2048.0*3.0, 512.0*3.0, 2048.0*3.0),
        (_('x 4'),  2048.0*4.0, 512.0*4.0, 2048.0*4.0),
        (_('x 5'),  2048.0*5.0, 512.0*5.0, 2048.0*5.0),
        (_(u'Custom'),2048, 512, 2048),
        ),
    (_(u'Shell Litter Time'),_(u"Time before shell cases fade away from cells."),
        ('fGunShellLifetime',),
        (_(u'[10 Seconds]'),10),
        (_(u'20 Seconds'),20),
        (_(u'30 Seconds'),30),
        (_(u'1 Minute'),60),
        (_(u'3 Minutes'),60*3),
        (_(u'5 Minutes'),60*5),
        (_(u'Custom (in seconds)'),10),
        ),
    (_(u'Shell Litter Count'),_(u"Maximum number of debris (shell case, etc) allowed in cell."),
        ('iDebrisMaxCount',),
        (_('[50]'),50),
        (_('100'),100),
        (_('500'),500),
        (_('1000'),1000),
        (_('3000'),3000),
        (_(u'Custom'),50),
        ),
    (_(u'Terminal Speed Adjustment'),_(u"The display speed at the time of terminal hacking."),
        ('iHackingDumpRate','iHackingInputRate','iHackingOutputRate','iHackingFlashOffDuration','iHackingFlashOnDuration','iComputersDisplayRateMenus','iComputersDisplayRateNotes'),
        (_('x 2'),1000,40,134,250,375,300,300),
        (_('x 4'),2000,80,268,125,188,600,600),
        (_('[x 6]'),3000,120,402,83,126,900,900),
        (_(u'Custom'),3000,120,402,83,126,900,900),
        ),
    (_(u'Drag: Max Moveable Weight'),_(u"Maximum weight to be able move things with the drag key."),
        ('fMoveWeightMax',),
        (_('1500'),1500.0),
        (_(u'[Default (150)]'),150),
        (_(u'Custom'),150),
        ),
    ]
#-------------------------------------------------------------------------------
# ListsMerger
#-------------------------------------------------------------------------------
listTypes = ('LVLC','LVLI','LVLN')
#-------------------------------------------------------------------------------
# NamesPatcher
#-------------------------------------------------------------------------------
namesTypes = set((
    'ACTI', 'ALCH', 'AMMO', 'ARMO', 'BOOK', 'CLAS', 'CONT', 'CREA', 'DOOR', 'EYES',
    'FACT', 'HAIR', 'INGR', 'KEYM', 'LIGH', 'MISC', 'NOTE', 'NPC_', 'RACE', 'SPEL',
    'TACT', 'TERM', 'WEAP',
        ))
#-------------------------------------------------------------------------------
# ItemPrices Patcher
#-------------------------------------------------------------------------------
pricesTypes = {'ALCH':{},'AMMO':{},'ARMO':{},'ARMA':{},'BOOK':{},'INGR':{},'KEYM':{},'LIGH':{},'MISC':{},'WEAP':{}}

#-------------------------------------------------------------------------------
# StatsImporter
#-------------------------------------------------------------------------------
statsTypes = {
        'ALCH':('eid', 'weight', 'value'),
        'AMMO':('eid', 'value', 'speed', 'clipRounds'),
        'ARMA':('eid', 'weight', 'value', 'health', 'ar'),
        'ARMO':('eid', 'weight', 'value', 'health', 'ar'),
        'BOOK':('eid', 'weight', 'value'),
        'INGR':('eid', 'weight', 'value'),
        'KEYM':('eid', 'weight', 'value'),
        'LIGH':('eid', 'weight', 'value', 'duration'),
        'MISC':('eid', 'weight', 'value'),
        'WEAP':('eid', 'weight', 'value', 'health', 'damage','clipsize',
                'animationMultiplier','reach','ammoUse','minSpread','spread','sightFov','baseVatsToHitChance','projectileCount',
                'minRange','maxRange','animationAttackMultiplier','fireRate','overrideActionPoint','rumbleLeftMotorStrength',
                'rumbleRightMotorStrength','rumbleDuration','overrideDamageToWeaponMult','attackShotsPerSec',
                'reloadTime','jamTime','aimArc','rambleWavelangth','limbDmgMult','sightUsage',
                'semiAutomaticFireDelayMin','semiAutomaticFireDelayMax',
                'criticalDamage','criticalMultiplier'),
        }
statsHeaders = (
        #--Alch
        (u'ALCH',
            (u'"' + '","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
            _(u'Editor Id'),_(u'Weight'),_(u'Value'))) + u'"\n')),
        #Ammo
        (u'AMMO',
            (u'"' + u'","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
            _(u'Editor Id'),_(u'Weight'),_(u'Value'),_(u'Speed'),_(u'Clip Rounds'),_(u'Proj/Shot'))) + u'"\n')),
        #--Armor
        (u'ARMO',
            (u'"' + u'","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
            _(u'Editor Id'),_(u'Weight'),_(u'Value'),_(u'Health'),_(u'AR'),_(u'DT'))) + u'"\n')),
        #--Armor Addon
        (u'ARMA',
            (u'"' + u'","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
            _(u'Editor Id'),_(u'Weight'),_(u'Value'),_(u'Health'),_(u'AR'))) + '"\n')),
        #Books
        (u'BOOK',
            (u'"' + u'","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
            _(u'Editor Id'),_(u'Weight'),_(u'Value'))) + u'"\n')),
        #Ingredients
        (u'INGR',
            (u'"' + u'","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
           _(u'Editor Id'),_(u'Weight'),_(u'Value'))) + u'"\n')),
        #--Keys
        (u'KEYM',
            (u'"' + u'","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
            _(u'Editor Id'),_(u'Weight'),_(u'Value'))) + u'"\n')),
        #Lights
        (u'LIGH',
            (u'"' + u'","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
            _(u'Editor Id'),_(u'Weight'),_(u'Value'),_(u'Duration'))) + u'"\n')),
        #--Misc
        (u'MISC',
            (u'"' + u'","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
            _(u'Editor Id'),_(u'Weight'),_(u'Value'))) + u'"\n')),
        #--Weapons
        (u'WEAP',
            (u'"' + u'","'.join((_(u'Type'),_(u'Mod Name'),_(u'ObjectIndex'),
            _(u'Editor Id'),_(u'Weight'),_(u'Value'),_(u'Health'),_(u'Damage'),
            _(u'Clip Size'),_(u'Animation Multiplier'), _(u'Reach'), _(u'Ammo Use'),
            _(u'Min Spread'), _(u'Spread'), _(u'Sight Fov'),
            _(u'Base VATS To-Hit Chance'), _(u'Projectile Count'),_(u'Min Range'),
            _(u'Max Range'), _(u'Animation Attack Multiplier'), _(u'Fire Rate'),
            _(u'Override - Action Point'), _(u'Rumble - Left Motor Strength'),
            _(u'rRmble - Right Motor Strength'), _(u'Rumble - Duration'),
            _(u'Override - Damage To Weapon Mult'), _(u'Attack Shots/Sec'),
            _(u'Reload Time'), _(u'Jam Time'), _(u'Aim Arc'), _(u'Ramble - Wavelangth'),
            _(u'Limb Dmg Mult'), _(u'Sight Usage'),_(u'Semi-Automatic Fire Delay Min'),
            _(u'Semi-Automatic Fire Delay Max'),_(u'Critical Damage'),
            _(u'Crit % Mult'))) + '"\n')),
        )

#-------------------------------------------------------------------------------
# SoundPatcher
#-------------------------------------------------------------------------------
# Needs longs in SoundPatcher
soundsLongsTypes = set((
    'ACTI', 'ADDN', 'ALCH', 'ASPC', 'CONT', 'CREA', 'DOOR', 'EXPL', 'IPCT', 'LIGH',
    'MGEF', 'PROJ', 'SOUN', 'TACT', 'WATR', 'WEAP', 'WTHR',
))
soundsTypes = {
    "ACTI": ('soundLooping','soundActivation',),
    "ADDN": ('ambientSound',),
    "ALCH": ('dropSound','pickupSound','soundConsume',),
    "ASPC": ('soundLooping','useSoundFromRegion',),
    "CONT": ('soundOpen','soundClose',),
    "CREA": ('footWeight','inheritsSoundsFrom','sounds'),
    "DOOR": ('soundOpen','soundClose','soundLoop',),
    "EXPL": ('soundLevel','sound1','sound2',),
    "IPCT": ('soundLevel','sound1','sound2',),
    "LIGH": ('sound',),
    "MGEF": ('castingSound','boltSound','hitSound','areaSound',),
    "PROJ": ('sound','soundCountDown','soundDisable','soundLevel',),
#    "REGN": ('entries.sounds',),
    "SOUN": ('soundFile','minDist','maxDist','freqAdj','flags','staticAtten',
             'stopTime','startTime','point0','point1','point2','point3',
             'point4','reverb','priority','xLoc','yLoc',),
    "TACT": ('sound',),
    "WATR": ('sound',),
    "WEAP": ('pickupSound','dropSound','soundGunShot3D','soundGunShot2D',
             'soundGunShot3DLooping','soundMeleeSwingGunNoAmmo','soundBlock','idleSound',
             'equipSound','unequipSound','soundLevel',),
    "WTHR": ('sounds',),
}
soundsFidTypes = {
}

#-------------------------------------------------------------------------------
# CellImporter
#-------------------------------------------------------------------------------
cellAutoKeys = (
    u'C.Acoustic',u'C.Climate',u'C.Encounter',u'C.ImageSpace',u'C.Light',
    u'C.Music',u'C.Name',u'C.Owner',u'C.RecordFlags',u'C.Water',)#,u'C.Maps')
cellRecAttrs = {
            u'C.Acoustic': ('acousticSpace',),
            u'C.Climate': ('climate',),
            u'C.Encounter': ('encounterZone',),
            u'C.ImageSpace': ('imageSpace',),
            u'C.Light': ('ambientRed','ambientGreen','ambientBlue','unused1',
                        'directionalRed','directionalGreen','directionalBlue','unused2',
                        'fogRed','fogGreen','fogBlue','unused3',
                        'fogNear','fogFar','directionalXY','directionalZ',
                        'directionalFade','fogClip','fogPower',
                        'lightTemplate','lightInheritFlags'),
            u'C.Music': ('music',),
            u'C.Name': ('full',),
            u'C.Owner': ('ownership',),
            u'C.RecordFlags': ('flags1',), # Yes seems funky but thats the way it is
            u'C.Water': ('water','waterHeight','waterNoiseTexture',),
            }
cellRecFlags = {
            u'C.Acoustic': '',
            u'C.Climate': 'behaveLikeExterior',
            u'C.Encounter': '',
            u'C.ImageSpace': '',
            u'C.Light': '',
            u'C.Music': '',
            u'C.Name': '',
            u'C.Owner': 'publicPlace',
            u'C.RecordFlags': '',
            u'C.Water': 'hasWater',
            }
#-------------------------------------------------------------------------------
# GraphicsPatcher
#-------------------------------------------------------------------------------
graphicsLongsTypes = set((
    'ACTI', 'ALCH', 'AMMO', 'ARMA', 'ARMO', 'BOOK', 'CLAS', 'CREA', 'DOOR', 'EFSH',
    'EXPL', 'FURN', 'GRAS', 'INGR', 'KEYM', 'LIGH', 'LSCR', 'LTEX', 'MISC', 'NPC_',
    'STAT', 'TREE', 'WEAP', 'MGEF',
    ))
graphicsTypes = {
    "ACTI": ('model',),
    "ALCH": ('iconPath','model',),
    "AMMO": ('iconPath','model',),
    "ARMA": ('maleBody','maleWorld','maleIconPath','femaleBody','femaleWorld','femaleIconPath',),
    "ARMO": ('maleBody','maleWorld','maleIconPath','femaleBody','femaleWorld','femaleIconPath',
	         'objectEffect',),
    "BOOK": ('iconPath','model',),
    "CLAS": ('iconPath',),
    "CREA": ('bodyParts','nift_p','effect',),
    "DOOR": ('model',),
    "EFSH": ('flags','unused1','memSBlend',
    'memBlendOp','memZFunc','fillRed','fillGreen','fillBlue',
    'unused2','fillAIn','fillAFull','fillAOut','fillAPRatio',
    'fillAAmp','fillAFreq','fillAnimSpdU','fillAnimSpdV','edgeOff',
    'edgeRed','edgeGreen','edgeBlue','unused3','edgeAIn',
    'edgeAFull','edgeAOut','edgeAPRatio','edgeAAmp','edgeAFreq',
    'fillAFRatio','edgeAFRatio','memDBlend','partSBlend',
    'partBlendOp','partZFunc','partDBlend','partBUp',
    'partBFull','partBDown','partBFRatio',
    'partBPRatio','partLTime','partLDelta',
    'partNSpd','partNAcc','partVel1','partVel2',
    'partVel3','partAcc1','partAcc2','partAcc3',
    'partKey1','partKey2','partKey1Time',
    'partKey2Time','key1Red','key1Green',
    'key1Blue','unused4','key2Red','key2Green',
    'key2Blue','unused5','key3Red','key3Green',
    'key3Blue','unused6','key1A','key2A',
    'key3A','key1Time','key2Time','key3Time',
    'partNSpdDelta','partRot',
    'partRotDelta','partRotSpeed',
    'partRotSpeedDelta','addonModels',
    'holesStartTime','holesEndTime',
    'holesStartVal','holesEndVal',
    'edgeWidth','edgeRed','edgeGreen',
    'edgeBlue','unused7','explosionWindSpeed',
    'textureCountU','textureCountV',
    'addonModelsFadeInTime','addonModelsFadeOutTime',
    'addonModelsScaleStart','addonModelsScaleEnd',
    'addonModelsScaleInTime','addonModelsScaleOutTime',),
    "EXPL": ('model','objectEffect',),
    "FURN": ('model',),
    "GRAS": ('model',),
    "INGR": ('iconPath','model',),
    "KEYM": ('iconPath','model',),
    "LIGH": ('iconPath','model',),
    "LSCR": ('iconPath',),
    "LTEX": ('iconPath',),
    "MGEF": ('iconPath','model',),
    "MISC": ('iconPath','model',),
    "NPC_": ('unarmedAttackEffect',),
    "STAT": ('model',),
    "TREE": ('iconPath','model',),
    "WEAP": ('iconPath','model','enchantment',),
}
graphicsFidTypes = {
    "MGEF": ('effectShader','light','objectDisplayShader','cefEnchantment',)
}
graphicsModelAttrs = ('model','shellCasingModel','scopeModel','worldModel')
#-------------------------------------------------------------------------------
# Inventory Patcher
#-------------------------------------------------------------------------------
inventoryTypes = ('CREA','NPC_','CONT',)
#-------------------------------------------------------------------------------
# Mod Record Elements ----------------------------------------------------------
#-------------------------------------------------------------------------------
FID = 'FID' #--Used by MelStruct classes to indicate fid elements.

# Record type to name dictionary
record_type_name = {
    'ALCH':_(u'Potions'),
    'AMMO':_(u'Ammo'),
    'ARMA':_(u'Armature'),
    'ARMO':_(u'Armors'),
    'BOOK':_(u'Books'),
    'INGR':_(u'Ingredients'),
    'KEYM':_(u'Keys'),
    'LIGH':_(u'Lights'),
    'MISC':_(u'Misc'),
    'WEAP':_(u'Weapons'),
}

# xEdit menu string and key for expert setting
xEdit_expert = (_(u'Fo3Edit Expert'), 'fo3View.iKnowWhatImDoing')
