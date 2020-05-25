from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    # html = urlopen("https://site_nao_existe.com.br") # Forçando erro URLError
    # html = urlopen("http://pythonscraping.com/pages/page1.html") # Forçando o sucesso
    html = urlopen("http://pythonscraping.com/pages/page1.html") # Forçando o sucesso
except HTTPError as e:
    print(e)
except URLError as e:
    print("Servidor não encontrado")
else:    
    print("Servidor encontrado!")

    '''
        Existem situações que o site foi encontrado e esta ok, porém o conteudo do site pode 
        não ser o esperado. Neste cenário é impressindivel validar o conteudo com o BS4
    '''
    html = BeautifulSoup(html.read(), "html.parser")

    ''' Se uma tag não existir, o bs4 retorna None por padrão '''
    print(html.tag_inexistente)

    ''' 
        Caso tentar acessar uma tag dentro de uma tag que não exista, ou seja (None), uma 
        AttributeError sera lançada
    '''
    try:
        print(html.tag_inexistente.qualquer_outra_tag)
    except AttributeError as e:
        print("Tag inexistente")

    ''' Tratamento recomendado com exemplo de captura da tag H1 do site alvo: '''
    try:
        conteudo = html.h1
    except AttributeError as e:
        print("Tag inexistente")
    else:
        if html.h1 == None:
            print("Tag inexistente")
        else:
            print(html.h1)

    ''' 
        O ultimo exemplo acima é consideravelmente custoso de ler devido aos tratamento que um 
        scraper necessita, portanto é valido criar funções de apoio para encapsular algumas 
        tratativas e até mesmo buscar patterns existentes que lidam com esse tipo de situação
        visando um código mais limpo e legivel.
    '''  