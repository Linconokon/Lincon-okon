#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To LINCON
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\33[%s;1m'%str(31+j))
    x += '\33[0m'
    x = x.replace('!0','\33[0m')
    sys.stdout.write(x+'\')


def jalan(z):
	for e in z + '\':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Dev:ALI_MEHAR
##### LOGO #####
logo = """

\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
\33[1;96m꧁༒☬ᤂℌ LINCON ໔ℜ؏ৡ☬༒꧂
                 ;' ·,       ,         LINCON         •98• 
         ;     '·, ,'·,  ' ·, 
         ',       ,'   ' ·,    ' ·, 
  , · " " ·,     :',       '·,      ' · ,          ,   ·  ' ; 
,"::' ·,::   ", ,':::' ,       ' · ,   ,  ,' ·  '            ; 
¦::                 ' ··,:::::':·,......  , ' 
",:::      ,":::::          ' ··,::,::,'_._._._._._._._._._', 
         ,"::::::          ´   , "      „ „",  ,"      „ „', 
        ,"::::                 ;     „"   ,"   ;     „"  ," 
        ;::::                   "„    ", "     ",  „ "„ " ; 
        ;:::       , "  "   "   "   "     „"·::::::::::::::"„- , 
        ;::      ,"                         "„·:::::::::::::·„" 
        ;::      ;                             "„·:::::::„" 
        ",::    ;         ,·'                       ", " 
          ",::   ",       '·,         ˆ ·,         ,·'    ,ˆ 
            ",::   ",                     ˆ · , ,' , · ˆ    ," 
            _",:::   ",_._._._._._._.      _._._ ," 
          ,'                             ,":::",          ', 
        ,'                            ,"::::::::",          ', 
       ,'                           ,' ",::::::::,",          ', 
      ,',.,. ,.,.,.,.,.,.,.,.,.,.,.,"   "::::"    ", 
         ,":::::                       ,":::",        º² "ALI
       ,":::                          ,"::::::",            ", 
      ,"::                          ,":::::::::",            ", 
     ,"::                          ,":::::::::::",            "
   |___'|.·´�    LINCON     -«��
\33[1;91m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\33[1;93mLINCON\33[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•
\33[1;92m:•◈•🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️
\33[1;92m:•◈•║║─💐💐─────║🌷🌷─────║║     🌸
\33[1;93m:•◈•💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮
\33[1;93m:•◈•║║║💐💐║╚╝║║═╣🌷🌷╔╗║╔═╣╚╝🌸   
\33[1;98m:•◈•║╚╣💐💐╠╗╔╣║═╣🌷🌷║╔╗║╚═╣╔🌸   LINCON
\33[1;98m:•◈•🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺
\33[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\33[1;95mLINCON\33[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\\1b[1;93mPlease Wait \1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\33[31mNot Vuln"
vuln = "\33[32mVuln"

os.system("clear")
print  """
\33[1;96m ALI_MEHAR
\33[1;96m╭╮╱╭┳━━━┳━━━┳╮╭━┳━━━┳━━━╮
\33[1;96m┃┃╱┃┃╭━╮┃╭━╮┃┃┃╭┫╭━━┫╭━╮┃
\33[1;96m┃╰━╯┃┃╱┃┃┃╱╰┫╰╯╯┃╰━━┫╰━╯┃
\33[1;96m┃╭━╮┃╰━╯┃┃╱╭┫╭╮┃┃╭━━┫╭╮╭╯
\33[1:96m┃┃╱┃┃╭━╮┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮
\33[1;96m╰╯╱╰┻╯╱╰┻━━━┻╯╰━┻━━━┻╯╰━╯
\33[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\33[1;93mLINCON\33[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"""
jalan("\33[1;96m----------------------//\")
jalan("\33[1;96m---------------------// ¤ \")
jalan("\33[1;96m---------------------\ ¤ //")
jalan("\33[1;96m---------------------- \//")
jalan("\33[1;96m-------------------- (___)")
jalan("\33[1;96m---------------------(___)")
jalan("\33[1;96m---------------------(___)")
jalan("\33[1;96m---------------------(___)_________")
jalan("\33[1;96m--------\____/\_/----\_/\____/")
jalan("\33[1;96m------------\_°_[------------]_ _° /")
jalan("\33[1;96m----------------\°_¤ ---- ¤_°_/")
jalan("\33[1;96m--------------------\__°__ /")
jalan("\33[1;96m---------------------|\°_/|")
jalan("\33[1;96m---------------------[|\/|]")
jalan("\33[1;96m---------------------[|[¤]|]")
jalan("\33[1;96m---------------------[|;¤;|]")
jalan("\33[1;96m---------------------[;;¤;[]")
jalan("\33[1;96m---
