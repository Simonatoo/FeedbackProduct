import requests
import json

class mercado_livre:

    def __init__(self):
        self.mercado_livre_feedback_list = []

    def request(self,CATEGORY_ID):
        for item_id in CATEGORY_ID:
            res = requests.get("https://api.mercadolibre.com/reviews/item/"+item_id)
            total = res.json()['paging']['total']
            for review in res.json()['reviews']:
                item_dict = { 
                    'shop': 'Mercado Livre',
                    'product_name':self.item_name,
                    'data': review['date_created'],
                    'title': review['title'],
                    'comment': review['content'],
                    'likes': review['likes'],
                    'dislikes': review['dislikes']
                }
                self.mercado_livre_feedback_list.append(item_dict)
        return self.mercado_livre_feedback_list

    def product(self,ITEM_NAME):
        self.item_name = ITEM_NAME
        res = requests.get("https://api.mercadolibre.com/sites/MLB/search?q="+ITEM_NAME)
        item_id = res.json()['results']
        products_list = []
        for x in range(0,3):
            products_list.append(item_id[x]['id'])
        return self.request(products_list)

# mercado = mercado_livre()
# arr = mercado.product('samsung')

# for x in arr:
#     print(x['title'])