#!/usr/bin/env python3
import sys
favThing1 = sys.argv[1]
favThing2 = sys.argv[2]
favThing3 = sys.argv[3]
favThing4 = sys.argv[4]
favThing5 = sys.argv[5]
list_favThings = [favThing1, favThing2, favThing3, favThing4, favThing5]
print("As suas coisas favoritas são: ", list_favThings)
print("A sua terceira coisa favorita é: ", list_favThings[2])
replace = input("Qual é sua canção favorita? ")
list_favThings.pop(2)
list_favThings.insert(2, replace)
print("Sua nova lista de coisas favoritas é: ", list_favThings)
newElement = input("Digite uma nova coisa favorita: ")
list_favThings.append(newElement)
print("Sua nova lista de coisas favoritas é: ", list_favThings)
newFirstElement = input("Digite a sua coisa mais favorita de todas: ")
list_favThings.insert(0, newFirstElement)
print("Sua nova lista de coisas favoritas é: ", list_favThings)
newOtherElement = input("Digite outra coisa favorita: ")
list_favThings.insert(1, newOtherElement)
print("A sua nova lista de coisas favoritas é: ", list_favThings)
list_favThings.pop()
print("Removendo o ultimo valor")
print("A sua nova lista de coisas favoritas é: ", list_favThings)
list_favThings.pop(0)
print("Removendo o primeiro valor")
print("A sua nova lista de coisas favoritas é: ", list_favThings)
list_favThings.pop(1)
print("Removendo o segundo valor")
print("A sua nova lista de coisas favoritas é: ", list_favThings)
separator = ", "
ListaDeFavoritos = separator.join(list_favThings)
print("A sua lista atualizada de coisas favoritas transformada em string é: ", ListaDeFavoritos)
