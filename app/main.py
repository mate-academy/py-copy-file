def checking_command(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Too many / Not enough values!")
    if command[0] != "cp":
        raise ValueError(f"The program can "
                         f"copy only (use 'cp', not '{command[0]}')!")
    if "." not in command[1] or "." not in command[2]:
        raise ValueError("Specify the extension (*.txt)")
    for word in command[1].split() + command[2].split():
        if not word:
            raise ValueError("Check that the values are correct")


def copy_file(command: str) -> None:
    checking_command(command)
    first_file = command.split()[1]
    second_file = command.split()[2]
    if first_file != second_file:
        with (open(first_file) as copied_file,
                open(second_file, "w") as pasted_file):
            pasted_file.write(copied_file.read())
