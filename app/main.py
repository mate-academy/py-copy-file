def copy_file(command: str) -> None:
    line_command = command.split(" ")

    if (len(line_command) == 3
            and line_command[0] == "cp"
            and line_command[1] != line_command[2]):

        with (open(line_command[1], "r") as file_in, 
              open(line_command[2], "w") as file_out):
            file_out.write(file_in.read())
    