print("Konversi Suhu Kelvin")

# Entry
suhu = input("Masukan Suhu Dalam Kelvin")

# rumus
C = float(suhu) - 273
R = 4/5 * (float(suhu) - 273)
F = 9/5 * (float(suhu) - 273) + 32

# output
print(suhu + "Kelvin Sama Dengan")
print(str(C) + " Celcius ")
print(str(R) + " Reamur ")
print(str(F) + " Fahrenheit ")