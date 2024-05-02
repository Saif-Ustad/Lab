# Assembly source code input
assembly_code = [
    "START 180",
    "READ M",
    "READ N",
    "LOOP MOVER AREG, M",
    "MOVER BREG, N",
    "COMP BREG, ='200'",
    "BC GT, LOOP",
    "BACK SUB AREG, M",
    "COMP AREG, ='500'",
    "BC LT, BACK",
    "STOP",
    "M DS 1",
    "N DS 1",
    "END",
]

# Step 1: First Pass - Build the symbol table
symbol_table = {}
current_location_counter = 0  # Initialize the location counter

# Process the code line by line
for line in assembly_code:
    # Split the line into its components
    parts = line.split()
    if len(parts) == 0:
        continue

    # Extract the first component to check for symbols
    first_word = parts[0]

    # If it's a known directive to set the start address
    if first_word == "START":
        if len(parts) > 1:
            current_location_counter = int(parts[1])
        continue  # No symbol to record for START

    # If the first word is an instruction or directive that doesn't require a symbol
    if first_word in ["READ", "MOVER", "COMP", "BC", "SUB", "STOP", "END"]:
        # Increment location counter for each instruction/operation
        current_location_counter += 1
        continue

    # If the first word is not in the above lists, it's considered a symbol
    if first_word not in symbol_table:
        # Record the symbol with the current location counter
        symbol_table[first_word] = current_location_counter

    # If the first word is a directive for memory declaration
    if parts[1] in ["DS"]:
        current_location_counter += int(parts[2])  # DS means declare storage

# Output the symbol table
print("Symbol Table:")
print("Symbol\tAddress")
for symbol, address in symbol_table.items():
    print(f"{symbol}\t{address}")
