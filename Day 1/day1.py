with open('data.txt', 'r') as reader:
    input_data = [int(i) for i in reader.read().strip('\n').split('\n')]


def find_2020(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            for k in range(len(arr) - 1):
                if arr[i] + arr[j] + arr[k] == 2020:
                    return arr[i] * arr[j] * arr[k]


print(find_2020(input_data))
