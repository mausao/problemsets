#!/usr/bin/env python3
taxa = ["sapiens", "erectus", "neanderthalensis"]
print("A variável taxa contêm: ", taxa)
print("O resultado de taxa[1] é: ", taxa[1])
varTaxa = type(taxa)
print("O tipo da primeira variável é: ", varTaxa)
separador = ", "
species = separador.join(taxa)
print("A primeira variável separada em string por , fica: ", species)
print("O resultado de species[1] é: ", species[1])
varSpecies = type(species)
print("O tipo da segunda variável é: ", varSpecies)
sortTaxa = sorted(taxa)
sortSpecies = sorted(species)
print("A primeira variável ordenada alfabeticamente é: ", sortTaxa, "e a segunda é: ", sortSpecies)
sortLenTaxa = sorted(taxa, key=len)
sortLenSpecies = sorted(species, key=len)
print("A primeira variável ordenada pelo tamanho da string é: ", sortLenTaxa)
print("A segunda variável ordenada pelo tamanho da string é: ", sortLenSpecies)
