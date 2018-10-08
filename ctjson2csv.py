#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#######################################################

#Copyright 2018 Marvelousblack<Galaxyhappy5@gmail.com>#

#######################################################

import json

try:
        with open('./class.json',encoding='utf-8') as f:
            data = json.loads(f.read())
            f.close()
except:
        print('The file is no found!')


starttimetable = {'01':'08:30','02':'09:20','03':'10:25','04':'11:15','05':'13:50','06':'14:40','07':'15:30','08':'16:30','09':'17:20','10':'18:30','11':'19:20','12':'20:10'} 
endtimetable = {'01':'09:15','02':'10:05','03':'11:10','04':'12:00','05':'14:35','06':'15:25','07':'16:15','08':'17:15','09':'18:05','10':'19:15','11':'20:05','12':'20:55'} 

outputdata = []
row = data['rows']

for element in row:
    subject = element['kcmc']
    startdata = element['pkrq'].replace("-","/")
    enddata = startdata
    starttime = starttimetable.get(element['jcdm'][0:2],'error')
    endtime = endtimetable.get(element['jcdm'][-2:],'error')
    description = element['sknrjj']
    location = element['jxcdmc']
    out= subject+","+startdata+","+starttime+","+enddata+","+endtime+","+description+","+location
    outputdata.append(out)

with open('./csvout.csv','wt',encoding='utf-8') as csvout:
    print('Subject,Start Date,Start Time,End Date,End Time,Description,Location',file=csvout)
    for outdata in outputdata:
        print(outdata,file=csvout)
    csvout.close()
