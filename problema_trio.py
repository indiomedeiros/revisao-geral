def cumprimenta_usuario():
    try:
        nomeUsuario = str(input("Insira o seu nome: "))
        print(f"Olá, {nomeUsuario}! Seja bem-vindo(a) a calculadora de IMC!")
    except:
        print("Os dados inseridos não foram aceitos, tente novamente!")
        cumprimenta_usuario()