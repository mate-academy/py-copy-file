def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Missed some arguments.")
    cp, file_in, file_out = command.split()
    if cp != "cp":
        raise ValueError("Incorrect command.")
    if file_in == file_out:
        raise ValueError("Incorrect FileIn and FileOut.")
    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        for line in f_in:
            f_out.write(line)
