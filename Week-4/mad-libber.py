print("Madlib Maker")
name = input("name :")
place = input('place:')
verb = input("verb:")

first_sentence = "Old Mc-{0} had a {1}, E-I-E-I-O".format("name", "place")
first_sentence = first_sentence.replace('name', name)
first_sentence = first_sentence.replace('place', place)
# print(first_sentence)

second_sentence = "And on that {0} he liked to {1}, E-I-E-I-O".format(
    "place", "verb")
second_sentence = second_sentence.replace("place", place)
second_sentence = second_sentence.replace("verb", verb)
# print(second_sentence)

third_sentence = "With a {0} {0} here, and a {0} {0} there, everywhere a {0} {0}".format(
    "verb")
third_sentence = third_sentence.replace("verb", verb, 6)
print(third_sentence)
