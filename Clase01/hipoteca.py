# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
extra = 1000.00
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo > 0:

    saldo = saldo * (1+tasa/12) - pago_mensual
    if ((mes >= (pago_extra_mes_comienzo-1))and(mes < pago_extra_mes_fin)): #Correccion pagos extras
        saldo = saldo - extra
    
    total_pagado = total_pagado + pago_mensual
    if ((mes >= (pago_extra_mes_comienzo-1))and(mes < pago_extra_mes_fin)): #Correccion pagos extras
        total_pagado = total_pagado + extra
    
    if saldo < 0:   #Correccion ultimo mes
        total_pagado= total_pagado-abs(saldo)
        saldo = 0
 
    mes = mes + 1
    print(f"Mes {mes} Total Pagado ${total_pagado:0.2f} Saldo Restante ${saldo:0.2f}")
    #print(mes, round(total_pagado, 2), round(saldo, 2))

print(f'Total Pagado ${total_pagado:0.2f}')
print(f'Meses totales {mes}')

#print('Total pagado', round(total_pagado, 2))
#print('Meses', )