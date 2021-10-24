class Budget_App():
    def __init__(budget, food, clothing, entertainment):
        budget.food = food
        budget.clothing = clothing
        budget.entertainment = entertainment

    def balance(budget, food, clothing, entertainment):
        balance_deposit = food + clothing + entertainment
        return f" Your total balance is: {balance_deposit}"

    def __repr__(budget):
        return f"{budget.food} food, {budget.clothing} clothing, {budget.entertainment} entertainment"

    def food_balance(budget, food):
        food_deposit = food
        return f" Your food balance is: {food_deposit}"
        
    def clothing_balance(budget, clothing):
        clothing_deposit = clothing
        return f" Your clothing balance is: {clothing_deposit}"
    
    def entertainment_balance(budget, entertainment ):
        entertainment_deposit = entertainment
        return f" Your entertainment balance is: {entertainment_deposit}"
        

food = int(input("Your food budget: "))
clothing = int(input("Your clothing budget: "))
entertainment = int(input("Your entertainment budget: "))


budget1 = Budget_App("Potato", "Jeans", "TV")
budget2 = Budget_App("Orange", "Socks", "Movie")


print(budget1.food_balance(food))
print(budget1.clothing_balance(clothing))
print(budget1.entertainment_balance(entertainment))
print(budget1.balance(food, clothing, entertainment))

file1 = open('food.txt', 'r')
foodfile = file1.readline()
file1.close()
foodfile_int = int(foodfile)

food_total = foodfile_int + food 

file1 = open('food.txt', 'w')
file1.write(str(food_total))
file1.close()

file2 = open('clothing.txt', 'r')
clothingfile = file2.readline()
file2.close()
clothing_int = int(clothingfile)

clothing_total = clothing_int + clothing

file2 = open('clothing.txt', 'w')
file2.write(str(clothing_total))
file2.close()

file3 = open('entertainment.txt', 'r')
entertainmentfile = file3.readline()
file3.close()
entertainment_int = int(entertainmentfile)

entertainment_total = entertainment_int + entertainment

file3 = open('entertainment.txt', 'w')
file3.write(str(entertainment_total))
file3.close()



