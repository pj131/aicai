# --*-- Encoding: UTF-8 --*--
import os
import shutil
import platform
import footballinfo
import infodb

basePath = r"./footballinfo"
dbFile=r'./info.db'
dbTable='info'

if platform.system() == 'Windows':
    basePath = r"D:/footballinfo"

# if os.path.isdir(basePath):
#     shutil.rmtree(basePath)

if not os.path.isdir(basePath):
    os.mkdir(basePath)

infodb.create_db(dbFile)
worldcupurl='http://league.aicai.com/cup/71/'
url1=r'http://league.aicai.com/cup/cupmatchresult!ajaxsMatchRound.htm?leagueId=71&season=2018&isownGroup=1&round=分组赛'

url2=r'http://league.aicai.com/cup/cupmatchresult!ajaxsMatchRound.htm?leagueId=71&season=2014&isownGroup=1&round=分组赛'

season={2018,2014,2010,2006}
round={'分组赛','16强','半准决赛','准决赛','季军赛','决赛'}
for s in season:
    for r in round:
        url=r'http://league.aicai.com/cup/cupmatchresult!ajaxsMatchRound.htm?leagueId=71&season=%d&isownGroup=1&round=%s' % (s,r)
        print(s,"----",r)
        print(url)
        info=footballinfo.req_get_content(url)
        infodb.db_insert(info,dbFile)
