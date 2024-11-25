def func1():
    with open("data/inputs.txt", "r") as file:
        lines = file.readlines()
    return lines[0].strip()