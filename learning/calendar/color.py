import os,sys

if __name__ == "__main__":
	vals = sys.argv[1]
	
	res = vals.split(',')
	
	s = ''
	for i in res:
		print( hex( int(i) ) )
		