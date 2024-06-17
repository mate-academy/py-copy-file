def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print(
            "Invalid command format. Example usage: cp file.txt new_file.txt"
        )
        return
    source_filename = parts[1]
    dest_filename = parts[2]
    if source_filename == dest_filename:
        print(
            f"Source file '{source_filename}' and "
            f"destination file '{dest_filename}' are the same. "
            f"No copy performed."
        )
        return
    try:
        with (open(source_filename, "r") as file_in,
              open(dest_filename, "w") as file_out):
            file_out.write(file_in.read())

        print(
            f"File '{source_filename}' "
            f"successfully copied to '{dest_filename}'."
        )

    except FileNotFoundError:
        print(
            f"Error: One or both of the files '{source_filename}' "
            f"or '{dest_filename}' not found."
        )

    except IOError as e:
        print(f"Error: Failed to copy file. {e}")
