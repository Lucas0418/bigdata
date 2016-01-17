#!/usr/bin/python
#Filename: kmeans.py
#Usage: ./kemans.py sourcefilename k
#source data may be some coordinates in this format (x,y).

import sys

def readSourceFile(sourceFileName):
    '''Function to import source data from source file.'''
    f = file(sourceFileName)
    while True:
        line = f.readline()
        line = line.strip('\n')
        if len(line) == 0:
            break
        curList = []
        for a in line.rsplit(','):
            curList.append(float(a))
        sourceData.append(curList)
    f.close()

def kmeans(sourceList,sourceCenterList):
    '''kmeans the data in source list.'''
    global kmeanstimes
    kmeanstimes += 1
    centerList = sourceCenterList[:]
    groups = []
    for i in range(0,userK):
        groups.append([])
    for i in range(0,total):
        dx = sourceList[i][0]
        dy = sourceList[i][1]
        for j in range(0,userK):
            sx = centerList[j][0]
            sy = centerList[j][1]
            if j == 0:
                minumumDistanceSquare = (sy-dy)**2+(sx-dx)**2
                minumum = 0
            else:
                distanceSquare = (sy-dy)**2+(sx-dx)**2
                if distanceSquare < minumumDistanceSquare:
                    distanceSquare = minumumDistanceSquare
                    minumum = j
        groups[minumum].append(i)
    for j in range (0,len(groups)):
        if len(groups[j]) == 0:
            for i in range (0,len(groups)):
                print centerList[i]
                print 'has %d dots:'%(len(groups[i]))
                print groups[i]
            print 'kmeans times :%d'%(kmeanstimes)
            sys.exit(0)
    newCenterList = modCenter(sourceList,groups)
    for i in range(0,userK):
        if (newCenterList[i][0]-centerList[i][0])**2 + (newCenterList[i][1]-centerList[i][1])**2 > 1:
            kmeans(sourceList,newCenterList)
            sys.exit()
    for i in range (0,len(groups)):
        print newCenterList[i]
        print 'has %d dots:'%(len(groups[i]))
        print groups[i]
    print 'kmeans times :%d'%(kmeanstimes)

def modCenter(sourceList,groups):
    centerList = []
    for i in range(0,len(groups)):
        sumx = 0
        sumy = 0
        for j in range(0,len(groups[i])):
            sumx += sourceList[groups[i][j]][0]
            sumy += sourceList[groups[i][j]][1]
        centerList.append([sumx/len(groups[i]),sumy/len(groups[i])])
    return centerList

def initCenter(sourceList):
    '''init number k center.'''
    centerList = []
    for i in range(0,userK):
        centerList.append(sourceList[total*(i+1)/userK-total/2/userK])
    centerList.sort()
    return centerList
#Script starts from here

if len(sys.argv) < 2:
    print 'No source file specified.'
    sys.exit()

sourceData = []
centerData = []
readSourceFile(sys.argv[1])
total = len(sourceData)
userK = int(sys.argv[2])
count = [0]*userK
centerData = initCenter(sourceData)
global kmeanstimes
kmeanstimes = 0
kmeans(sourceData,centerData)
