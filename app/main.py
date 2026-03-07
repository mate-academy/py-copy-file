def copy_file(command: str) -> None:
    spl = command.strip().split()
    if len(spl) == 3:
        if spl[0] == "cp":
            if spl[1] != spl[2]:
                try:
                    with open(spl[1], "r") as file_in:
                        with open(spl[2], "w") as file_out:
                            file_out.write(file_in.read())
                finally:
                    return
