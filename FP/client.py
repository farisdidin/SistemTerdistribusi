import Pyro4
import os
import sys

def main():
	uri = 'PYRO:middleware@127.0.0.1:9001'
	middleware = Pyro4.Proxy(uri)
	cmd = middleware.[fungsi waktu ngambil command]
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