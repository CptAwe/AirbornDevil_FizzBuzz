def userInput():
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
        
        # Έλεγχος για ορθή λογική εισαγωγής δεδομένων
        if input_nums["κάτω"] > input_nums["πάνω"] :
            print("\nΔεν δώσατε σωστή τιμή...")
            print("\nΠρέπει το πάνω όριο να είναι μεγαλύτερο από το κάτω...")
            input_nums = {}
            continue
        else:
            break
    
    return input_nums


def breakme():
    num = 0

    def infinite():
        # print("hello world")
        # global num
        num += 1
        infinite()

    try:
        # infinite()
        # from translations import infinite
        infinite()
    except:
        print(num)