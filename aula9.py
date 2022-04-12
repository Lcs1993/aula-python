texto = 'Curso em video python  '
print(texto[12])  #recupera uma letra da frase da posição que passamos entre colchetes
print(texto[6:15])  #recupera uma parte do texto de acordo com intervalo passado
print(texto[:12])  #recupera uma parte do texto,desde o inicio até a posição de acordo com o parametro
print(texto[1:15:3])  #corta o texto de 3 em 3
print(texto[::2])  #recupera todo o texto pulando de 2 em 2
print('''Com a adoção de processos de metodologia ágil, foi necessário que os procedimentos 
de segurança no desenvolvimento também se adaptassem, trazendo a cultura de DevSecOps, que consiste
 no modelo de inserir ações de segurança e pontos de controle em algumas etapas do desenvolvimento 
 de aplicações, seguindo a mesma mentalidade ágil.''')  # 3 aspas para textos longos e com quebra de linha
print(texto.count('o'))
print(texto.upper())
print(len(texto.strip()))
print(texto.replace('python', 'java'))
print(texto)
texto=texto.replace('python','java')
print(texto)
print(texto.lower().find('casa'))
print(texto.split())
dividido=texto.split()
print(dividido[3][2])


