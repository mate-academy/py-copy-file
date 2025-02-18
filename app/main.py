def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3:
        action, source_file, destination_file = parts

        if action == "cp" and source_file != destination_file:
            try:
                with (
                    open(source_file, "r") as file_in,
                    open(destination_file, "w") as file_out
                ):
                    file_out.write(file_in.read())
            except OSError as e:
                print(f"Error occurred: {e}")
