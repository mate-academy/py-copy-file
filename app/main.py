def copy_file(command: str) -> None:
    command_parts = command.split()
    cp_command, source, destination_file = (command_parts[0],
                                            command_parts[1],
                                            command_parts[2])
    if cp_command != "cp" or source == destination_file:
        print("Command is not 'cp' or source "
              "and destination files are the same.")
        return

    with open(source, "r") as file_in, open(destination_file, "w") as file_out:
        file_out.write(file_in.read())
    print(f"Copied contents from {source} to {destination_file}")
