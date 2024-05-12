año = int(input("Introduce un año: "))

if año < 1582:
	print("No se encuentra en el periodo Gregoriano. \n Vuelve a intentarlo.")
else:
    if año % 4 != 0:
        print ("Es un año común")
    
    elif año % 100 != 0:
        print ("Es un año bisiesto")
    
    elif año % 400 != 0:
        print("Es un año común")
    
    else:
        print ("Es un año bisiesto")
