import Pyro4
import os
import sys

def readFile(data):
	print "read file"
	with open(data,'rb') as f1:
		buf=f1.read()
			
	return buf

def main():
	uri = 'PYRO:middleware@127.0.0.1:8001'
	middleware = Pyro4.Proxy(uri)
	arg = sys.argv
	nama = arg[1]
	print str(nama)

	data=readFile(nama)
	middleware.upload(nama,data)

if __name__ == '__main__':
	main()