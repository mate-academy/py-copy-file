

def copy_file(command: str) -> None:
    cp, existing_file, new_file = command.split()

    if cp != "cp":
        return

    if existing_file == new_file:
        return

    with open(existing_file, "r") as file_out, open(new_file, "a") as file_in:
        for line in file_out:
            file_in.write(line)
