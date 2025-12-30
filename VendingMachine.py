from DataItems import coins, usr, items_equipment, items_food

print('Hello Traveler! Welcome to the Medieval Vending Machine.')
input_ask = input('Can i help you with something today? (I want to buy something/No thanks, maybe next time):').strip().lower()
if input_ask in ("I want", 'i want', 'y', 'Y', 'yes', 'Yes', 'I want to buy something'):
    print('Great! Let me assist you with that.')
else:
    print('Okay then, have a nice day Traveler! See ya!')
    exit()

print('For the first, let me know how much coins you have.')
input_answer = input('Can you please tell me how much coins you have? (Yes/No): ').strip().lower()
if input_answer in ('yes', 'y'):
    print('Oh thanks, let me check...')
    print('You have', coins, 'coins.')
else:
    print('Alright, maybe next time. See ya!')
    exit()

while True:
    print('Then, what would you like to buy today? In here, we have Equipment and Food items.')
    choice_category_item = input('What category would you like to choose? (Equipment/Food/Exit):')
    if choice_category_item == 'Equipment':
        print('Sure! Here the availabe Equipment Items that we have:')
        for key, item in items_equipment.items():
            print(f'{key}: {item.name} - {item.price}')
        selection = input('Select the number of the item you want to buy, Traveler:').strip()
        if selection in items_equipment:
            selected_item = items_equipment[selection]
            print('You have selected:', selected_item.name, ', it will cost you', selected_item.price)
            if usr.coins >= selected_item.price:
                usr.coins -= selected_item.price
                print('Thank you for your purchase! Now, you have', usr.coins, 'coins left.')
            else:
                print('Sorry, your coins are not enough for this item')
        else:
            print('Invalid selection. Please choose a valid item number.')
            continue

    elif choice_category_item == 'Food':
        print('Sure! Here the availabe Food Items that we have:')
        for key, item in items_food.items():
            print(f'{key}: {item.name} - {item.price}')
        selection = input('Select the number of the item you want to buy, Traveler:').strip()
        if selection in items_food:
            selected_item = items_food[selection]
            print('You have selected', selected_item.name, ', it will cost you', selected_item.price)
            if usr.coins >= selected_item.price:
                usr.coins -= selected_item.price
                print('Thank you for your purchase! Now, you have', usr.coins, 'coins left')
            else:
                print('Sorry, your coins are not enough for this item')
        else:
            print('Invalid selection. Please choose a valid item number.')
            continue
    elif choice_category_item == 'Exit':
        print('Thank you for visiting the Medieval Vending Machine. See you next time, Traveler!')
        break
    else:
        print('Please choose a valid category: Equipment, Food, or Exit.')
        continue