def copy_file(command: str) -> None:
    arguments = command.split()
    if len(arguments) != 3:
        raise ValueError("Wrong count of arguments")
    com, original_filename, copy_filename = arguments
    if com != "cp":
        raise ValueError("Wrong command")
    with (open(arguments[1], "r") as file_in,
          open(arguments[2], "w") as file_out):
        if original_filename != copy_filename:
            file_out.write(file_in.read())
