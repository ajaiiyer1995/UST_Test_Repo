def func2():
    with open("data/inputs.txt", "r") as file:
        lines = file.readlines()
    return lines[1].strip()