def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command")
        return

    source_file, dest_file = parts[1], parts[2]

    if source_file == dest_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(dest_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File {source_file} not found")
