name_1 = input("What is ur name? ")
name_2 = input("What is ur name? ")
name_3 = input("What is ur name? ")

Slices_in_the_pizza = input("How many slices in pizza? ")
Price_of_the_pizza = input("What is the price of the pizza? ")

Percentage_ate_by_person_1 = input(name_1 + " What percentage of the pizza u've ate? ")
Percentage_ate_by_person_2 = input(name_2 + " What percentage of the pizza u've ate? ")
Percentage_ate_by_person_3 = input(name_3 + " What percentage of the pizza u've ate? ")

number_of_slices_ate_person_1 = float(Slices_in_the_pizza) * float(Percentage_ate_by_person_1)
number_of_slices_ate_person_2 = float(Slices_in_the_pizza) * float(Percentage_ate_by_person_2)
number_of_slices_ate_person_3 = float(Slices_in_the_pizza) * float(Percentage_ate_by_person_3)

Price_payed_by_name_1 = float(Percentage_ate_by_person_1) * float(Price_of_the_pizza)
Price_payed_by_name_2 = float(Percentage_ate_by_person_2) * float(Price_of_the_pizza)
Price_payed_by_name_3 = float(Percentage_ate_by_person_3) * float(Price_of_the_pizza)

print(name_1 + " have ate " + str(number_of_slices_ate_person_1) + " slices and have paid " + str(
    Price_payed_by_name_1) + "$ for his meal.")
print(name_2 + " have ate " + str(number_of_slices_ate_person_2) + " slices and have paid " + str(
    Price_payed_by_name_2) + "$ for his meal.")
print(name_3 + " have ate " + str(number_of_slices_ate_person_3) + " slices and have paid " + str(
    Price_payed_by_name_3) + "$ for his meal.")
