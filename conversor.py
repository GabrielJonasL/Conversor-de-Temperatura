def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def exibir_menu():
    print("conversor de Temperatura")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    print("3. Sair")

    if __name__ == "__main__":
        while True:
                exibir_menu()
                opcao = input("Escolha a opcao (1-3): ")

                if opcao == "1":
                    try:
                        celsius = float(input("Temperatura em Celsius: "))
                        fahrenheit = celsius_para_fahrenheit(celsius)
                        print(f"Resultado em Fahrenheit: {fahrenheit:.2f}F")
                    except ValueError:
                        print("Erro, digite novamente")

                elif opcao =="2":
                    try:
                        fahrenheit = float(input("Digite em Fahrenheit: "))
                        celsius = fahrenheit_para_celsius(fahrenheit)
                        print(f"Resultado em Celsius: {celsius:.2f}C")
                    except ValueError:
                        print("Erro, tente novamente.")

                elif opcao == "3":
                    print("Encerramndo Conversor...")
                    break
                else:
                    print("Opcao Invalida.")