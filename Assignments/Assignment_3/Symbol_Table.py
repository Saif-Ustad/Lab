def get_class(operator):
    for i in EMOT:
        if i[0] == operator:
            return i[1]
    return 0

EMOT = [['STOP', 1, 0], ['ADD', 1, 1], ['SUB', 1, 2], ['MULT', 1, 3], ['MOVER', 1, 4],
        ['MOVEM', 1, 5], ['COMP', 1, 6], ['BC', 1, 7], ['DIV', 1, 8], ['READ', 1, 9],
        ['PRINT', 1, 10], ['START', 3, 1], ['END', 3, 2], ['ORIGIN', 3, 3], ['EQU', 3, 4],
        ['LTORG', 3, 5], ['DS', 2, 1], ['DC', 2, 2], ['AREG', 4, 1], ['BREG', 4, 2],
        ['CREG', 4, 3], ['DREG', 4, 4]]

with open("ASSEMBLY CODE.txt", "r") as file:
    lines = file.readlines()

tokens = [line.split() for line in lines]
lc = int(tokens[0][-1])
lc_list = [lc] * len(tokens)

symbol_table = []

for i in range(len(tokens)):
    if len(tokens[i]) == 4:
        label = tokens[i][0]
        if label not in [entry[0] for entry in symbol_table]:
            lc = lc_list[i]
            symbol_table.append([label, lc])
        symbol = tokens[i][-1]
        if symbol[0] != '=' and symbol not in [entry[0] for entry in symbol_table]:
            symbol_table.append([symbol, 0])

        if 'DS' in tokens[i] or 'DC' in tokens[i]:
            operator = tokens[i][2] if 'DS' in tokens[i] else tokens[i][1]
        else:
            operator = tokens[i][1]

        if operator == 'DS':
            incr = int(tokens[i][-1])
            for entry in symbol_table:
                if entry[0] == symbol:
                    entry[1] = lc
        elif operator in ['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC', 'DIV', 'READ', 'PRINT']:
            lc += 1
        else:
            pass

for entry in symbol_table:
    print(entry)


