d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(d))
if d<= 200:
    print('E o preço dessa passagem custa: R${:.2f}'.format(d*0.50))
else:
    print('E o preço dessa passagem custa: R${:.2f}.'.format(d*0.45))
