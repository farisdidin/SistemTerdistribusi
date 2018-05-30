import os
import sys

path = "/home/didin/Project/"
pathSekarang = os.getcwd()
args=[]
arg = raw_input()
args.extend(arg.split(' '))


#args = ['upload', 'worker1']
pathDownload = pathSekarang+'/'+args[1]+'/'
if os.path.isdir(pathDownload):

	dirs = os.listdir(pathDownload)
	for file in dirs:
		file = args[1]+'/'+file
		args.append(file)

	print args
else:
	print 'bukan folder'

del args[0:2]
print args
print pathSekarang
print pathDownload