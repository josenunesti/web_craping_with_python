from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")

#bs = BeautifulSoup(html.read(),'html.parser')

# O bs4 suporta o objeto do urllib, portanto não é necessário ler o objeto com o metodo .read()
bs = BeautifulSoup(html,'html.parser')

''' O bs4 possui outros parser alem do parser utilizado acima. Os principais parser são:

    - lxml - Possui maior vantegem para códigos html escritos de forma errada, pois ele tem mecanismos que trata 
       esse tipo de proble. Ele tambem precisa ser instalado a parte "pip install lxml" e possui dependencias em C

    - html5lib - Possui maior tolerancia a falias que o lxml e também é mais lento comparado ao lxml. Também possui
      dependencias no entanto pode ser uma boa opção para html confusos e escritos manualmente.       
''' 

print(bs.h1)

'''
O conteúdo HTML é então transformado em um objeto BeautifulSoup com a seguinte estrutura:

html → < html > < head >... </ head > < body >... </ body > </ html > 
    – head → < head > < title > A Useful Page < title > </ head > 
        – title → < title > A Useful Page </ title > 
    – body → < body > < h1 > An Int... </ h1 > < div > Lorem ip... </ div > </ body > 
        – h1 → < h1 > An Interesting Title </ h1 > 
        – div → < div > Lorem Ipsum dolor... </ div >
'''