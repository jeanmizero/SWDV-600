# Indefinite we use WHILE LOOP
number_of_words = 0
count_of_es = 0
total_length_of_inputs = 0

should_continue = "y"

while should_continue == "y":
    number_of_words = number_of_words + 1
    input_word = input("Enter word{0}: ".format(number_of_words))
    count_of_es = count_of_es + input_word.count("e")
    total_length_of_inputs = total_length_of_inputs + len(input_word)

    should_continue = input("Do you want continue (y/n)")

print('Total e\'s seen', count_of_es)
print('Pct of e\'s:{:0.2}%'.format(count_of_es / total_length_of_inputs))
print('Average e\'s seen:{:0.2}'.format(count_of_es / number_of_words))
