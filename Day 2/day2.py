import re
with open('input.txt', 'r') as reader:
    input_data = reader.read().strip('\n').split('\n')
    print(input_data)


def valid_password(password) -> bool:
    data_dict = re.match("(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)", password).groupdict()
    if int(data_dict["min"]) <= data_dict["password"].count(data_dict["letter"]) <= int(data_dict["max"]):
        return True


valid_count = 0
for password in input_data:
    if valid_password(password):
        valid_count += 1

print(valid_count)
