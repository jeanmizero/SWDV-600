# 4. Phrase repetition
phrase_in_string = input(" Input your phrase: ")
num_of_repeat = int(input(" How many times should it be repeated?"))

for index in range(num_of_repeat):
    # Display the phrase with line number
    print((index + 1), phrase_in_string)
