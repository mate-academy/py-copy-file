def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        print("Invalid command!")
        return

    if parts[1] == parts[2]:
        print("The source file and destination file have the same name!")
        return

    try:
        with open(parts[1], "r") as source_file, \
                open(parts[2], "w") as dest_file:
            dest_file.write(source_file.read())
            print("Copied successfully!")
    except FileNotFoundError:
        print("Source file not found!")
    except PermissionError:
        print("Permission denied!")
