def copy_file(command: str) -> None:
    args = command.split()
    if len(args) != 3:
        print("Command must be in format 'cp source destination'")
        return

    cmd, original, copy = args
    if cmd != "cp":
        print("Only 'cp' command is supported")
        return
    if original == copy:
        print("Can't copy file to file with the same name")
        return

    try:
        with open(original, "rb") as orig, open(copy, "wb") as cpy:
            for line in orig:
                cpy.write(line)
    except FileNotFoundError:
        print(f"File '{original}' not found")
    except IsADirectoryError:
        print(f"'{original}' is a directory")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")
