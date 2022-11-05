def anobissexto(ano):
    if ano > 0 and ano <= 2099:
        if ano % 4 == 0:
            print(f"O ano de {ano} é um ano bissexto!")
        else:
            print(f"O ano de {ano} não é um ano bissexto!")
    else:
        print("Ano inválido!")

ano = eval(input("Digite um ano entre 0 e 2099 e descubra que ele é um ano Bissexto: "))

anobissexto(ano)
