#!/usr/bin/env python3.8
import os
import sys
import time

#För varje sak i mappen
#   Om saken är en fil och börjar med "HorribleSubs" grejen
#       Extrahera namn och säsong
#       Om mapp med namnet inte finns
#           Skapa mapp
#       Om mapp för säsongen inte finns
#           Skapa mapp
#       Flytta filen till slutgiltiga mappen

creatorTag = "[HorribleSubs]"
sourceFolder = "Uncategorized"
destinationFolder = "Anime/Serier"


files = os.listdir(sourceFolder)
for file in files:
    if os.path.isfile(f"{sourceFolder}/{file}") and file[0:14] == creatorTag:
        print("Sorting " + file)
        originalLength = len(file)
        currentLength = originalLength
        qualityIndex = 0
        episodeDashIndex = 0
        isSeasoned = False

        #Look for quality from the back
        currIndex = originalLength - 1 #Last index
        while currIndex >= 0:
            if file[currIndex] == '[':
                qualityIndex = currIndex
                break
            currIndex = currIndex - 1

        #Look for episode dash from the quality index
        while currIndex >= 0:
            if file[currIndex] == '-':
                episodeDashIndex = currIndex
                break
            currIndex = currIndex - 1
        
        titleLength = episodeDashIndex - 2 - len(creatorTag)
        animeName = file[15:titleLength + 15]
        seasonNum = -1
        if animeName[titleLength - 2] == 'S':
            seasonNum = animeName[-1]
            if int(seasonNum) >= 1:
                season = True
        else:
            seasonNum = 1
        fileLocation = f"{os.getcwd()}/{sourceFolder}/{file}"
        os.chdir(os.getcwd() + '/' + destinationFolder)

        animePath = os.getcwd() + '/' + animeName
        try:
            os.mkdir(animePath)
        except FileExistsError:
            print("Title folder already created")
        os.chdir(animePath)

        seasonPath = os.getcwd() + '/' + "Season " + f"{seasonNum}"
        try:
            os.mkdir(seasonPath)
            print(os.getcwd())
        except FileExistsError:
            print("Season folder already created")
        os.chdir(seasonPath)
        os.replace(fileLocation, os.getcwd() + '/' + file)
        
