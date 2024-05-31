import os

mensagens = []

nome = input("Nome : ")

while True:
    #limpando cache
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'],"-", m['texto'])

    print("__________________")

    #obter texto
    texto = input("mensagens : ")
    if texto == "fim":
        break
    
    #adc mensagens na lista
    mensagens.append({
        "nome" : nome,
        "texto": texto
    })