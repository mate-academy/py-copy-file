def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return print("Invalid command!")
    cmd, old_file, new_file = parts

    if old_file == new_file:
        return print("The source and destination files have the same name!")

    try:
        with open(old_file, "r") as source, open(new_file, "w") as dest:
            dest.write(source.read())
            print("Copied successfully!")
    except FileNotFoundError:
        print("Source file not found!")
    except PermissionError:
        print("Permission denied!")
