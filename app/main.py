def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    target_file = parts[2]

    if source_file == target_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(target_file, "w") as file_out):
            file_out.write(file_in.read())
        print(f"Copied {source_file} to {target_file}")
    except FileNotFoundError:
        print(f"Error: {source_file} not found")
    except IOError:
        print("Error: Failed to copy file")
