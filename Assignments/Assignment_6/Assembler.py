class Assembler:
	def __init__(self):
		self.symbol_table = {}
		self.literal_table = {}
		self.pool_table = []
		self.intermediate_code = []
		
	def pass_one(self, source_code):
		lines = source_code.split('\n')
		location_counter = 0
		pool_index = 0
		
		for line in lines:
			tokens = line.split()
			if len(tokens)==0:
				continue
			if tokens[0]=='START':
				location_counter = int(tokens[1])
				self.intermediate_code.append(f"{location_counter} (AD,01)  (C, (C, {tokens[1]})")
				continue
			if tokens[0]=="END":
				self.intermediate_code.append(f"{location_counter} (AD, 02)")
				break
			if tokens[0] == "LTORG":
				self.intermediate_code.append(f"{location_counter} (AD, 03)")
				for i in range(pool_index, len(self.pool_table)):
					self.literal_table[self.pool_table[i]] = location_counter
					location_counter+=1
				self.pool_table = []
				pool_index = len(self.literal_table)
				continue
			if tokens[1] == 'DS':
				self.symbol_table[tokens[0]]==location_counter
				size = int(tokens[2])
				location_counter += size
			elif tokens[1] == 'DC':
				self.symbol_table[tokens[0]]==location_counter
				location_counter += 1
			elif tokens[1] == 'LT':
				self.pool_table.append(tokens[0])
			else:
				self.symbol_table[tokens[0]] = location_counter
				location_counter += 1
			self.intermediate_code.append(f"{location_counter}({tokens[1]}, {tokens[0]})")
			
			
	def pass_two(self, source_code):
		lines = source_code.split('\n')
		location_counter = 0
		
		for line in lines:
			tokens = line.split()
			if len(tokens) == 0:
				continue
			if tokens[0]=='START':
				location_counter = int(tokens[1])
				continue
			if tokens[0]=='END':
				break
			if tokens[1] == 'DS' or tokens[1] == 'DC':
				location_counter += int(tokens[2])
			else:
				location_counter +=1
	def print_tables(self):
		print("Symbol Table:")
		print(self.symbol_table)
		print("Literal Table:")
		print(self.literal_table)
		print("Pool Table:")
		print(self.pool_table)
		print("Intermediate Code:")
		for code in self.intermediate_code:
			print(code)

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
	assembler.pass_two(source_code)
	assembler.print_tables()

