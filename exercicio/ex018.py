from math import radians, sin, cos, tan
angulo = float(input('Didite o ângulo que vc deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))

# import math
# angulo = float(input('Didite o ângulo que vc deseja: '))
# seno = math.sin(math.radians(angulo))
# print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
# cosseno = math.cos(math.radians(angulo))
# print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
# tangente = math.tan(math.radians(angulo))
# print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))