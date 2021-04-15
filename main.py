# import numpy as np # Not used
'''
Program FizzBuzz
by AirbornDevil

Σε ένα σύνολο από ακέραιους αριθμούς ελέγχουμε έναν έναν τους αριθμούς.
Αν ο αριθμός διαιρείται τέλεια με το 3, τότε εμφανίζουμε Fizz.
Αν ο αριθμός διαιρείται τέλεια με το 5, τότε εμφανίζουμε Buzz.
Αν διαιρείται τέλεια και με τους δύο, τότε εμφανίζουμε FizzBuzz.
Σε κάθε άλλη περίπτωση εμφανίζουμε τον αριθμό.
'''

from FizzBuzz import fizzbuzz
import FizzBuzz

from utls import userInput

# Αλλαξε τα F και B για να αλλάξουν τα Fizz Buzz του παιχνιδιού
FizzBuzz.F = 3
FizzBuzz.B = 5

def main():

    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # Για να ξεχωρίζει η κάθε επανάληψη
    print("\nΚαλώς ήρθατε στο FizzBuzz !!!")
    print("\nΘα πρέπει να μου δώσετε τα όρια των αριθμών που θα ελέγξω...")

    input_nums = userInput()
    
    print()

    lista = fizzbuzz(input_nums["κάτω"], input_nums["πάνω"])
    lista = str(lista)

    lista = lista.strip("[]")       #για να βγάλει τα "[" και "]" από την αρχή και το τέλος
    lista = lista.replace("'", "")  #για να βγάλει τα " ' " από τα Fizz και Buzz
    
    print(lista)
    print('\nΘέλετε να συνεχίσετε ?')
    check=True
    while check:

        w=str(input('\nΠατήστε, Enter: Συνέχεια, q+Enter: Τερματισμός :  \n'))
        if w=='':
            break
        # elif w=='q' or w=='Q':
        elif w.lower() == 'q':# <--- Συνηθίζεται να γίνεται έτσι
            print('\nΓεια σας...\n')
            return False
        else:
            print('\nΠατήσατε λάθος κουμπί, ξαναπροσπαθήστε...')
            continue
    
    return True



restart = True
while restart:
    restart = main()
