def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Command must be in the "
                         "format 'cp <file.txt> <file-copy.txt>'")
    source_file, destanation_file = parts[1], parts[2]
    if source_file == destanation_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destanation_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{source_file}' does not exits.")
    except IOError as e:
        raise IOError(f"An I/O error occurred: {e}")
