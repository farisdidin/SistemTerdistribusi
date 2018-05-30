import sys
import Pyro4
import os

def readFile(file):
    print ">> Membaca file"
    with open(file,'rb') as f1:
        buf=f1.read()
    return buf

def writeFile(file,data):
    with open(file,'wb') as f2:
        buf = f2.write(data.encode('utf-8').strip())
    return buf

def main():
    #uri = 'PYRO:middleware@10.151.253.198:8001'
    uri = 'PYRO:middleware@127.0.0.1:8001'
    middleware = Pyro4.Proxy(uri)
    commands = middleware.getCommands()
    cwd = '/'
    while True:
        args = []
        print ('cli >> '+ cwd ),
        arg = raw_input()
        args.extend(arg.split(' '))

        if args[0] in commands:
            if args[0] == 'exit':
                break

            if args[0] == 'cd':
                errors, results, cwd = middleware.args(args, cwd)
                if(errors is not None):
                    print('Server: '+errors)

            if args[0] == 'ls':
                errors, results, cwd = middleware.args(args, cwd)
                if(errors is not None):
                    print('Server: '+errors)
                else:
                    if(isinstance(results, list)):
                        for result in results:
                            print(result)
                    else:
                        print(results)

            if args[0] == 'rm' or args[0] == 'touch' or args[0] == 'cp' or args[0] == 'mv':
                errors, results, cwd = middleware.args(args, cwd)
                if(errors is not None):
                    print('Server: '+errors)
                else:
                    print('Server: '+results)

            if args[0] == 'upload':
                print '>> ' + str(args)
                print '>> Sedang mengupload...'
                count = 0
                #upload folder
                currentPath = os.getcwd()
                pathDownload = currentPath+'/'+args[1]+'/'
                if os.path.isdir(pathDownload):
                    fileToUpload=[]
                    dirs = os.listdir(pathDownload)
                    for file in dirs:
                        #fileToUpload.append(file)
                        fileDownload = args[1]+'/'+file
                        data = readFile(fileDownload)
                        middleware.upload(file,data)
                else:
                    for data in args:
                        count+=1
                        data = readFile(args[count])
                        middleware.upload(args[count],data)
                        print '>> File ' + args[count] + ' berhasil di upload!'
                        print count
                        if(count==len(args)-1):
                            break
                    


                del args[:]
                continue

            if args[0] == 'download':
                print '>> ' + str(args)
                print '>> Sedang mendownload...'
                dataDownload = middleware.download(args[1])
                writeFile(args[1],dataDownload)
                del args[:]

        elif args[0] == '':
            continue

        else:
            print('server: command not found: '+args[0])



if __name__ == "__main__":
    main()
