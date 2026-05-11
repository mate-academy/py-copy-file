def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "cp":
        print("Invalid command format.Use 'cp' source file destination_file")
    else:
        source_file, destination_file = command_parts[1], command_parts[2]
        if source_file != destination_file:
            try:
                with (open(source_file, "r") as file_in,
                      open(destination_file, "w") as file_out):
                    read_content = file_in.read()
                    file_out.write(read_content)
            except FileNotFoundError:
                print(f"File {source_file} does not exist")
