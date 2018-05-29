import Pyro4
import os
import sys
import hashlib

listWorkers=['PYRO:worker@127.0.0.1:9000','PYRO:worker@127.0.0.1:9001','PYRO:worker@127.0.0.1:9002','PYRO:worker@127.0.0.1:9003','PYRO:worker@127.0.0.1:9004']
workers=[]

@Pyro4.expose
@Pyro4.callback
class Middleware(object):
  
    def __init__(self):
        self.commands=['ls','cd','rm','upload','mv','cp']

    def getCommands(self):
        return self.commands

    def upload(self,path,data):
        numberServer = self.chooseWorker(path)
        print numberServer
        worker=workers[numberServer]
        cwd='/'
        worker.createFile(cwd,path,data)
        print 'sudah create'
    
    def chooseWorker(self,path):
        self.hashResult = hashlib.md5(path).hexdigest()
        self.number = ord(self.hashResult[-1:])

        return self.number%5
        

    def args(self,args,cwd):
        
        if args[0] == 'ls':
            print 'ls'
        if args[0] == 'upload':
            workers[0].createFile(cwd,path,data)

            print 'upload'
        if args[0] == 'cd':
            print 'cd'
        if args[0] == 'rm':
            print 'rm'
        if args[0] == 'cp':
            print 'cp'

def connectWorker():
    for worker in listWorkers:
        workers.append(Pyro4.Proxy(worker))
    print workers    
    
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
        ns=False, host="127.0.0.1", port=8001)


if __name__ == "__main__":
    main()
