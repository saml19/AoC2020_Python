import re
with open('input.txt', 'r') as reader:
    input_data = reader.read().strip('\n').split('\n')


def valid_password(password) -> bool:
    data_dict = re.match("(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)", password).groupdict()
    if int(data_dict["min"]) <= data_dict["password"].count(data_dict["letter"]) <= int(data_dict["max"]):
        return True

def valid_password_part_2(password) -> bool:
    data_dict = re.match("(?P<pos1>\d+)-(?P<pos2>\d+) (?P<letter>\w): (?P<password>\w+)", password).groupdict()
    letter = data_dict["letter"]
    pos1 = int(data_dict["pos1"])
    pos2 = int(data_dict["pos2"])
    pos1_match = letter == data_dict["password"][pos1-1]
    pos2_match = letter == data_dict["password"][pos2-1]
    return pos2_match ^ pos1_match


valid_count = 0
for password in input_data:
    if valid_password(password):
        valid_count += 1

valid_count_2 = 0
for password in input_data:
    if valid_password_part_2(password):
        valid_count_2 += 1

print("part 1 valid count", valid_count)
print("part 2 valid count", valid_count_2)
