def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        src_file, dest_file = parts[1], parts[2]

        if src_file != dest_file:
            try:
                with (
                    open(src_file, "r") as file_in,
                    open(dest_file, "w") as file_out
                ):
                    file_out.write(file_in.read())
            except (FileNotFoundError, IOError) as e:
                print(f"Error copying file: {e}")
