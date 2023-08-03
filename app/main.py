def copy_file(command: str) -> None:
    splitted = command.split()

    if splitted[0] == "cp" and splitted[1] != splitted[2]:
        with (open(splitted[1], "r") as file_in,
              open(splitted[2], "a") as file_out):
            for line in file_in:
                file_out.write(line)
