# Assembly code with macro definitions
assembly_code = [
    "LOAD A",
    "MACRO ABC",
    "LOAD p",
    "SUB q",
    "MEND",
    "STORE B",
    "MULT D",
    "MACRO ADD1 ARG",
    "LOAD X",
    "STORE ARG",
    "MEND",
    "LOAD B",
    "MACRO ADD5 A1, A2, A3",
    "STORE A2",
    "ADD1 5",
    "ADD1 10",
    "LOAD A1",
    "LOAD A3",
    "MEND",
    "ADD1 t",
    "ABC",
    "ADD5 D1, D2, D3",
    "END",
]

# Step 1: Parse macro definitions into a macro table
macro_table = {}
current_macro_name = None
current_macro_body = []

for line in assembly_code:
    parts = line.split()
    if len(parts) == 0:
        continue

    if parts[0] == "MACRO":
        # Start of a macro definition
        current_macro_name = parts[1]
        current_macro_body = []
    elif parts[0] == "MEND":
        # End of a macro definition
        if current_macro_name:
            macro_table[current_macro_name] = current_macro_body.copy()
        current_macro_name = None
        current_macro_body = []
    else:
        if current_macro_name:
            # Add lines to the current macro body
            current_macro_body.append(line)

# Step 2: Generate intermediate code with macro expansion
intermediate_code = []

for line in assembly_code:
    parts = line.split()
    if len(parts) == 0:
        continue

    first_word = parts[0]

    if first_word == "MACRO" or first_word == "MEND":
        # Skip macro definitions for intermediate code
        continue

    if first_word in macro_table:
        # Expand macro calls with their body code
        macro_body = macro_table[first_word]
        # Replace macro parameters if provided
        macro_arguments = parts[1:] if len(parts) > 1 else []
        
        for macro_line in macro_body:
            expanded_line = macro_line
            for idx, arg in enumerate(macro_arguments):
                expanded_line = expanded_line.replace(f"{chr(112 + idx)}", arg)
            intermediate_code.append(expanded_line)
    else:
        # If not a macro call, add the line directly
        intermediate_code.append(line)

# Display the intermediate code
print("Intermediate Code:")
for code_line in intermediate_code:
    print(code_line)
