import pymongo
import re
import random
import json
from pymongo import MongoClient
from controles.ecommerces.Magazineluiza import Magalu
from controles.ecommerces.mercadolivre import mercado_livre

ecommerce_magalu = Magalu()
ecommerce_mercadolivre = mercado_livre()

class Connect:
    def __init__(self,user,password):
        self.__USER = user
        self.__PASS = password

    def login(self):
        cluster = MongoClient('mongodb+srv://'+self.__USER+':'+self.__PASS+'@cluster0.2q7tf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        self.db = cluster['feedback_product']
        self.collection = self.db['products']
        return self.db,self.collection

    def search_product(self,produto):
        self.login()
        feedbacks_list = []
        if(self.collection.find_one({'product_name':produto}) is not None):
            for result in self.collection.find({'product_name':produto}):
                item = self.collection.find_one({'product_name':produto})
                arr = {'title':item['product_name']}
                feedbacks_list.append(arr)
            return feedbacks_list
        else:
            return self.create_product(produto)

    def create_product(self,produto):
        list_of_product = ecommerce_mercadolivre.product(re.sub('-',' ',produto)) + ecommerce_magalu.procurar_produto(re.sub('-',' ',produto))
        for x in list_of_product:
            insert_dict = {'shop':x['shop'],
                           'product_name':re.sub('\s','-',x['product_name']),
                           'data':x['data'],
                           'title':x['title'],
                           'comment':x.get('comment'),
                           'likes':x['likes'],
                           'dislikes':x['dislikes'],
                            }
            self.collection.insert(insert_dict)
        return list_of_product 

