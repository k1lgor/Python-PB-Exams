cash = float(input())
gender = str(input())
age = int(input())
sport = str(input())
if sport == 'Gym':
    if gender == 'm':
        if age <= 19:
            if cash >= 42 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(42 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 42:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(42 - cash):.2f} more.")
    elif gender == 'f':
        if age <= 19:
            if cash >= 35 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(35 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 35:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(35 - cash):.2f} more.")
elif sport == 'Boxing':
    if gender == 'm':
        if age <= 19:
            if cash >= 41 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(41 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 41:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(41 - cash):.2f} more.")
    elif gender == 'f':
        if age <= 19:
            if cash >= 37 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(37 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 37:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(37 - cash):.2f} more.")
elif sport == 'Yoga':
    if gender == 'm':
        if age <= 19:
           if cash >= 45 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
           else:
                print(f"You don't have enough money! You need ${(45 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 45:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(45 - cash):.2f} more.")
    elif gender == 'f':
        if age <= 19:
            if cash >= 42 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(42 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 42:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(42 - cash):.2f} more.")
elif sport == 'Zumba':
    if gender == 'm':
        if age <= 19:
            if cash >= 34 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(34 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 34:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(34 - cash):.2f} more.")
    elif gender == 'f':
        if age <= 19:
            if cash >= 31 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(31 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 31:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(31 - cash):.2f} more.")
elif sport == 'Dances':
    if gender == 'm':
        if age <= 19:
            if cash >= 51 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(51 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 51:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(51 - cash):.2f} more.")
    elif gender == 'f':
        if age <= 19:
            if cash >= 53 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(53 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 53:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(53 - cash):.2f} more.")
elif sport == 'Pilates':
    if gender == 'm':
        if age <= 19:
            if cash >= 39 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(39 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 39:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(39 - cash):.2f} more.")
    elif gender == 'f':
        if age <= 19:
            if cash >= 37 * 0.8:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(37 * 0.8 - cash):.2f} more.")
        else:
            cash = cash
            if cash >= 37:
                print(f"You purchased a 1 month pass for {sport}.")
            else:
                print(f"You don't have enough money! You need ${(37 - cash):.2f} more.")
