# Sample assembly source code
assembly_code = [
    "START 100",
    "READ A",
    "READ B",
    "MOVER AREG, A",
    "SUB AREG, B",
    "STOP",
    "A DS 1",
    "B DS 1",
    "END",
]

# Define opcodes and register mapping for intermediate representation
opcodes = {
    "START": "01",
    "READ": "02",
    "MOVER": "03",
    "SUB": "04",
    "STOP": "05",
}

registers = {
    "AREG": "0",
    "BREG": "1",
    "CREG": "2",
    "DREG": "3",
}

# Step 1: Generate a symbol table
symbol_table = {}
current_location_counter = 100

for line in assembly_code:
    parts = line.split()
    if len(parts) == 0:
        continue

    # First part can be a label or instruction
    first_word = parts[0]
    if first_word == "START":
        if len(parts) > 1:
            current_location_counter = int(parts[1])
        continue
    
    if first_word not in opcodes:
        # It's a label, so add it to the symbol table
        symbol_table[first_word] = current_location_counter
        continue

    # Increment location counter for each operation
    current_location_counter += 1

# Step 2: Generate intermediate code
intermediate_code = []

for line in assembly_code:
    parts = line.split()
    if len(parts) == 0:
        continue

    first_word = parts[0]
    
    # If it's a label or symbol definition, skip generating code
    if first_word in symbol_table:
        continue

    # Get the opcode
    opcode = opcodes.get(first_word, "??")
    
    # Intermediate code entry
    code = {
        "opcode": opcode,
        "operands": []
    }

    # If there's an operand
    if len(parts) > 1:
        # Handle operands, checking for register or symbol
        for operand in parts[1:]:
            # Handle register operands
            if operand in registers:
                code["operands"].append(registers[operand])
            elif operand in symbol_table:
                code["operands"].append(str(symbol_table[operand]))
            else:
                code["operands"].append(operand)
    
    intermediate_code.append(code)

# Display the intermediate code
print("Intermediate Code:")
for entry in intermediate_code:
    operand_str = ", ".join(entry["operands"])
    print(f"{entry['opcode']} {operand_str}")
