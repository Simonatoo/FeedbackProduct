import requests
from bs4 import BeautifulSoup
import re
import json



class Magalu:
    def __init__(self):
        self.feedback_list = []

    def procurar_produto(self,nome_do_produto):
        self.item_name = nome_do_produto
        r = requests.get('https://www.magazineluiza.com.br/busca/'+re.sub('\s','-',nome_do_produto.lower()))
        html_content = r.content
        soup = BeautifulSoup(html_content,'html.parser')
        link = []
        for links in soup.find_all('a',class_='product-li',href=True):
            link.append(links.get('href'))
        return self.procurar_feedback(link)

    def procurar_feedback(self,link):
        try:
            for links in link[0:10]:
                r = requests.get(links)
                html_content = r.content
                soup = BeautifulSoup(html_content,'html.parser')

                for resultado in soup.find_all('div',class_='product-review__post'):
                    feedback_dict = { 
                                'shop':'Magazine Luiza',
                                'product_name':self.item_name,
                                'data':'',
                                'title': resultado.span.text,
                                'comment:': resultado.p.text,
                                'likes':0,
                                'dislikes':0}
                    if(feedback_dict['title'] != ""):
                        self.feedback_list.append(feedback_dict)
        except:
            pass
        return self.feedback_list