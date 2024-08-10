añoactual= int(input("Introduzca el año actual: "))
añocualquiera= int(input("Introduzca un año cualquiera: "))

if añoactual== añocualquiera:
    print("Has introducido el mismo año que el actual")


if añocualquiera-añoactual == 1:
     print("Para llegar a",añocualquiera, "falta 1 año")  

elif añoactual < añocualquiera:
    años = añocualquiera - añoactual
    print("Faltan", años, "años para", añocualquiera )

 

if añoactual-añocualquiera == 1:
      print("Desde el año", añocualquiera, "ha pasado 1 año")

elif añoactual >añocualquiera:
     años = añoactual- añocualquiera
     print("Ha pasado",años,"años desde", añocualquiera)

 
