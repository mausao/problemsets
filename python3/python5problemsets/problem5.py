#!/usr/bin/env python3
fav_things = {}
x = "yes"
def adicionando(x):
    if x == "yes":
        tipo = input("Write one type of your favorite thing: ")
        coisa = input("Write the favorite thing of this type: ")
        fav_things[tipo] = coisa
        return(dict.values(fav_things))
    else:
        return()
def procurando(find):
    if find == "yes":
        search = input("Write one type of your favorite things: ")
        if search in fav_things:
            return(print("Your favorite thing of this type is: ", fav_things[search]))
        else:
            print("This type wasn't add to your list!")
            return(dict.values(fav_things))
    else:
        return()
while x == "yes":
    x = input("Do you want to add some types and things to your favorite list? ")
    if x == "yes":
        adicionando(x)
    else:
        h = input("Is the list complete? ")
        if h == "no":
            x = "yes"
            adicionando(x)
        else:
            g = input("Do you want to search any type in your favorite list? ")
            if g == "yes":
                find = "yes"
                procurando(find)
