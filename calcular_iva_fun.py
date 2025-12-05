#función sin parámetros ni retorno
def saludar_usuario():
    print("¡Hola,: Bienvenido al programa!")
saludar_usuario()

#función con parámetros pero sin retorno
def saludar_usuario(nombre):
    print(f"¡Hola, {nombre}: Bienvenido al programa!")
saludar_usuario("reinaldo")    

#función con parametro y retorno
def calcular_iva(venta):
    return venta*0.19
print(calcular_iva(10000))

#programa que calcula el valor del iva 
def calcular_iva():
    subtotal = float(input("Ingrese el subtotal "))
    iva = subtotal*0.19
    return iva
print(f" el iva es {calcular_iva()}")

#Calcular ventas con parametros y retorno
def calcular_total(sub_total , IVA=0.19):
    total = sub_total*IVA
    return total+sub_total
sub_total = float(input(" ingrese el subtotal "))
print(f" el total a pagar es {calcular_total(sub_total)} ")