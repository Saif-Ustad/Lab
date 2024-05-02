assembly_code = []

mnemonics = {
    'STOP': ('IS', '00'),
    'ADD': ('IS', '01'),
    'SUB': ('IS', '02'),
    'MUL': ('IS', '03'),
    'MOVER': ('IS', '04'),
    'MOVEM': ('IS', '05'),
    'COMP': ('IS', '06'),
    'BC': ('IS', '07'),
    'DIV': ('IS', '08'),
    'READ': ('IS', '09'),
    'PRINT': ('IS', '10'),
    'LTORG': ('AD', '05'),
    'ORIGIN': ('AD', '03'),
    'START': ('AD', '01'),
    'EQU': ('AD', '04'),
    'DS': ('DL', '01'),
    'DC': ('DL', '02'),
    'END': ('AD', '02'),
    'AREG': ('RG', '01'),
    'BREG': ('RG', '02'),
    'CREG': ('RG', '03'),
    'EQ': ('CC', '01'),
    'NE': ('CC', '02'),
    'LT': ('CC', '03'),
    'GT': ('CC', '04'),
    'LE': ('CC', '05'),
    'GE': ('CC', '06'),
    'ANY': ('CC', '07')
}


with open("input_code.txt", "r") as file:
    assembly = file.readlines()

for i in assembly:
    assembly_code.append(i.strip().split())

lc = int(assembly_code[0][1])

symbol_table = {}
literal_table = []
pool_table = []
p_v = 0
literal_temp = []

for i in range(1, len(assembly_code)):
    if assembly_code[i][0] not in mnemonics:
        symbol_table[assembly_code[i][0]] = lc

    if "=" in assembly_code[i][-1]:
        if assembly_code[i][-1] not in literal_temp:
            literal_temp.append(assembly_code[i][-1].replace("â€™", ""))

    if assembly_code[i][0] == "LTORG" or assembly_code[i][0] == "END":
        temp = {}
        for i in literal_temp:
            temp[i] = lc
            lc += 1
        literal_temp = []

        literal_table.append(temp)

        if len(temp) > 0:
            pool_table.append(p_v)

            p_v += len(temp)

    else:
        lc += 1

print(symbol_table)
print(literal_table)
print(pool_table)

intermediate_code = []
c_l = 0

for line in assembly_code:
    if line[0] == "LTORG":
        c_l += 1
    a = []
    for token in line:
        token = token.strip().replace(",", "")
        if token in mnemonics:
            a.append(mnemonics[token])

        elif token in symbol_table:
            a.append(("S", list(symbol_table.keys()).index(token)))

        elif token in literal_table[c_l]:
            a.append(("L", list(literal_table[c_l].keys()).index(token)))

        elif token.isdigit():
            a.append(("C", token))

    intermediate_code.append(a)

print(intermediate_code)