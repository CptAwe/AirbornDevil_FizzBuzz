import numpy as np
'''
Program FizzBuzz
by AirbornDevil

Σε ένα σύνολο από ακέραιους αριθμούς ελέγχουμε έναν έναν τους αριθμούς.
Αν ο αριθμός διαιρείται τέλεια με το 3, τότε εμφανίζουμε Fizz.
Αν ο αριθμός διαιρείται τέλεια με το 5, τότε εμφανίζουμε Buzz.
Αν διαιρείται τέλεια και με τους δύο, τότε εμφανίζουμε FizzBuzz.
Σε κάθε άλλη περίπτωση εμφανίζουμε τον αριθμό.
'''

#---------------------------------------------------------------------------------------
#driver
main=True
while main:
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # Για να ξεχωρίζει η κάθε επανάληψη
    print("\nΚαλώς ήρθατε στο FizzBuzz !!!")
    print("\nΘα πρέπει να μου δώσετε τα όρια των αριθμών που θα ελέγξω...")
    while True:
        try:
            x_start=int(input('\nΔώστε μου έναν ακέραιο αριθμό για το κάτω όριο : '))
        except ValueError:
            print('\nΔεν δώσατε σωστή τιμή...')
            continue
        else:
            while True:
                try:
                    x_end=int(input('\nΔώστε μου έναν ακέραιο για το πάνω όριο : '))
                except ValueError:
                    print('\nΔεν δώσατε σωστή τιμή...')
                    continue
                else:
                    if x_start > x_end :
                        print("\nΔεν δώσατε σωστή τιμή...")
                        print("\nΠρέπει το πάνω όριο να είναι μεγαλύτερο από το κάτω...")
                        continue
                    else:
                        break
            break

    print()
    lista=" " 
    # Αλλαξε τα n και m για να αλλάξουν τα Fizz Buzz του παιχνιδιού
    n=3
    m=5 
    #----------------------------------------------------------------     
    for i in range(x_start,x_end+1):

        if i==0:
            lista += " "+str(i)+" , "
        elif i%n==0 and i%m==0 :
            lista+=" FizzBuzz "+" , "
            #print("FizzBuzz")
        elif i%n==0 :
            lista +=" Fizz "+" , "
            #print("Fizz")
        elif i%m==0:
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