def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[1] == parts[2]:
        return

    with (open(parts[1], "r") as file_in,
            open(parts[2], "w") as file_out):
        for line in file_in:
            file_out.write(line)


copy_file("cp test.txt test.txt")
