class Assembler:
    def __init__(self):
        self.symbol_table = {}
        self.literal_table = {}
        self.pool_table = []

    def pass_one(self, source_code):
        lines = source_code.split('\n')
        location_counter = 0
        pool_index = 0

        for line in lines:
            tokens = line.split()
            if len(tokens) == 0:
                continue
            if tokens[0] == 'START':
                location_counter = int(tokens[1])
                continue
            if tokens[0] == 'END':
                break
            if tokens[1] == 'LT':
                self.pool_table.append(tokens[0])
            else:
                self.symbol_table[tokens[0]] = location_counter
                location_counter += 1

    def pass_two(self, source_code):
        lines = source_code.split('\n')
        location_counter = 0

        intermediate_code = []

        for line in lines:
            tokens = line.split()
            if len(tokens) == 0:
                continue
            if tokens[0] == 'START':
                location_counter = int(tokens[1])
                continue
            if tokens[0] == 'END':
                break
            if tokens[1] == 'LT':
                continue
            if tokens[1] == 'DS' or tokens[1] == 'DC':
                location_counter += int(tokens[2])
            else:
                intermediate_code.append(f"{location_counter} ({tokens[1]}, {tokens[0]})")
                location_counter += 1

        return intermediate_code

if __name__ == "__main__":
    assembler = Assembler()
    source_code = """
    START 100
    MOV A, 10
    ADD B, A
    LT 5
    DS C, 1
    END
    """
    assembler.pass_one(source_code)
    intermediate_code = assembler.pass_two(source_code)

    print("Intermediate Code:")
    for code in intermediate_code:
        print(code)
