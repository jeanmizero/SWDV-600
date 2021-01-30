# accumulation algorithms factorials
number_of_scoops = int(input("Enter the number of scoops: "))
total_scoop_orderings = 1
for scoop_choice_left in range(number_of_scoops, 0, -1):
    total_scoop_orderings = total_scoop_orderings * scoop_choice_left
print(total_scoop_orderings)
