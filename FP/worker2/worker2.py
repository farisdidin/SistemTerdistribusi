from __future__ import print_function
import Pyro4
import os
import shutil

@Pyro4.expose
@Pyro4.callback

class Worker(object):
    sharingFolder = {}

    def __init__(self):
        self.sharingFolder['folder'] = '/home/didin/Project/SistemTerdistribusi/FP/worker2/' #/home/didin/Project/SistemTerdistribusi/FP/

    def isFolder(self, path):
        fullPath = self.sharingFolder['folder'] + path
        if(os.path.isdir(fullPath)):
            return True
        else:
            return False

    def getSharingFolder(self):
        return self.sharingFolder

    def notEmpty(self, path):
        fullPath = self.sharingFolder['folder'] + path
        if(os.path.isfile(fullPath)):
            return 1, fullPath
        elif(os.path.isdir(fullPath)):
            return 2, fullPath
        else:
            return 0, fullPath

    def removeData(self, cwd, path=None):
        flag, fullPath = self.notEmpty(path)
        if(flag == 1):
            os.remove(fullPath)
            return None, "File removed"
        elif(flag == 2):
            shutil.rmtree(fullPath)
            return None, "Folder removed"
        else:
            return 'No file to remove', None

    def listSource(self, cwd, path=None):
        flag = self.isFolder(path)
        if(flag):
            print(self.sharingFolder['folder'] + path)
            listFolder = os.listdir(self.sharingFolder['folder'] + path)
            return None, listFolder
        else:
            return 'No such folder', []
        
    def getSize(self):
        disk = os.statvfs(self.sharingFolder['folder'])
        return disk.f_bfree

    def createFolder(self, cwd, path):
        fullPath = self.sharingFolder['folder'] + path
        print('New folder' + fullPath)
        if(os.path.exists(fullPath)):
            return 'Folder already exists', None
        try:
            os.makedirs(fullPath)
            return None, 'Folder created'
        except Exception as ex:
            err = str(ex)
            err = err.replace(self.sharingFolder['folder'], '')
            print(err)
            return err, None

    def createFile(self, cwd, path, data):
        create = 'create'
        print (create)
        fullPath = self.sharingFolder['folder'] + path
        if(os.path.isfile(fullPath)):
            return 'File already exists', None
        try:
            with open(fullPath, 'wb') as file:
                file.write(data.encode('utf-8').strip())
            return None, 'File created'
        except Exception as ex:
            err = str(ex)
            return err.replace(self.sharingFolder['folder'], ''), None
    
    # def readFile(self, cwd, path=None):
    #     fullPath = self.notEmpty(path)
    #     data = ''
    #     with open(fullPath, 'rb') as file:
    #         data = file.read()
    #     return data

    def readFile(self, cwd, path):
        # fullPath = self.notEmpty(path)
        read = 'read'
        print (read)
        fullPath = path
        data = None
        with open(fullPath, 'rb') as file:
            data = file.read()
        return data
    
    def touch(self, cwd, path=None):
        fullPath = self.sharingFolder['folder'] + path
        print(fullPath)
        if(os.path.isfile(fullPath)):
            return 'File already exists', None
        try:
            with open(fullPath, 'wb'):
                os.utime(fullPath, None)
                return None, 'File created'
        except Exception as ex:
            err = str(ex)
            return err.replace(self.sharingFolder['folder'], ''), None

def main():
    Pyro4.Daemon.serveSimple ({
        Worker: "worker"
    },
    ns = False, host = "127.0.0.1", port = 9001)

if __name__ == "__main__":
    main()