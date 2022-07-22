#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import csv
import os
#按照列表的格式读取
def readCsvList():
   with open('data.xls','r')as f:
      reader = csv.reader(f)
      next(reader)
      #用迭代器的方式读取
      db = [item for item in reader]
      print(list(db))
      #按循环的方式读取
      for item in reader:
         print(list(item)['URL'])
readCsvList()
print(type(readCsvList()))

#按照字典的方式读取文件内容
def readCsvDict():
   with open('CSV.csv','r')as f:
      reader = csv.DictReader(f)
      for item in reader:
         print(dict(item)['caseID'])

readCsvDict()