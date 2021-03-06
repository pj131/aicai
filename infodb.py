# --*-- Encoding: UTF-8 --*--
import re
import requests
import os
import shutil
import sqlite3
import json

def db_insert(info,dbfile):
    '''insert info info to db'''
#    conn = sqlite3.connect('./info.db')
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    index=0
    for b in info:
        for l in b:
            insert_string1 = ''
            insert_string2 = ''
            update_string1 = ''
            index = index + 1
            # print('-------------', l['id'], l)
            for a in l:
                # print(a,l[a])
                if insert_string1!='':
                    insert_string1+=','
                if insert_string2!='':
                    insert_string2+=','
                insert_string1=insert_string1+'\''+a+'\''
                s=str(l[a]).replace("'", "")
                insert_string2=insert_string2+'\''+s+'\''

                if update_string1 != '':
                    update_string1 += ','
                s = str(l[a]).replace("'", "")
                update_string1 += '\'' + a + '\'=\'' + s + '\''


        #    print insert_string1
        #    print insert_string2
            insert_string='insert into info (%s) values (%s)' % (insert_string1,insert_string2)
            # print (insert_string)
            insert = True
            try :
                cursor.execute(insert_string)
                conn.commit()
                print("插入数据库成功",str(l['id']))
            except sqlite3.Error as e:
                print ("插入数据库失败",str(l['id']), e)
                insert=False
            if insert==False:
                update_string = 'update info set %s where id=\'%s\'' % (update_string1, str(l['id']))
                # print('update sql:' , update_string)
                try:
                    cursor.execute(update_string)
                    conn.commit()
                    print("更新数据库成功", str(l['id']))
                except sqlite3.Error as e:
                    print("更新数据库失败", str(l['id']), e)

    cursor.close()
    conn.close()

def create_db(dbfile):
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    s='''
    create table info(
asiaTapZh TEXT ,
asiaTape TEXT ,
asiaTapeResult TEXT ,
asiaTapeResultForAway TEXT ,
awayHalfScore TEXT ,
awayRank TEXT ,
awayScore TEXT ,
awayTeamId TEXT ,
awayTeamName TEXT ,
betId TEXT ,
colorValue TEXT ,
drawOdds TEXT ,
drawRate TEXT ,
dxTapeZh TEXT ,
europOddsResult TEXT ,
expertsNum TEXT ,
groupIndex TEXT ,
guest120Score TEXT ,
guestSpotScore TEXT ,
host120Score TEXT ,
hostHalfScore TEXT ,
hostRank TEXT ,
hostScore TEXT ,
hostSpotScore TEXT ,
hostTeamId TEXT ,
hostTeamName TEXT ,
id INT PRIMARY KEY NOT NULL ,
leagueId TEXT ,
leagueName TEXT ,
leagueType TEXT ,
loseOdds TEXT ,
loseRate TEXT ,
matchResult TEXT ,
matchTime TEXT ,
matchTimeStr TEXT ,
matchType TEXT ,
oddsSeq TEXT ,
round TEXT ,
scoreTape TEXT ,
scoreTapeResult TEXT ,
stadium TEXT ,
status TEXT ,
temperature TEXT ,
weather TEXT ,
winOdds TEXT ,
winRate TEXT 
);
    '''
    try:
        cursor.execute(s)
        conn.commit()
        print("新建数据库成功")
    except sqlite3.Error as e:
        print("新建数据库失败", e)
