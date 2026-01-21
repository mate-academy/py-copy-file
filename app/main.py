def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Error: Invalid command format")
        return
    _, source_file, dest_file = parts

    if source_file != dest_file:
        with (open(source_file, "r") as file_in,
              open(dest_file, "w") as file_out):
            file_out.write(file_in.read())
