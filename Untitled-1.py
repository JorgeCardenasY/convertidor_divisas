def convertidor(sopes):
    usd=960
    sol=287
    eur=1100
    print(f"\nTus ${sopes} pesos Chilenos equivalen a: \n {round((sopes/usd),2)} dolares americanos.\n {round((sopes/eur),2)} euros.\n {round((sopes/sol),2)} soles peruanos.")


sopes = int(input("\n¿Ingresa la cantidad de pesos chilenos que deseas cambiar: "))
convertidor(sopes)