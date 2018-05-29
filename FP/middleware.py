import Pyro4
import os
import sys

listWorkers=['PYRO:worker@127.0.0.1:9000','PYRO:worker@127.0.0.1:9001']
workers=[]

@Pyro4.expose
@Pyro4.callback
class Middleware(object):
  
    def __init__(self):
        self.commands=['ls','cd','rm','upload']

    def getCommands(self):
        return self.commands
        
    def upload(self,path,data):
        worker=workers[0]
        cwd='/'
        worker.createFile(cwd,path,data)
        print 'sudah create'
    
    
def connectWorker():
    workers.append(Pyro4.Proxy(listWorkers[0]))
    
    # def commands(self,command,target):
    #     if command == 'ls':
    #         #call function ls
    #     if command == 'upload':
            
    #     if command == 'cd':
    #     if command == 'rm':
        
   

def main():
    # listenToWorker()
    connectWorker()
    cwd = '/'
    path = 'file.txt'
    worker=workers[0]
    worker.touch(cwd,path)

    Pyro4.Daemon.serveSimple(
        {
            Middleware: "middleware"
        },
        ns=False, host="0.0.0.0", port=8001)


if __name__ == "__main__":
    main()
