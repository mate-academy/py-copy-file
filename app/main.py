def copy_file(command: str) -> None:
    args = command.split()
    if args[0] != "cp":
        raise ValueError("Command must start with 'cp'.")
    command_name, source_file, destination_file, *_ = args
    if source_file == destination_file:
        raise ValueError("Source and destination files are the same.")
    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
