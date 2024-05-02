# Assembly source code
assembly_code = [
    "START 100",
    "READ A",
    "READ B",
    "MOVER AREG, ='50'",
    "MOVER BREG, ='60'",
    "ADD AREG, BREG",
    "LOOP MOVER CREG, A",
    "ADD CREG, ='10'",
    "COMP CREG, B",
    "BC LT, LOOP",
    "NEXT SUB AREG, ='10'",
    "COMP AREG, B",
    "BC GT, NEXT",
    "STOP",
    "A DS 1",
    "B DS 1",
    "END",
]

# Step 1: Find all literals in the code
literal_pool = []
literal_addresses = {}

# Set an initial memory address (after "START")
current_location_counter = 100

# Process each line to find literals
for line in assembly_code:
    parts = line.split()
    if len(parts) == 0:
        continue

    for part in parts:
        # Check if part is a literal
        if part.startswith("='") and part.endswith("'"):
            literal_value = part
            # If not already in the literal pool, add it
            if literal_value not in literal_pool:
                literal_pool.append(literal_value)

# Step 2: Assign memory addresses to the literals
# Typically, literals are allocated after all other operations and symbols
# Thus, we increment the location counter with instructions
for line in assembly_code:
    # Split the line into components
    parts = line.split()
    
    # Check if it's an instruction or directive
    if parts[0] not in ["START", "STOP", "END"]:
        current_location_counter += 1
    
    # When hitting the END directive, assign literal addresses
    if parts[0] == "END":
        # Literals typically start after all other instructions and symbols
        for literal in literal_pool:
            if literal not in literal_addresses:
                literal_addresses[literal] = current_location_counter
                current_location_counter += 1

# Display the literal table
print("Literal Table:")
print("Literal\tAddress")
for literal, address in literal_addresses.items():
    print(f"{literal}\t{address}")
