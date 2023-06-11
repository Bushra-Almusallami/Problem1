def generate_multiples(num, length):
    multiples = []

    for i in range(1, length + 1):
        multiples.append(num * i)

    return multiples

number = 3
desired_length = 7

result = generate_multiples(number, desired_length)
print(result)
