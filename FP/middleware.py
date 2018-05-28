import Pyro4
import os
import sys

@Pyro4.expose
@Pyro4.callback
class Middleware(object):
    storage = None
    binaryFile = None
    # def setData(self, data):
    #     Middleware.storage = data
    #     print Middleware.storage
        
    
    # def getData(self):
    #     print Middleware.storage
    #     return Middleware.storage

    def readFile(self,data):
        print "read file"
        with open(data,'rb') as f1:
            buf=f1.read()
               
            Middleware.binaryFile=buf
        length = len(Middleware.binaryFile)
        print length
        # print Middleware.binaryFile
        return buf

    # def writeFile(self):
    #     with open('server/gambar2.png','wb') as f2:
    #         buf=f2.write(Middleware.binaryFile)
            
    #     print 'write file'
    #     return buf

def main():
    # listenToWorker()
    Pyro4.Daemon.serveSimple(
        {
            Middleware: "middleware"
        },
        ns=False, host="0.0.0.0", port=9001)


if __name__ == "__main__":
    main()
