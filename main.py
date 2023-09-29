from Suma import Suma

if __name__ == '__main__':

    num1 = int(input("Ingrese num1: "))
    num2 = int(input("Ingrese num2: "))

    suma = Suma(num1, num2)
    print(f"{num1} + {num2} = {suma.CalcularSuma()}")



