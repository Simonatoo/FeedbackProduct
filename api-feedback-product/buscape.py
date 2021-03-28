import re


teste = 'iphone-11-foda-pra-caramba'

valor = re.sub("-"," ",teste)

print(valor)