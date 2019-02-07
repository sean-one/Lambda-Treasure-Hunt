import requests
import json
import time
from variables import token, tokenContent
from stack import Stack

urlRoot = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/'

def playerStatus():
    resp = requests.post(f'{urlRoot}status/', headers=tokenContent)
    playerInfo = json.loads(resp.text)
    return playerInfo

def viewRoom():
    resp = requests.get(f'{urlRoot}init/', headers=token)
    roomInfo = json.loads(resp.text)
    return roomInfo

def wiseExplore(nextRoom, direction):
    move = {
        'direction': direction,
        'next_room_id': nextRoom
    }
    resp = requests.post(f'{urlRoot}move/', headers=tokenContent, json=move)
    newRoom = json.loads(resp.text)
    return newRoom

def blindExplore(direction):
    move = {
        'direction': direction
    }
    resp = requests.post(f'{urlRoot}move/', headers=tokenContent, json=move)
    newRoom = json.loads(resp.text)
    return newRoom

def findExits(exits):
    unexplored = []
    for direction in exits:
        if exits[direction] == '?':
            unexplored.append(direction)
        else:
            pass
    if len(unexplored) > 0:
        return unexplored
    else:
        return None

roomInfo = viewRoom()
time.sleep(roomInfo['cooldown'])

mapGraph = {0: [(60, 60), {'n': '?', 's': '?', 'w': '?', 'e': '?'}]}
inversalKey = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
stroll = []

exploreStack = Stack()
exploreStack.push(roomInfo['room_id'])

print(exploreStack.stack)

while exploreStack.size() < 5:
    exitOptions = mapGraph[roomInfo['room_id']][1]
    checkExits = findExits(exitOptions)
    if checkExits is not None:
        firstExit = checkExits[0]
        enterFrom = exploreStack.stack[-1]
        stroll.append(firstExit)
        newRoom = blindExplore(firstExit)
        print(newRoom)
        time.sleep(roomInfo['cooldown'])

        mapGraph[enterFrom][1][firstExit] = roomInfo['room_id']

        exitDict = {}
        if newRoom['room_id'] in exploreStack.stack:
            mapGraph[newRoom['room_id']][1][inversalKey[firstExit]] = enterFrom
        else:
            for exit in newRoom['exits']:
                exitDict[exit] = '?'
            exitDict[inversalKey[firstExit]] = enterFrom
            mapGraph[newRoom['room_id']][0] = newRoom['coordinates']
            mapGraph[newRoom['room_id']][1] = exitDict
        exploreStack.push(newRoom['room_id'])
    
    else:
        finishedRoom = exploreStack.pop()
        if exploreStack.size() > 0:
            lastRoom = exploreStack.stack[-1]
            for route, room in mapGraph[lastRoom][1].items():
                if room == finishedRoom:
                    stroll.append(inversalKey[route])
                    roomInfo = wiseExplore(room, inversalKey[route])
                    time.sleep(roomInfo['cooldown'])
                    break
print(mapGraph)

# roomInfo = viewRoom()
# firstMove = wiseExplore('0', 's')
# print(firstMove['room_id'])
# print(roomInfo['exits'])
