#!/usr/bin/python
# coding=utf-8
import xlwt
from datetime import datetime
import os 
import sys

if len( sys.argv) != 3:
	print "参数个数不对"
	print "Usage: txt2xls [txtfile] [savefile]"
	print "default txt decode is utf-8"
	exit()

txtfile = sys.argv[1] 
savefile = sys.argv[2]
txtdecode = "utf-8"

rptdata = file( txtfile, 'r')

wb = xlwt.Workbook(txtdecode)
ws = wb.add_sheet('Sheet 1')

col = 0
row = 0
while True:
	line = rptdata.readline()
	if len(line) == 0:
		break;
	print line
	strList = line.split('|')
	print strList
	col=0
	for ziduan in strList:
		print "[row=",row,"col=",col,"]",ziduan
		ws.write( row, col, strList[col])
		col=col+1
	row=row+1
	
wb.save(savefile)
print "成功生成excel文件，共",row,"行"
