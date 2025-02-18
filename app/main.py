def copy_file(command: str) -> None:
    part = command.split()
    if len(command.split()) != 3:
        raise ValueError("command should have 3 arguments")
    if part[0] != "cp":
        raise ValueError("The command should be 'cp'")
    first_file = part[1]
    second_file = part[2]
    if first_file != second_file:
        with open(first_file, "r") as first, open(second_file, "w") as second:
            first_content = str(first.read())
            second.write(first_content)
