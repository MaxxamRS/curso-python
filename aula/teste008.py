import math
import random
import django
import emoji

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
num = random.randint(1, 10)
print(num)
