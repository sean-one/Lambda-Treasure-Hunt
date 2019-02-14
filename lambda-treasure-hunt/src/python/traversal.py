import requests
import json
import time
import math
from variables import token, tokenContent
from stack import Stack

urlRoot = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/'

def findExits(exits):
    """
    find the exits in the room and mark them with a '?'
    returns an unexplored list of exits
    """
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

mapGraph = {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}
locations = {}
inversalKey = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
stroll = []

# gather information on the room
locations[roomInfo['room_id']] = {
    'room_id' : roomInfo['room_id'],
    'title' : roomInfo['title'],
    'description' : roomInfo['description'],
    'coordinates' : [int(roomInfo['coordinates'][1:3]), int(roomInfo['coordinates'][4:6])],
    'elevation' : roomInfo['elevation'],
    'terrain' : roomInfo['terrain'],
    'items' : roomInfo['items'],
    'exits' : roomInfo['exits'],
    'errors' : roomInfo['errors'],
    'messages' : roomInfo['messages']
}


# start the room stack to track path
exploreStack = Stack()
exploreStack.push(roomInfo['room_id'])

while exploreStack.size() > 0:
    exitOptions = mapGraph[exploreStack.stack[-1]]
    checkExits = findExits(exitOptions)
    if checkExits is not None:
        # get the first unknown exit
        firstExit = checkExits[0]
        enterFrom = exploreStack.stack[-1]

        # add to walking path
        stroll.append(firstExit)

        # move to the next room
        roomInfo = requests.post(f'{urlRoot}move/', headers=tokenContent, json={ 'direction' : firstExit}).json()
        
        # stall for the cooldown period
        time.sleep(roomInfo['cooldown'])

        # gather needed room information
        locations[roomInfo['room_id']] = {
            'room_id' : roomInfo['room_id'],
            'title' : roomInfo['title'],
            'description' : roomInfo['description'],
            'coordinates' : [int(roomInfo['coordinates'][1:3]), int(roomInfo['coordinates'][4:6])],
            'elevation' : roomInfo['elevation'],
            'terrain' : roomInfo['terrain'],
            'items' : roomInfo['items'],
            'exits' : roomInfo['exits'],
            'errors' : roomInfo['errors'],
            'messages' : roomInfo['messages']
        }

        mapGraph[enterFrom][firstExit] = roomInfo['room_id']

        exitDict = {}
        if roomInfo['room_id'] in exploreStack.stack:
            mapGraph[roomInfo['room_id']][inversalKey[firstExit]] = enterFrom
        else:
            for exit in roomInfo['exits']:
                if exit == 'c':
                    exitDict[exit] = roomInfo['coordinates']
                else:
                    exitDict[exit] = '?'
            exitDict[inversalKey[firstExit]] = enterFrom
            mapGraph[roomInfo['room_id']] = exitDict
        exploreStack.push(roomInfo['room_id'])
    
    else:
        finishedRoom = exploreStack.pop()
        if exploreStack.size() > 0:
            lastRoom = exploreStack.stack[-1]
            for route, room in mapGraph[lastRoom].items():
                if room == finishedRoom:
                    stroll.append(inversalKey[route])
                    roomInfo = requests.post(f'{urlRoot}move/', headers=tokenContent, json={'direction': inversalKey[route]}).json()
                    time.sleep(roomInfo['cooldown'])
                    locations[roomInfo['room_id']] = {
                        'room_id' : roomInfo['room_id'],
                        'title' : roomInfo['title'],
                        'description' : roomInfo['description'],
                        'coordinates' : [int(roomInfo['coordinates'][1:3]), int(roomInfo['coordinates'][4:6])],
                        'elevation' : roomInfo['elevation'],
                        'terrain' : roomInfo['terrain'],
                        'items' : roomInfo['items'],
                        'exits' : roomInfo['exits'],
                        'errors' : roomInfo['errors'],
                        'messages' : roomInfo['messages']
                    }
                    break

with open('mapGraph.json', 'w') as f:
    json.dump(mapGraph, f)

with open('locations.json', 'w') as f2:
    json.dump(locations, f2)
