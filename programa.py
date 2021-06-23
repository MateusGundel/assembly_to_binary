instruction_dict = {
    'MOVE': '0001',
    'LOAD': '0010',
    'STORE': '0011',
    'ADD': '0100',
    'SUB': '0101',
    'AND': '0110',
    'OR': '0111',
    'HALT': '1000',
    'NOP': '1001',
    'BRANCH': '1010',
    'BZERO': '1011',
    'BNEG': '1100'}


def generate_binary_code(value):
    if 'R' in value.upper():
        value = value[1:]

    binary = f"{int(value):b}"
    if len(binary) < 4:
        return "0"*(4-len(binary))+binary
    return binary


def assembly_to_binary():
    lines = []
    with open("entradas.txt", "r") as ini_file:
        for index, line in enumerate(ini_file.readlines()):
            values = line.replace("\n", "").split(" ")
            
            string = instruction_dict.get(values[0])
            string += generate_binary_code(values[1]
                                           ) if len(values) > 1 else ""
            string += generate_binary_code(values[2]
                                           ) if len(values) > 2 else ""
            string += generate_binary_code(values[3]
                                           ) if len(values) > 3 else ""
            string += ("0"*(16-len(string)))
            
            if index != 0:
                string += ","
                
            string += "\n"
            lines.append(string)
    with open('saidas.txt', 'w') as file:
        file.writelines(lines)


if __name__ == '__main__':
    assembly_to_binary()
