#Auditoria SEO

import urllib.request as requests

#verificar https

req = requests.Request('http://forthics.com')
resultado  = requests.urlopen(req)
print(resultado.geturl())

#el peso de la pagina
url = "https://forthics.com/index.php?action=inicio"
print("url: ",url)
site = requests.urlopen(url)
meta = site.info()
print(" Content-Length: ",site.headers['content-length'])

f = open('out.text','r')
print("File on disk: ", len(f.read()))
f.close()
