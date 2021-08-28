def RabbitCalculator(months, reproduction_rate):

    
    

    filhotes = 0
    filhotes2 = 0
    coelhos_adultos = 1
    

    if months == 1:
        return 1
    elif months == 2:
        return 1
    else:
        for numbers in range(months):
            print("Geracao: " + str(numbers))
            print("Número de Coelhos Adultos: " + str(coelhos_adultos))
            print("Número de Filhotes: " + str(filhotes))

            if numbers == months - 1:
                return coelhos_adultos
            
            filhotes = coelhos_adultos * 3
            coelhos_adultos = filhotes2 + coelhos_adultos
            filhotes2 = filhotes
    

print(RabbitCalculator(31, 3))