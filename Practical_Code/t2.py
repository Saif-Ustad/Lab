code = []

with open("input_code.txt", "r") as file:
    full_code = file.readlines()

for line in full_code:
    code.append(line.strip().split(" "))

intermediate_code = []

macro_check = False

for line in code:
    if line[0] == "MACRO":
        macro_check = True

    if line[0] == "MEND":
        macro_check = False
        continue

    if macro_check:
        continue

    intermediate_code.append(" ".join(line))

print(intermediate_code)