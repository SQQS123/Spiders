# JianSo_Movie

* 多进程电影资源爬虫
* 电影图片抓取脚本
* Flask+Nginx+wsgi网站架构
* SQlite3

# [Demo](http://but0n.me)
`共收录了8309部电影!`

![demo](/img/webno.gif)

# Crawler

![get_mov](/img/get_mov.png)
^ Get link, name, detail, image url of movies

![get_img](/img/get_img.png)
^ Download images

# Tree
```
├── LICENSE
├── README.md
├── config.ini
├── hello.py    \\Flask
├── img   \\Readme img
│   ├── get_img.png
│   ├── get_mov.png
│   └── webno.gif
├── jian_nginx.conf   \\Nginx Config
├── mv.db   \\Data base
├── note.txt    \\Python Note
├── robot.py    \\电影爬虫,数据将保存在mv.db
├── static
│   ├── css
│   │   ├── animation.css
│   │   ├── index.css
│   │   ├── main.css
│   │   └── search.css
│   ├── images
│   │   └── Get_img.py    \\Download images
│   ├── img
│   │   └── down.png    \\HTML img
│   └── scripts
│       ├── index.js
│       ├── jquery-2.1.4.min.js
│       └── search.js
├── templates
│   ├── index.html
│   └── searchList.html
└── venv
    ├ ...
```
