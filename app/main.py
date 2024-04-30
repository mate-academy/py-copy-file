def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command. Usage: cp source_file destination_file")
        return
    source_file = parts[1]
    destination_file = parts[2]
    if source_file == destination_file:
        print("Source and destination files are the same.")
        return
    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
        print(f"File '{source_file}' copied to "
              f"'{destination_file}' successfully.")
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An error occurred while copying the file.")
