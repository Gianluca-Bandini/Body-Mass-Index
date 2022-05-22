#Gianluca de la Rosa Bandini A01736162
#Programa que calcula el IMC y da a saber que vacuna le toca a 5 pacientes
contador_de_pacientes = 1
while contador_de_pacientes <= 5:
    Peso = float(input("Por favor, escriba su peso en kilogramos:"))
    Altura = float(input("Por favor, escriba su altura en metros:"))
    IMC = Peso/(Altura**2) #Fórmula que calula el IMC de cada paciente
    print ("Su IMC es, ", IMC)
    contador_de_pacientes = contador_de_pacientes + 1
    if IMC < 0:
        print ("Lo sentimos, el valor ingresado es incorrecto.")
    if IMC >= 0 and IMC <= 19:
        print ("Le toca la vacuna Tipo A.")
    elif IMC > 19 and IMC <= 25:
        print ("Le toca la vacuna Tipo B.") #Estructuras de repetición para decir que tipo de vacuna le toca al paciente
    elif IMC > 25 and IMC <= 29:
        print ("Le toca la vacuna Tipo C")
    elif IMC > 29 and IMC <= 35:
        print ("Le toca la vacuna Tipo D")
    else:
        print ("Le toca la vacuna tipo D2")
