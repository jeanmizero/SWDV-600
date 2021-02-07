in_file = input("Enter sales file name: ")
out_file = input("Enter name for total sales file:")
# Open file
in_sales = open(in_file, "r")
# Close file
out_sales = open(out_file, "w")

sale_seq = in_sales.readlines()

for sales in sale_seq:
    # Split line by space
    dollars = sales.split(" ")
    # convert values to float by removing '$' symbol at start
    sale1 = float(dollars[0][1:])

    sale2 = float(dollars[1][1:-2])

    total_sales = sale1 + sale2

    print("$%8s $%8s $%8s" % (sale1, sale2, total_sales), file=out_sales)


in_sales.close()
out_sales.close()

print("\nDone writing totals to", out_file)
