import Pyro4
import os
import sys

def readFile(data):
	print "read file"
	with open(data,'rb') as f1:
		buf=f1.read()
			
	return buf

def writeFile(path,data):
	with open(path,'wb') as f2:
		buf = f2.write(data)
	return buf

def main():
	uri = 'PYRO:middleware@127.0.0.1:8001'
	middleware = Pyro4.Proxy(uri)
	cmd = middleware.getCommands()
	cwd = '/'
	args = []
	while True:
		print ('cli >> '+ cwd + ' ')
		command = raw_input()
		args.extend(command.split())

		if args[0] in cmd:
			if args[0] == 'cd':
				cwd = middleware.args(args, cwd)

			if args[0] == 'ls':
				cwd = middleware.args(args, cwd)
				if(isinstance(results, list)):
					for result in results:
						print(result)
				else:
					print(results)
					
			if args[0] == 'rm' or args[0] == 'touch':
				cwd = middleware.args(args, cwd)

			if args[0] == 'cp' or args[0] == 'mv':
				cwd = middleware.args(args, cwd)

		elif args[0] == '':
			continue
		
		elif args[0] == 'quit':
			break

		else:
			print ('server >> command \''+args[0]+'\' not found')



if __name__ == '__main__':
	main()