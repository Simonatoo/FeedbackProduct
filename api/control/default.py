import requests
from bs4 import BeautifulSoup

class Default_data:
    def mercado_livre(self):
        def buscando(req):
            urls = []
            url = ('https://lista.mercadolivre.com.br/'+req)
            r = requests.get(url)
            html_content = r.text
            soup = BeautifulSoup(html_content, 'html.parser')
            for produtos in soup.find_all('div', class_='ui-search-result__image'):
                teste = produtos.a['href']
                urls.append(teste)
            return urls

        def produtos(link_do_produto):
            produtos = []
            for link in link_do_produto:
                try:
                    req = requests.get(link)
                    soup1 = BeautifulSoup(req.text, 'html.parser')
                    lista_de_comentarios = soup1.find_all('div', class_='ui-pdp-reviews__comments__review-comment')
                    for comentario in lista_de_comentarios:
                        produtos.append({'titulo': comentario.h2.text, 'comentario': comentario.p.text})
                except:
                    pass 
            return produtos
            
        urls = buscando('piso vinilico Durafloor')
        resultado = produtos(urls)

        return resultado