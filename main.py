"""Importem els altres arxius."""
import exercici1_B as an
import exercici2_B as tup

"""Et demana la teva edat per fer-la servir més endevant."""
print("Introdueix la teva edat: ")
edat = int(input())
buscaNum = 10
compteNum = 9

"""Aquí imprimim per pantallam els resultats."""
print(an.anyDeNeixement(edat))
print(len(tup.myTupla))
print(buscaNum in tup.myTupla)
print(tup.myTupla.count(compteNum))