def copy_file(command: str) -> None:
    splitted_input = command.split()
    if (len(splitted_input) == 3
            and splitted_input[0] == "cp"
            and splitted_input[1] != splitted_input[2]):
        with (open(splitted_input[1], "r") as file_in,
              open(splitted_input[2], "w") as file_out):
            file_out.write(file_in.read())
