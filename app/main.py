def copy_file(command: str) -> any:
    first_file = command.split()[1]
    second_file = command.split()[2]

    if first_file.split(".")[0] == second_file.split(".")[0]:
        return "Does nothing"

    with open(first_file, "r") as first_f, open(second_file, "a") as second_f:
        for line in first_f:
            second_f.write(line)
