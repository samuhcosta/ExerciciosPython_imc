def imc(peso, altura):
    imc = peso/altura**2
    if imc < 18.5:
        print("Você está abaixo do peso ideal!")
    elif imc < 25:
        print("Seu peso está NORMAL!")
    elif imc >= 25:
        print("Você está acima do peso ideal!")
    else:
        print("Erro, verifique o número digitado!")

print("Programa para calcular seu peso ideial:")

peso = eval(input("Digite seu peso (ex'kg'): "))
altura = eval(input("Digite sua altura (ex'1.74'): "))
imc(peso, altura)
