# -*- coding: utf-8 -*-
import Pyro4
import sys
import os


def writeFile(dataFile,namaFile):
    with open(namaFile,'wb') as f2:
        fileDataSend=f2.write(dataFile.encode('utf-8'))
        
    return fileDataSend
# .encode('utf-8').strip()

def main():
    uri = 'PYRO:middleware@10.151.252.249:9001'
    middleware = Pyro4.Proxy(uri)
    # data = middleware.getData()
    # print data
    name = raw_input()
    fileFromMiddleware=middleware.readFile(name)
    print len(fileFromMiddleware)
    writeFile(fileFromMiddleware,name)
    # middleware.writeFile()
    print "sudah write"
    # writeFile(fileFromMiddleware)




if __name__=="__main__":
    main()
