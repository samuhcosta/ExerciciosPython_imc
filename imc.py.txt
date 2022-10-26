print("_____Programa para calcular seu IMC_____")
peso = eval(input("Digite seu peso em (ex= kg): "))
altura = eval(input("Digite sua altura (ex=1.75): "))
imc = peso/altura**2

if imc < 18.5:
    print("Você está abaixo do peso ideal!")
elif imc < 25:
    print("Seu peso está NORMAL!")
elif imc >= 25:
    print("Você está acima do peso ideal!")
else:
    print("Erro, verifique o número digitado!")
