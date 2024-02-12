def copy_file(command: str) -> None:
    arguments = command.split()
    if len(arguments) != 3:
        raise ValueError("Wrong count of arguments")
    com, original_filename, copy_filename = arguments
    if com != "cp" or original_filename == copy_filename:
        raise ValueError("Wrong command")
    with (open(original_filename, "r") as file_in,
          open(copy_filename, "w") as file_out):
        file_out.write(file_in.read())
