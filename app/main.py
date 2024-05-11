def copy_file(command: str) -> None:
    parts = command.split()
    source_file, destination_file = parts[1:]
    if len(parts) != 3 or parts[0] != "cp":
        print("Please use the format: cp copy_file.txt new_file.txt")
        return
    if source_file == destination_file:
        print("Source and destination files are the same. Nothing to copy.")
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())
