#!/usr/bin/env python3

km_l = 20
distanza = 100
costo_l = int(input("costo_l: "))
consumo = distanza / km_l

costo_tot = consumo / costo_l

if costo_tot > 100:
	costo_tot = costo_tot - (costo_tot*5/100)
print(costo_tot)
