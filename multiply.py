a = [2, 6, 7, 5, 1]

b = [9, 6, 2, 5, 1]

def multiply_list(a,b):
    if len(a) != len(b):
        return None
result = [a * b for a, b in zip(a, b)]
print(result)