def to_c(from_f):
    Celsius = (from_f - 32) * 5/9
    return Celsius

# Main Routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} °F is {} °C".format(item, answer)
    converted.append(ans_statement)

print(converted)