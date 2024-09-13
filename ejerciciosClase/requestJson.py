#!/usr/bin/python
# Hacking Fight Club

import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
resp_json = r.json()

print("Titulo: "+resp_json['title'])
print()
print("Cuerpo: "+resp_json['body'])

s = requests.post('https://jsonplaceholder.typicode.com/posts', {'title':'Lordran', 'body':'Me gusta Dark Souls', 'userId':'3005'})
print()
print('El código de respuesta al POST fue '+ str(s.status_code))

# 3
u = requests.post('https://jsonplaceholder.typicode.com/users', {'title':'juanchoeh', 'body':'Tambien me gusta el pene', 'userId':'1306'})
print()
print('El código de respuesta al POST de usuario fue '+ str(s.status_code))


u = requests.post('https://regres.in/api/users', {'id':5,'first_name':'juanchoeh', 'last_name':'Computologo', 'id':'456'})
print()
print(s.text)
