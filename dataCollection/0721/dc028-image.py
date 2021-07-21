# 이미지 수집 프로그램
# coding : utf-8

from bs4 import BeautifulSoup
# import requests
import urllib
import urllib3
import os
# from os.path import os
# import html5lib
# import codecs

count = 28
index = 1
maxCount = 100
imageDataDir = "C:\\Users\\poimk\\PycharmProjects\\data_collection\\images\\"
querySet = ["dog", "cat", "tiger"]  # 검색어


def getSoup(url, header):
    return BeautifulSoup(urllib3.urlopen(urllib3.Request(url, headers=header)))


if not os.path.isdir(imageDataDir):
    os.mkdir(imageDataDir)


for query in querySet:
    print("query1", query)
    imageNaming = query  # image name
    query = query.split()
    tempDirName = "_".join(query)
    query = "+".join(query)
    print("query2", query)
    isQueryKorean = False
    targetDir = imageDataDir+tempDirName
    try:
        if not os.path.isdir(targetDir):
            os.mkdir(targetDir)
    except:
        isQueryKorean = True
        imageNaming = "temp"
        targetDir = imageDataDir+"temp"
        dirNum = 0
        while True:
            tempTargetDir = targetDir+str(dirNum)
            print("tempTargetDir", tempTargetDir)
            dirNum += 1
            if not os.path.isdir(tempTargetDir):
                targetDir = tempTargetDir
                os.mkdir(targetDir)
                print("targetDir", targetDir)
                break
    index = 1
    print("targetDir", targetDir)
    for i in range(maxCount):
        # 찾고자 하는 주소에서 규칙성을 찾기
        url = 'https://www.bing.com/images/search?q='+query+'&form=HDRSC3&first=1&tsc=ImageBasicHover'
        # print(url)
        index = index + count
        page = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(page, "html5lib")
        loopkey = True
        # cntr = 1
        for imgTemp in soup.find_all('img', {'class': 'mimg'}):
            img = imgTemp.get("src")

            try:
                print(img)
                rawImg = urllib.request.urlopen(img).read()
                cntr = len([i for i in os.listdir(targetDir) if imageNaming in i]) + 1
                if cntr > maxCount:
                    break
                else:
                    print("++++", cntr)
                    f = open(targetDir+"/"+imageNaming+"_"+str(cntr)+".jpg", "wb")
                    f.write(rawImg)
                    f.close()
            except:
                print("fail to download")
        if cntr > maxCount:
            break
    if cntr > maxCount:
        break
