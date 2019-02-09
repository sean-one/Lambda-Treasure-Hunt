import requests
import json
import time
import math
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


roomInfo = requests.get(f'{urlRoot}init/', headers=token).json()
time.sleep(roomInfo['cooldown'])

mapGraph = {0: {'n': '?', 's': '?', 'w': '?', 'e': '?', 'c': '?'}}
inversalKey = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
stroll = []

exploreStack = Stack()
exploreStack.push(roomInfo['room_id'])

print(exploreStack.stack)
while exploreStack.size() < 5:
    print(f'before {mapGraph}')
    exitOptions = mapGraph[exploreStack.stack[-1]]
    print(f'after {mapGraph}')
    checkExits = findExits(exitOptions)
    if checkExits is not None:
        firstExit = checkExits[0]
        enterFrom = exploreStack.stack[-1]
        stroll.append(firstExit)
        newRoom = requests.post(f'{urlRoot}move/', headers=tokenContent, json={ 'direction' : firstExit}).json()
        time.sleep(newRoom['cooldown'])
        print(newRoom)

        mapGraph[enterFrom][firstExit] = roomInfo['room_id']

        exitDict = {}
        if newRoom['room_id'] in exploreStack.stack:
            mapGraph[newRoom['room_id']][inversalKey[firstExit]] = enterFrom
        else:
            for exit in newRoom['exits']:
                if exit == 'c':
                    exitDict[exit] = newRoom['coordinates']
                else:
                    exitDict[exit] = '?'
            exitDict[inversalKey[firstExit]] = enterFrom
            mapGraph[newRoom['room_id']] = exitDict
        exploreStack.push(newRoom['room_id'])
        print(exploreStack.stack)
    
    else:
        finishedRoom = exploreStack.pop()
        if exploreStack.size() > 0:
            lastRoom = exploreStack.stack[-1]
            for route, room in mapGraph[lastRoom].items():
                if room == finishedRoom:
                    stroll.append(inversalKey[route])
                    roomInfo = requests.post(f'{urlRoot}move/', headers=tokenContent, json={'direction': inversalKey[route]}).json()
                    time.sleep(roomInfo['cooldown'])
                    # roomInfo = blindExplore(inversalKey[route])
                    break
print(mapGraph)

# roomInfo = viewRoom()
# firstMove = wiseExplore('0', 's')
# print(firstMove['room_id'])
# print(roomInfo['exits'])
