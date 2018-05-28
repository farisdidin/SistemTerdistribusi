import Pyro4
import os
import sys

def main():
	uri = 'PYRO:middleware@127.0.0.1:9001'
	middleware = Pyro4.Proxy(uri)
	arg = sys.argv
	nama = arg[1]
	print str(nama)

	middleware.setData(nama)

if __name__ == '__main__':
	main()