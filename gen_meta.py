#!/usr/bin/env python
#-*- coding:utf8 -*-
import os, json

def walkDirs(targetDir):
    result = {}
    for dirs in os.listdir(targetDir):
        name2Files = {}
        for f in os.listdir(os.path.join(targetDir, dirs)):
            fileName = f.split('.')[0]
            li = fileName.split('_')
            name2Files.setdefault(li[0], [])
            name2Files[li[0]].append(os.path.join(targetDir, dirs, f))
        result[dirs] = name2Files
    return result

if __name__ == '__main__':
    audios = walkDirs('mp3')
    imgs = walkDirs('img')

    newAudios = {}
    for k, v in imgs.items():
        newAudios[k] = {}
        for name in v.keys():
            newAudios[k][name] = audios[k][name]

    with open("meta.dat", "w") as fp:
        fp.write(json.dumps(newAudios, indent=4))



        

        

