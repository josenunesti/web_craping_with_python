from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

bs = BeautifulSoup(html, "html.parser")

lista_nome = bs.find_all('span',{'class':'green'})

for nome in lista_nome:
    print(nome.get_text())