
def copy_file(command: str) -> None:
    command_parts = command.split()
    if command_parts[0] != "cp":
        print("Invalid command format.")
        return
    source_file, destination_file = command_parts[1], command_parts[2]
    if source_file == destination_file:
        print("Source and destination files are the same.")
        return
    else:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
