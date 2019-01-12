import sys
reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'but0n'
from multiprocessing import Pool, Manager
import requests, sqlite3, os, hashlib

mes = Manager()
s = mes.dict({'label' : 'NONE', 'title':'none', 'IMG':'none', 'index':0, 'total':10})
def commit(opt):
    os.system('clear')
    print('\033[41;30m MESSAGE: %-47s\033[m' % opt['label'])
    print('\033[46;30m PATH: %-50s\033[m\n\n\n' % opt['IMG'][-30:])

    print('\033[0;35m TITLE\033[m:\t%s\n\n' % opt['title'])
    bar_status = opt['index']*40/opt['total']
    status = opt['index']*100/opt['total']
    print('\n[%-40s]%s(%d/%d)' % ('>'*bar_status, str(status)+'%', opt['index'], opt['total']))

def saveImg(url):
    name = url[-16:].replace('/','_')
    try:
        cache = requests.get('http://'+url, stream = True, timeout=10)
        img = cache.content
        with open(name,'w') as jpg:
            s['label'] = cache.status_code
            s['title'] = name
            s['IMG'] = url
            s['index']+=1
            commit(s)
            jpg.write(img)
            return
    except Exception as e:
            s['label'] = e
            return






db = sqlite3.connect('../../mv.db')
s['label'] = '<<<<<<<<<<<<< Database Connected >>>>>>>>>>'
commit(s)
cur = db.cursor()
cur.execute('SELECT * FROM movies')
data = cur.fetchall()

s['total'] = len(data)
commit(s)
for e in data:
    saveImg(e[3])
print 'ok'
