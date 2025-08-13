# From the previous degrees convertor, there's an issue that
# the degrees are not rounded nicely

# With this component, the decimals are expected to round to 1dp. The integers are expected to be displayed in 0dp.

#number = int(input("Enter an integer: "))

to_round = [1, 1/1, 1/2, 1/3]
print("**** Numbers to round ****")
print(to_round)

print()
print("**** Rounded Numbers ****")

for item in to_round:
    print(int(item))