# Assembly code with macros
assembly_code = [
    "LOAD J",
    "STORE M",
    "MACRO EST",
    "LOAD e",
    "ADD d",
    "MEND",
    "LOAD S",
    "MACRO SUB4 ABC",
    "LOAD U",
    "STORE ABC",
    "MEND",
    "LOAD P",
    "ADD V",
    "MACRO ADD7 P4, P5, P6",
    "LOAD P5",
    "SUB4 XYZ",
    "SUB 8",
    "SUB 2",
    "STORE P4",
    "STORE P6",
    "MEND",
    "EST",
    "ADD7 C4, C5, C6",
    "SUB4 z",
    "END",
]

# Step 1: Define the macro table to store macro definitions
macro_table = {}
current_macro_name = None
current_macro_body = []

# Parse the assembly code to find macro definitions
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
            # Add the code line to the current macro body
            current_macro_body.append(line)

# Step 2: Generate the intermediate code with macro expansion
intermediate_code = []

for line in assembly_code:
    parts = line.split()
    if len(parts) == 0:
        continue

    first_word = parts[0]

    if first_word in ["MACRO", "MEND"]:
        # Skip macro definition lines for intermediate code
        continue

    if first_word in macro_table:
        # Expand the macro call with the macro body
        macro_body = macro_table[first_word]
        macro_args = parts[1:] if len(parts) > 1 else []
        
        # Replace parameters in the macro body
        for macro_line in macro_body:
            expanded_line = macro_line
            # Replace parameters with given arguments
            for idx, arg in enumerate(macro_args):
                # Replace placeholders like `p`, `q`, etc., with actual arguments
                placeholder = f"{chr(97 + idx)}"  # 97 is ASCII 'a', thus `a`, `b`, `c`, etc.
                expanded_line = expanded_line.replace(placeholder, arg)

            intermediate_code.append(expanded_line)
    else:
        # If not a macro call, add the line directly
        intermediate_code.append(line)

# Output the intermediate code
print("Intermediate Code:")
for code_line in intermediate_code:
    print(code_line)
