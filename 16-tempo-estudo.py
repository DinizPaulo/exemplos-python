import os 
os.system("cls")

horas = float(input("QUANTAS HORAS VOCÊ ESTUDA POR DIA? "))

if (horas < 2):
    print("POUCO ESTUDO!")

elif (horas >= 2 and horas < 4):
    print ("ESTUDO MÉDIO!")

else:
    print("MUITO ESTUDO!")