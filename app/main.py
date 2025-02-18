def copy_file(command: str) -> None:
    my_command, from_file, to_file = command.split()
    if from_file == to_file:
        return
    if my_command == "cp":
        with (open(from_file, "r") as file_in,
              open(to_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    else:
        print("error, command is not cp")
