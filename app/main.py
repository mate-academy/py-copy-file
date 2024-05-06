def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format")
        return

    source_file, destination_file = command[1], command[2]

    if source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out
              ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File: {source_file} not found")
