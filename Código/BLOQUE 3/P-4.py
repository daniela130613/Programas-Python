# PROGRAMA 4.Programa que calcule los impuestos que debe pagar un empleado de acuerdo con la siguiente tabla:
# INGRESOS         |  IMPUESTOS
# Hasta $1000      |  5%
# $1001 - $2500    |  8%
# $2501 - $6000    |  12%
# Más de $ 6000    |  15%
# Fecha de elaboración:2024/10/29
# Elaborado por: Daniela Sahori Hinojosa Meza

ingresos =input("¿Cuáles son sus ingresos? ")
ingresos =float(ingresos)

if ingresos <=1000:
    impuesto=ingresos * 0.05
elif ingresos > 1001 and ingresos<=2500:
    impuesto=ingresos * 0.08
elif ingresos > 2501 and ingresos <= 6000:
    impuesto=ingresos * 0.12
else:
    impuesto=ingresos * 0.15

salario_total=ingresos - impuesto
print("Tus impuestos son: " + str(impuesto) + "\n y tu salario final es: " + str(salario_total))

