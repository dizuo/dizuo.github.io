# notepad++
# -*- coding:gbk -*- 

# python代码中有中文字符串，所以编码必须统一。
# 该文件采用gbk采用gbk，则输入的txt必须是gbk编码，代码中的字符串也是gbk编码

import sys
import os

# date space flag(1 is work day, 2 is free day.)
# 2015-0506 2
def proc(fname, resmap):
	with open(fname, 'r') as fp:
		while True:
			line = fp.readline()
			
			if not line:
				break
				
			if len(line) < 5:
				continue
				
			res = line.strip().split('\t')
			
			dat = res[0].split(' ')[0]
			info = res[2]
			
			flag = 0
			
			if '周六' in info or '周日' in info:
				flag = 1				
			
			# print('%s %d' % (dat, flag))
			
			if resmap.__contains__(dat) == False:
				resmap[dat] = flag
			
def main():
	size = len(sys.argv)
	if size == 1:
		print('bad parameters')
		sys.exit(1)
	
	print(sys.argv)
	iter = 1
	
	dict_map = {}
	
	while iter < size:
		fname = sys.argv[iter]
		proc(fname, dict_map)
		
		iter += 1
		
	sorted_list = sorted( dict_map.iteritems(), key=lambda d:d[0], reverse = False)
	
	res = ''
	lineCnt = 0
	for item in sorted_list:
		xx = '\"%s\":%d, ' % (item[0], item[1])
		res += xx
		lineCnt += 1
		if lineCnt == 5:
			print(res)
			res = ''
			lineCnt = 0
	print(res)
			
	#print( dict_map )
	#print( sorted(dict_map.iteritems(), key = lambda asd:asd[0], reverse = False) )
'''
	#print dict_map directly.
	res = ''
	lineCnt = 0
	for k,v in dict_map.items():
		xx = '\"%s\":%d, ' % (k, v)
		res += xx
		lineCnt += 1
		
		if lineCnt == 5:
			print(res)
			res = ''
			lineCnt = 0			
		#print( '%s, %d' % (k, v) )		
	print(res)'''	
	
if __name__ == "__main__":
	main()