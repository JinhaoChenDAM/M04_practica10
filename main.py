# Importem els altres arxius.
import exercici1_A as e1a
import exercici2_A as e2a
import exercici1_B as an
import exercici2_B as tup

# Et demana la teva edat per fer-la servir més endevant.
print("Introdueix la teva edat: ")
edat = int(input())
buscaNum = 10
compteNum = 9

# Aquí imprimim per pantallam els resultats.
print(an.anyDeNeixement(edat))
print(len(tup.myTupla))
print(buscaNum in tup.myTupla)
print(tup.myTupla.count(compteNum))

# calculate the age with given birth year.
year = int(input("enter your birth year "))
print(e1a.age(year))
# managing dictionary
myDict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
# length of dictionary.
print(e2a.dictLen(myDict))
# values of dictionary.
print(e2a.dictValues(myDict))
# remove the last item.
print(e2a.removeLast(myDict))
