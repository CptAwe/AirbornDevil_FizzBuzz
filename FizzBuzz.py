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
    lista=" "
    # [GeoPap] Τις μεταβλητές που ίσως θέλουμε να αλλάζουμε στο μέλλον,
    # ανάλογα με την περίσταση, συνηθίζεται να τις βάζουμε πάνω πάνω στο
    # πρόγραμμα, για να τις βρίσκουμε εύκολα.
    # Αλλαξε τα F και B για να αλλάξουν τα Fizz Buzz του παιχνιδιού
    # F=3
    # B=5
    #----------------------------------------------------------------     
    for i in range(x_start,x_end+1):

        if i==0:
            lista += " "+str(i)+" , "
        elif i%F==0 and i%B==0 :
            lista+=" FizzBuzz "+" , "
            #print("FizzBuzz")
        elif i%F==0 :
            lista +=" Fizz "+" , "
            #print("Fizz")
        elif i%B==0:
            lista +=" Buzz "+" , "
            #print("Buzz")
        else:
            lista += " "+str(i)+" "+" , "
            #print(i)

    lista=lista.lstrip(" ")    #για να βγάλει το " "  από την αρχή.  
    lista=lista.rstrip(", ")   #για να βγάλει το " , " από το τέλος.
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