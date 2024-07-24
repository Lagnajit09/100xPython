from data import MENU, resources


def calculate_money(pennies, quarters, nickles, dimes):
    return (pennies * 0.01) + (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05)


def compare_resources(ingredients, available_resources):
    for item in ingredients:
        if available_resources[item] <= ingredients[item]:
            return False
    return True


def ask_money():
    print("\nPlease insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    return calculate_money(pennies, quarters, nickles, dimes)


def print_report(available_resources):
    for item in available_resources:
        if item == 'milk' or item == 'water':
            print(f"{item}: {available_resources[item]}ml")
        elif item == 'coffee':
            print(f"{item}: {available_resources[item]}g")
        else:
            print(f"{item}: ${available_resources[item]}")


should_off = False
available_resources = resources
available_resources["money"] = 0

while not should_off:
    user_order = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if user_order == 'report':
        print_report(available_resources)
    elif user_order == 'off':
        should_off = True
    elif user_order == 'espresso' or user_order == 'latte' or user_order == 'cappuccino':
        is_possible = compare_resources(MENU[user_order]["ingredients"], available_resources)

        money = ask_money()
        change = money - MENU[user_order]["cost"]

        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is ${change} in change.")
            available_resources["money"] = MENU[user_order]["cost"]
            for item in MENU[user_order]["ingredients"]:
                available_resources[item] = available_resources[item] - MENU[user_order]["ingredients"][item]
            print(f"Here is your {user_order}🍵")
