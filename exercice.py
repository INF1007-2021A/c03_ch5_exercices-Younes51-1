#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0 :
        number *= -1
    return number

def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    Liste=""
    for caractère in prefixes :
        Liste += caractère + suffixe + ","
    return Liste


def prime_integer_summation() -> int:
    number=1
    i=0
    somme=0
    count=0
    while count <100 :
        Prime=True
        number+=1
        for i in range(2,number-1):
            if number % i == 0:
                Prime= False
        if Prime==True:
            somme +=number
            count +=1
    return somme


def factorial(number: int) -> int:
    factoriale=number
    if number==0 :
        factoriale=1
    else :
        for i in range (number-1,1,-1) :
            factoriale *= i
    return factoriale


def use_continue() -> None:
    affichage=""
    for i in range (1,11) :
     if i!=5 :
        affichage += str(i)+ ","
    return affichage 


def verify_ages(groups: List[List[int]]) -> List[bool]:
    groups_acceptes =[False for _ in range(len(groups))]
    for i in range(len(groups)):
        Acceptance = True
        if len(groups[i]) > 10 or len(groups[i]) <= 3 :
            Acceptance = False
        else:
            for j in range(len(groups[i])):
                if groups[i][j] == 25:
                    Acceptance = True
                elif groups[i][j] == 50 or groups[i][j] > 70:
                    Acceptance = False
                elif groups[i][j] < 18:
                    Acceptance = False
        if Acceptance == True:
            groups_acceptes[i] = True
    return groups_acceptes

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est: {use_continue()} ")

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
