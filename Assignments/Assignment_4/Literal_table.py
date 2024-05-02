def generate_literal_table(source_code):
    literal_table = {}
    current_address = 0

    for line in source_code:
        tokens = line.split()
        for token in tokens:
            if '=' in token:
                literal, value = token.split('=')
                if literal not in literal_table:
                    literal_table[literal] = {'value': value, 'address': current_address}
                    current_address += 1

    return literal_table

def main():
    # Example source code
    source_code = [
        "START 100",
        "LDA =5",
        "STA X",
        "ADD =2",
        "SUB X",
        "END"
    ]

    literal_table = generate_literal_table(source_code)

    print("Literal Table:")
    print("Literal\tValue\tAddress")
    for literal, info in literal_table.items():
        print(f"{literal}\t{info['value']}\t{info['address']}")

if __name__ == "__main__":
    main()

