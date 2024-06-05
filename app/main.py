def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file, destination_file = parts[1], parts[2]

    if source_file == destination_file:
        return

    try:
        with (
            open(source_file, "r") as src_file,
            open(destination_file, "w") as dest_file
        ):
            dest_file.write(src_file.read())
    except FileNotFoundError:
        print(f"File not found: {source_file}")
    except PermissionError:
        print(f"Permission denied: {source_file} or {destination_file}")
    except Exception as error:
        print(f"An error occurred: {error}")
