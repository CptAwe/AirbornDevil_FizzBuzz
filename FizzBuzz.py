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

# Αλλαξε τα F και B για να αλλάξουν τα Fizz Buzz του παιχνιδιού
F=3
B=5


def FizzBuzz(start, end):
    """
    Plays the game Fizzbuzz and returns a list of the results.
    It does NOT make any sanity checks.
    """
    output = []
    for i in range(x_start,x_end+1):
        if i==0:
            # lista += " "+str(i)+" , "
            output.append(i)
        elif i%F==0 and i%B==0 :
            # lista+=" FizzBuzz "+" , "
            output.append("FizzBuzz")
        elif i%F==0 :
            # lista +=" Fizz "+" , "
            output.append("Fizz")
        elif i%B==0:
            # lista +=" Buzz "+" , "
            output.append("Buzz")
        else:
            # lista += " "+str(i)+" "+" , "
            output.append(i)
    
    return output

main=True
while main:
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # Για να ξεχωρίζει η κάθε επανάληψη
    print("\nΚαλώς ήρθατε στο FizzBuzz !!!")
    print("\nΘα πρέπει να μου δώσετε τα όρια των αριθμών που θα ελέγξω...")

    """
    [GeoPap]
    Αυτό το while-try-except είναι πάρα πολύ βολικό, αλλά το γράφεις δύο φορές και είναι αμαρτία
    """

    while True:
        input_nums = {
            "κάτω" : None,
            "πάνω" : None
        }
        for i in input_nums:
            while True:
                try:
                    input_number = int(
                        input('\nΔώστε μου έναν ακέραιο αριθμό για το {which} όριο : '.format(which = i))
                    )
                except ValueError:
                    print('\nΔεν δώσατε σωστή τιμή...')
                    continue
                
                # Επιτυχής εισαγωγή
                input_nums[i] = input_number
                break

        if input_nums["κάτω"] > input_nums["πάνω"] :
            print("\nΔεν δώσατε σωστή τιμή...")
            print("\nΠρέπει το πάνω όριο να είναι μεγαλύτερο από το κάτω...")
            input_nums = {}
            continue
        else:
            break
    
    x_start = input_nums["κάτω"]
    x_end = input_nums["πάνω"]
    print()

    lista = FizzBuzz(x_start, x_end)
    lista = str(lista)

    lista = lista.strip("[]")       #για να βγάλει τα "[" και "]" από την αρχή
    lista = lista.replace("'", "")  #για να βγάλει τα " ' " από τα Fizz και Buzz
    # lista=lista.lstrip(" ")    #για να βγάλει το " "  από την αρχή.  
    # lista=lista.rstrip(", ")   #για να βγάλει το " , " από το τέλος.
    print(lista)
    print('\nΘέλετε να συνεχίσετε ?')
    check=True
    while check:

        w=str(input('\nΠατήστε, Enter: Συνέχεια,  \
q+Enter: Τερματισμός :  \n'))
        if w=='':
            break
        elif w=='q' or w=='Q':
            main=False
            print('\nΓεια σας...\n')
            break
        else:
            print('\nΠατήσατε λάθος κουμπί, ξαναπροσπαθήστε...')
            continue



