def copy_file(command: str) -> None | str:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError(
            "Please use valid command format: "
            "cp <source_file> <destination_file>"
        )

    src_file, dest_file = parts[1], parts[2]

    if src_file == dest_file:
        return f"{src_file} and {dest_file} are the same"

    try:
        with (
            open(src_file, "r") as file_orig,
            open(dest_file, "w") as file_copy
        ):

            file_copy.write(file_orig.read())

        print(f"File '{src_file}' successfully copied to '{dest_file}'")

    except FileNotFoundError:
        print(f"Error: File '{src_file}' not found")

    except Exception as e:
        print(f"An error occurred: {e}")
