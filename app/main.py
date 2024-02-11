def copy_file(command: str) -> None:
    arguments = command.split(" ")
    if (len(arguments) != 3
            or arguments[0] != "cp"
            or arguments[1] == arguments[2]):
        return
    with (open(arguments[1], "r") as file_in,
          open(arguments[2], "w") as file_out):
        file_out.write(file_in.read())
