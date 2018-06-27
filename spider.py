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

if os.path.isdir(basePath):
    shutil.rmtree(basePath)

if not os.path.isdir(basePath):
    os.mkdir(basePath)

infodb.create_db(dbFile)
worldcupurl='http://league.aicai.com/cup/71/'
url1=r'http://league.aicai.com/cup/cupmatchresult!ajaxsMatchRound.htm?leagueId=71&season=2018&isownGroup=1&round=分组赛'
info=footballinfo.req_get_content(url1)
infodb.db_insert(info,dbFile)
