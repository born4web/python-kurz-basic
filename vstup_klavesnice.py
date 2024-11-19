"""
Vstup z klavesnice
"""
from xxsubtype import bench

#jmeno = input("Zadej jmeno: ")
#prijmeni = input("Zadej prijmeni: ")
while True:
    vek = input("Zadej vek: ")
    if vek.isdigit():
        break  # je to cis

print(f"Vek: {int(vek)}")