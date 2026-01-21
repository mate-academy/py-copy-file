def copy_file(command: str) -> None:
    try:
        cp, old_file, new_file = command.split()
        for_len = cp, old_file, new_file
        if len(for_len) == 3 and cp == "cp":
            if old_file != new_file:
                try:
                    with (open(old_file, "r") as file_in,
                          open(new_file, "w") as file_out):
                        for line in file_in:
                            file_out.write(line)
                except FileNotFoundError:
                    print("FileNotFoundError:")
    except ValueError:
        print("ValueError")
