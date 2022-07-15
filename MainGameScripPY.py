import pyautogui
import requests
import json
import time
from mine import *

""" 
CODE BY YAROSLAV BOGDANOV 
yaroslav.bogdanov.2005@mail.ru
LHTG Group ( Lo-fi hip-hop tip-top girl Group )
...
"""

# Start positions
lobbyPosition = (-90, 0, 224)
parkourStart_position = (14, 15, -105)
shootingStart_position = (-326, 1, -27)
labirintStart_position = (-53, 0, 33)
arenaStart_position = (-178, 1, 88)

# Parkour command blocks positions
blindnessPos = (13, 0, -92)
unblindnessPos = (13, 0, -90)

# Labirint command blocks positions
slownessPos = (-53, 0, 38)
unslownessPos = (-53, 0, 40)

# Arena command blocks
firstDoor = (-155, 0, 66)
realaxTest = (-147, 0, 66)
relaxActive = (-136, 0, 65)
unrelaxActive = (-134, 0, 65)

# Main flags
flagSpawnMain = True
flagParkour = False
flagLabirint = False
flagShooting = False
flagArena = False

# Flags of locating
LobbyFlag = True
ParkurFlag = True
LabirintFlag = True

# Connection to MC
mc = Minecraft()
mc.postToChat("Biofeedback mini-games started")

# Main script cycle
while True:
    # Gets player positon in MC
    playerPosition = (mc.player.getTilePos().x, mc.player.getTilePos().y, mc.player.getTilePos().z)

    # Gets information on the percentage of concentration
    data = requests.get("http://127.0.0.1:2336/concentration")
    jsonData = data.json()

    # Main game flags
    if playerPosition == lobbyPosition and not flagSpawnMain:
        mc.postToChat("Lobby")
        flagSpawnMain = True
        flagParkour = False
        flagLabirint = False
        flagShooting = False
        flagArena = False
    elif playerPosition == parkourStart_position and not flagParkour:
        mc.postToChat("Parkour")
        flagSpawnMain = False
        flagParkour = True
        flagLabirint = False
        flagShooting = False
        flagArena = False
    elif playerPosition == labirintStart_position and not flagLabirint:
        mc.postToChat("Labirint")
        flagSpawnMain = False
        flagParkour = False
        flagLabirint = True
        flagShooting = False
        flagArena = False
    elif playerPosition == shootingStart_position and not flagShooting:
        mc.postToChat("Shooting range")
        flagSpawnMain = False
        flagParkour = False
        flagLabirint = False
        flagShooting = True
        flagArena = False
    elif playerPosition == arenaStart_position and not flagArena:
        mc.postToChat("Arena")
        flagSpawnMain = False
        flagParkour = False
        flagLabirint = False
        flagShooting = False
        flagArena = True

    if flagSpawnMain:
        pass

    # Parkour script
    elif flagParkour:
        if jsonData['concentration'] > 70:
            x, y, z = blindnessPos
            mc.setBlock(x, y, z, block.REDSTONE_BLOCK.id)
            x, y, z = unblindnessPos
            mc.setBlock(x, y, z, block.AIR.id)
        elif jsonData['concentration'] < 70:
            x, y, z = unblindnessPos
            mc.setBlock(x, y, z, block.REDSTONE_BLOCK.id)
            x, y, z = blindnessPos
            mc.setBlock(x, y, z, block.AIR.id)

    # Labirbirint script
    elif flagLabirint:
        if jsonData['concentration'] > 80:
            x, y, z = slownessPos
            mc.setBlock(x, y, z, block.REDSTONE_BLOCK.id)
            x, y, z = unslownessPos
            mc.setBlock(x, y, z, block.AIR.id)
        elif jsonData['concentration'] < 80:
            x, y, z = unslownessPos
            mc.setBlock(x, y, z, block.REDSTONE_BLOCK.id)
            x, y, z = slownessPos
            mc.setBlock(x, y, z, block.AIR.id)

    # Shooting range script
    elif flagShooting:
        if jsonData['concentration'] > 80:
            pyautogui.mouseDown(button='right')
        else:
            pyautogui.mouseUp(button='right')

    # Arena script
    elif flagArena:

        # Arena flags
        flagFirstDoor = True
        flagSecondDoor = False
        flagMainArenaGame = False

        # Arena coords
        firstDoorCoord = (-178, 1, 83)
        secondDoorCoord = (-178, 1, 74)
        mainArenaCoord = (-178, 1, 59)

        # Arena flags control
        if playerPosition == firstDoorCoord:
            flagFirstDoor = True
            flagSecondDoor = False
            flagMainArenaGame = False
        elif playerPosition == secondDoorCoord:
            flagFirstDoor = False
            flagSecondDoor = True
            flagMainArenaGame = False
        elif playerPosition == mainArenaCoord:
            flagFirstDoor = False
            flagSecondDoor = False
            flagMainArenaGame = True

        # Arena scripts
        if flagFirstDoor:
            if jsonData['concentration'] >= 80:
                x, y, z = firstDoor
                mc.setBlock(x, y, z, block.REDSTONE_BLOCK.id)
        elif flagSecondDoor:
            if jsonData['concentration'] >= 100:
                x, y, z = realaxTest
                mc.setBlock(x, y, z, block.REDSTONE_BLOCK.id)
        elif flagMainArenaGame:
            if jsonData['concentration'] >= 100:
                x, y, z = relaxActive
                mc.setBlock(x, y, z, block.REDSTONE_BLOCK.id)
            else:
                x, y, z = unrelaxActive
                mc.setBlock(x, y, z, block.REDSTONE_BLOCK.id)