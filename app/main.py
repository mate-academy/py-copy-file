def copy_file(command: str) -> None:

    splitted = command.split()

    if len(splitted) != 3 or splitted[0] != "cp":
        return
    else:
        original = splitted[1]
        copy = splitted[2]

        try:
            with open(original, "r") as file_in, open(copy, "w") as file_out:
                if original == copy:
                    return
                else:
                    file_out.write(file_in.read())
        except FileNotFoundError:
            return
