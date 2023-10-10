def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format")

    _, source_file, destination_file = parts

    if source_file == destination_file:
        print("Files are the same!")
        return

    with (open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
        print(f"File {source_file} copied to {destination_file}")
