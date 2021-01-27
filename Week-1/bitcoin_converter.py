# 2. Bitcoin converter
print(" As of 01/13/21 at 12:08 pm, bitcoin is currently trading at $35652.93 per bitcoin.")
input_bitcoin_string = input(" Enter the bitcoin amount: ")
bitcoin_in_decimal = float(input_bitcoin_string)
# bitcoin to dollars
bitcoin_to_dollars = bitcoin_in_decimal * 35892.24
print(" That is worth", bitcoin_to_dollars, "us dollars")
