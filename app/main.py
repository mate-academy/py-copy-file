def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 and parts[0] != "cp":
        print("Invalid command format")
        return

    if parts[1] == parts[2]:
        print("Source file and destination file names are the same")
        return

    try:
        with open(parts[1], "r") as file_in, open(parts[2], "w") as file_out:
            file_out.write(file_in.read())
            print("File copied successfully")
    except FileNotFoundError:
        print("Source file not found")
    except Exception as e:
        print(e)
