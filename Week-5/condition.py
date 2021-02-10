km_value = float(input('Enter the distance in km: '))

if km_value >= 0:
    miles_value = km_value / 1.609
    print("{0:0.2f} km is the same as {1:0.2f} mi ".format(km_value, miles_value ))
else:   
#if km_value < 0:
    print("You cannot enter negative value")
print("Thanks for converting!")
