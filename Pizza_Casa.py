#Dictionaries for pizza types and toppings
pizza_type = {'DEEP-DISH' : 29, 'NEW-YORK STYLE': 25, 'MARGERITA': 22, 'PESTO ITALIAN': 26, 'BLACK HAM': 24, 'VEGGIE DELUXE': 23, 'BBQ CHICKEN' : 26}
pizza_topping = {'PINEAPPLE': 0.50, 'BLACK OLIVES': 1, 'TOMATO': 1, 'ONION' : 0.75, 'PESTO': 1.25, 'FETA CHEESE' : 2, 'RED PEPPER': 1.5, 'GREEN PEPPER': 1.5, 'MUSHROOM': 1, 'JALEPENOS': 1.75}

#Empty list for toppings 
topping = [], 

#Empty dictionary for storing all the pizza orders with their total price
pizza_order = dict()

#Initialisation
continue_toppings = 'yes'
continue_order = 'yes'
flag = True

#Empty list for toppings
topping = [], 

#Empty dictionary for storing all the pizza orders with their total price
pizza_order = dict()

#Welcome message
print('******************WELCOME TO PIZZA CASA!!******************\n')
print('\nPIZZA TYPES:\n')

#While loop for running program continuously until user enters no to end it
while (continue_order == 'yes'):
#Pizza
    #Pizza options
    for pizza, price in pizza_type.items():
        print('{}: ${}'.format(pizza, price))
    
    #Input question for the type of pizza
    pizzaType_choice = input('\nWHICH PIZZA WOULD YOU LIKE TO ORDER?\n').upper()
    
    #If statement for when the input is CANCEL
    #Ends the program/order
    if (pizzaType_choice == 'CANCEL'):
        continue_order = 'no'
    
    #If statement to check for a valid pizza choice and if the input is CANCEL
    elif (pizzaType_choice not in pizza_type.keys() and pizzaType_choice != 'CANCEL'):
        print('\nINVALID CHOICE. PLEASE CHOOSE A PIZZA FROM THE LIST or ENTER cancel IF DO NOT WANT TO ORDER\n') #Message for when an invalid pizza choice is entered and the input isn't CANCEL
            
    else:
        pizza_price = pizza_type[pizzaType_choice]
        
    #Toppings
        #Toppings message
        print('\nAVAILABLE TOPPINGS:\n')
        
        #Topping options
        for toppings, cost in pizza_topping.items():
            print('{}: ${}'.format(toppings, cost))
        
        #Redifining list for when the user orders the pizza again
        #Stores all the toppings selected by the user
        topping = []
        
        #While loop for asking for toppings until user enters done
        while (continue_toppings == 'yes'):
            
            #Input question for toppings
            pizzaTopping_choice = input('\nWHICH TOPPINGS WOULD YOU LIKE TO HAVE ON YOUR PIZZA? ENTER done WHEN DONE CHOOSING TOPPINGS\n').upper()
            
            #If statement to check if a valid topping has been entered or not
            if ((pizzaTopping_choice != 'DONE') and (pizzaTopping_choice not in pizza_topping.keys())):
                print('INVALID CHOICE. CHOOSE A TOPPING FROM THE LIST\n') #Message for when an invalid topping is entered
            
            #elif statement for when user enters done
            elif (pizzaTopping_choice == 'DONE'):
                continue_toppings = 'no' 
                flag = True
                
            #else statement for appending the toppings list with toppings until the user enters done
            else:
                topping.append(pizza_topping[pizzaTopping_choice])

    #Continue order
        #While loop for asking the user if they want too continue ordering or not
        while(flag == True):
            
            #Input question for continuing order
            continue_order = input('\nWOULD YOU LIKE TO CONTINUE ORDERING? PLEASE ANSWER USING yes OR no\n').lower()
            
            #If statement for when the input is not yes or not(invalid input)
            if(continue_order !='yes' and continue_order != 'no'):
                print('PLEASE ENTER A VALID CHOICE') #Message for when an invalid choice is entered
                
            #Else statement for when the user wants to continue ordering
            #Stores the total price (Base price +  all the topping prices combines) for the pizza that was ordered
            else:
                continue_toppings = 'yes'
                flag = False
                topping_total = float(sum(topping)) #Calculates the price of all the toppings combined
                
                #Calculates the total cost of the pizza when the pizza is a new pizza
                if (pizzaType_choice not in pizza_order.keys()):
                    pizza_order[pizzaType_choice] = float(topping_total + pizza_price)
                 
                #Calculates the total cost of the pizza when there is already a same pizza type in the pizza order dictionary
                #Updates the cost of the pizza that was already in the pizza order dictionary
                else:
                    update_bill = pizza_order[pizzaType_choice] + float(topping_total + pizza_price)
                    pizza_order[pizzaType_choice] = update_bill
                
#Bill   
#If statement for when user says no to continuing the order
if (continue_order == 'no' and pizza_order != dict()) :
    total_bill = sum(pizza_order.values())
    print('\nYOUR BILL:\n')
    
    #For loop for printing the pizzas, their prices and the final cost
    for pizzas, total in pizza_order.items():
        print('pizza: {}  price: ${}'.format(pizzas, total))
    print('\nTOTAL COST: ${}'.format(total_bill))

#Goodbye message
print('~~~~~~~~~~~~~~~~~~~~~~~THANKS FOR STOPPING BY PIZZA CASA. WE HOPE TO SEE YOU AGAIN 👋:)~~~~~~~~~~~~~~~~~~~~~~~')
