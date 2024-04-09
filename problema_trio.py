def imprimir_agradecimento():
    print("Obrigado por utilizar a nossa calculadora de IMC!")

imprimir_agradecimento()

def calcula_imc():
    """
    Crie uma função que pede a altura e o peso do usuário, calcula o seu IMC e imprime o resultado. 
    Ao final faça um commit no repositório remoto. Dica: O cálculo do IMC é: peso/(altura x altura). 
    Exemplo de saída: "O seu IMC é: [resultado] "
    """
    print("Calculadora de IMC")
    try:
        altura = float(input("Digite a sua altura em metros(Ex: 1.70): "))
        peso = float(input("Digite o peso em kg(Ex: 68): "))
        imc = peso / (altura*altura)
        print("O seu IMC é: ", round(imc,2))
    except:
        print("Entrada inválida")
        calcula_imc()
