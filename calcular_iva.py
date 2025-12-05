


def calcular_iva():
    subtotal = float(input("Ingrese el subtotal "))
    iva = subtotal*0.19
    return iva
print(f" el iva es {calcular_iva()}")

subtotal = float(input("Ingrese el subtotal "))
iva = subtotal*0.19
def calcular_iva():
    return iva
print(" el iva es " , iva)


#nomina
def calcular_nomina(valor_hora, horas, fondo_empleados, otras_deducciones, activo):
    if activo:  # Si el empleado está activo
        salario_bruto = valor_hora * horas
        total_deducciones = fondo_empleados + otras_deducciones
        total_pagar = salario_bruto - total_deducciones
        return total_pagar
    else:
        return 0  # Si no está activo, no se paga nada


# --- Variables definidas ---
valor_hora = 12000           # Valor pagado por hora trabajada
horas = 40                   # Cantidad de horas trabajadas
fondo_empleados = 50000      # Deducción fondo de empleados
otras_deducciones = 20000    # Otras deducciones
activo = True                # Estado del empleado (True = activo, False = inactivo)

# --- Cálculo usando la función ---
total = calcular_nomina(valor_hora, horas, fondo_empleados, otras_deducciones, activo)

# --- Resultado ---
if activo:
    print(f"El total a pagar al empleado es: ${total:.2f}")
else:
    print("El empleado no está activo, no se genera pago.")
