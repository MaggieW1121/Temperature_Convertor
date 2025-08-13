# This is a quick component to convert degrees from °C to °F
# for this component, I will not use the tkinter or graphic interface
# I will only programming a component to get the right value of °C and °F
# Function takes in value, does conversion and puts answer into a list

def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit

# Main Routine
temperatures = [0, -160/9, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    # ans_statement = "() °C is () °F".format(item, answer)
    ans_statement = "{} °C is {} °F".format(item, answer)
    converted.append(ans_statement)

print(converted)
