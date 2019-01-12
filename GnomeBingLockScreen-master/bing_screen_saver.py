# -*- coding:utf-8 -*-
import json
import os
import urllib.request
import datetime
# 日期，为了给文件取名
date=datetime.datetime.now().strftime('%Y-%m-%d')
# 几个url
json_url="https://www.bing.com/HPImageArchive.aspx?format=js&idx=1&n=1&mkt=en-US"
bing_url="https://www.bing.com"
# 路径
HOME=os.path.expandvars('$HOME')+"/"
json_file=HOME+".bing.json"
directory=HOME+"Pictures/Bing"
# 文件保存到$HOME/Pictures/yyyy-mm-dd.jpg
picture=directory+"/"+date+".jpg"

# 如果没有Pictures/Bing则新建
if not os.path.exists(directory):
	os.makedirs(directory)

# 如果图片不存在则保存
if not os.path.exists(picture):
	#get the json file and hide the file
	# 请求json_url获得了json文件保存到了json_file中
	json_file = urllib.request.urlretrieve(json_url,)
	#open the file and import json string
	with open(json_file[0],"r", encoding='UTF-8') as f:
		bing_json=json.load(f)
	url_append=bing_json['images'][0]['url']
	url=bing_url+url_append

	#get picture
	urllib.request.urlretrieve(url,picture)
	# change screen saver
	# 下面的gsettings表明了他是linux阵营的
	# cmd="gsettings set org.gnome.desktop.screensaver picture-uri file:"+picture
	# os.system(cmd)
