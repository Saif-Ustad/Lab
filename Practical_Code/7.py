# Assembly source code with macro definitions
assembly_code = [
    "LOAD J",
    "STORE M",
    "MACRO EST1",
    "LOAD e",
    "ADD d",
    "MEND",
    "MACRO EST ABC",
    "EST1",
    "STORE ABC",
    "MEND",
    "MACRO ADD7 P4, P5, P6",
    "LOAD P5",
    "EST 8",
    "SUB4 2",
    "STORE P4",
    "STORE P6",
    "MEND",
    "EST",
    "ADD7 C4, C5, C6",
    "END",
]

# Step 1: Initialize the MDT and MNT
macro_definition_table = []  # Stores macro content
macro_name_table = {}  # Stores macro names with MDT index reference

current_macro_name = None  # Current macro name being processed
current_macro_start = None  # Starting index of the current macro in MDT

# Step 2: Parse the assembly code to find macro definitions
for line in assembly_code:
    parts = line.split()
    if len(parts) == 0:
        continue

    if parts[0] == "MACRO":
        # Start of a new macro definition
        current_macro_name = parts[1]  # Macro name
        current_macro_start = len(macro_definition_table)  # MDT index
    elif parts[0] == "MEND":
        # End of the macro definition
        if current_macro_name is not None:
            # Add the macro to the MNT
            macro_name_table[current_macro_name] = current_macro_start
            current_macro_name = None
            current_macro_start = None
    else:
        if current_macro_name:
            # Add the macro content to the MDT
            macro_definition_table.append(line)

# Step 3: Display the Macro Name Table (MNT)
print("Macro Name Table (MNT):")
print("Macro Name\tMDT Index")
for macro_name, mdt_index in macro_name_table.items():
    print(f"{macro_name}\t\t{mdt_index}")

# Step 4: Display the Macro Definition Table (MDT)
print("\nMacro Definition Table (MDT):")
print("MDT Index\tInstruction")
for index, instruction in enumerate(macro_definition_table):
    print(f"{index}\t\t{instruction}")
