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
        if exitList[direction] == '?':
            unexplored.append(direction)
    if len(unexplored) > 0:
        return unexplored

mapGraph = {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}

roomInfo = viewRoom()
time.sleep(1)
roomExits = roomInfo['exits']
# exits = findExits(roomExits)
# roomInfo = viewRoom()
# firstMove = wiseExplore('0', 's')
# print(firstMove['room_id'])
# print(roomInfo['exits'])

print(roomExits)
# exploreStack = Stack()
# exploreStack.push(roomInfo['room_id'])

# print(exploreStack.stack)