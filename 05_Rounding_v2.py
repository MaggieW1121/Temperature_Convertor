# Compare to version 1, this function works as what I expected

# Check the number use modulo operator (%)
# Display output using the formatting string function

to_round = [1, 1/1, 1/2, 1/3]
print("**** Numbers to round ****")
print(to_round)

print()
print("**** Rounded Numbers ****")

for item in to_round:
    if item%1 == 0:
        print("{:.0f}".format(item))
    else:
        print("{:.1f}".format(item))
