n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma é {},\n o produto é {}, e a divsão é {:.3f}'.format(s, m, d),end='<<<')
print('Divisao inteira {} ,  e potência {}'.format(di, p))
