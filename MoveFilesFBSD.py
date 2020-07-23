#!/usr/bin/env python3.8
import os
import sys
import time


files = os.listdir("Uncategorized")
cwd = os.getcwd()
for f in files:
    torrent = f
    ani = f
    if os.path.isfile(f"Uncategorized/{ani}"):
        if ani[0:14] == "[HorribleSubs]":
            aniLength = len(ani)
            epDash = 0
            qBrac = 0
            i = aniLength - 1
            while i >= 0:
                if ani[i] == '[':
                    qBrac = i
                    break
                i = i - 1

            i = qBrac
            while i >= 0:
                if ani[i] == '-':
                    epDash = i
                    break
                i = i - 1

            aniLength = epDash - 2 - 15 + 1
            ani = ani[15:aniLength + 15]
            season = False
            seasonNum = "-1"
            aniLength = len(ani)
            if ani[aniLength - 2] == 'S':
                seasonNum = ani[-1]
                if int(seasonNum) > 1:
                    season = True
            downPath = f"/Uncategorized/{torrent}"
            aniPath = ""
            endPath = ""
            if season:
                anic = ani[0:aniLength - 3]
                aniPath = f"/Anime/Serier/{anic}"
                endPath = aniPath + f"/Season {seasonNum}"
                try:
                    os.mkdir(cwd + aniPath)
                except:
                    print("Error")
                    pass
                try:
                    os.mkdir(cwd + endPath)
                except:
                    print("Error")
                    pass
            else:
                aniPath = f"/Anime/Serier/{ani}"
                endPath = aniPath + "/Season 1"
                try:
                    os.mkdir(cwd + aniPath)
                except:
                    print("Error")
                    pass
                try:
                    os.mkdir(cwd + endPath)
                except:
                    print("Error")
                    pass
                os.replace(cwd + downPath, cwd + endPath + f"/{torrent}")
