def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) <= 4 and parts[0] != "cp":
        print("Invalid command format")
        return

    s_file = parts[1]
    d_file = parts[2]

    if s_file == d_file:
        print("Source file and destination file names are the same")
        return

    try:
        with open(s_file, "r") as file_in, open(d_file, "w") as file_out:
            file_out.write(file_in.read())
            print("File copied successfully")
    except FileNotFoundError:
        print("Source file not found")
    except Exception as e:
        print(e)
