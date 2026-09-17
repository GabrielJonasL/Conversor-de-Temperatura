def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32



def exibir_menu():
    print("conversor de Temperatura")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Sair")

    if __name__ == "__main__":
        while True:
                exibir_menu()
                opcao = input("Escolha a opcao (1-2): ")

                if opcao == "1":
                    try:
                        celsius = float(input("Temperatura em Celsius: "))
                        fahrenheit = celsius_para_fahrenheit(celsius)
                        print(f"Resultado em Fahrenheit: {fahrenheit:.2f}F")
                    except ValueError:
                        print("Erro, digite novamente")
                
                elif opcao == "3":
                    print("Encerramndo Conversor...")
                    break
                else:
                    print("Opcao Invalida.")