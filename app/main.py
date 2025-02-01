def copy_file(command: str) -> None:
    linux = command.split()
    if len(linux) != 3:
        raise ValueError("Invalid command: expected 'cp <f1> <f2>'")

    if linux[0] != "cp":
        raise ValueError("Invalid command: expected 'cp'")

    if linux[1] == linux[-1]:
        return  # Do nothing if the source and destination are the same

    try:
        with open(linux[1], "r") as src, open(linux[-1], "w") as dst:
            dst.write(src.read())
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file '{linux[1]}' not found.")
    except IOError as e:
        raise IOError(f"Error during file operation: {e}")
