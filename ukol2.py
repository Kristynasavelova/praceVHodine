cislo1 = float(input("zadej desetinné číslo "))
cislo2 = float(input("zadej desetinné číslo "))

soucet = cislo1+cislo2 
rozdil = cislo1-cislo2
soucin = cislo1*cislo2
if cislo2 != 0:
    podil = cislo1/cislo2
else:
    podil = 0

print(f"Součet: {soucet:.2f}")
print(f"rozdíl: {rozdil:.2f}")
print(f"součin: {soucin:.2f}")

if podil != 0:
    print(f"podíl: {podil:.2f}")
else:
    print("Podíl nelze vypočítat.")
