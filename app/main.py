def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) <= 4 and parts[0] != "cp":
        print("Invalid command format")
        return

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        print("Source file and destination file names are the same")
        return

    try:
        with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
            print("File copied successfully")
    except FileNotFoundError:
        print("Source file not found")
    except Exception as e:
        print(e)
