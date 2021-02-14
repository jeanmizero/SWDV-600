# open file
with open("sales_data.csv", "r") as csv_file:
    # read file
    read_doc = csv_file.read()
    read_doc = read_doc.split("\n")
    # remove empty lines
    if " " in read_doc:
        read_doc.remove("")

# search by using input
search_input = input(
    'Search by invoice id (id) or customer last name (lname) ? ')

while search_input not in ["id", "lname"]:
    print("ERROR: You must enter either 'id' for invoice or 'lname' for customer search ")

    search_input = input(
        'Search by invoice id (id) or customer last name (lname) ? ')

search_item = input("Enter your search term: ")

search_count = 0

if search_input == "id":
    for doc in read_doc:
        # Search by ID
        if doc.split(",")[0] == search_item:
            search_count += 1
            print(doc)

    print("{} records found".format(search_count))

else:
    for doc in read_doc:
        # Search by lastname
        if doc.split(",")[2] == search_item:
            search_count += 1
            print(doc)

    print("{} records found".format(search_count))
