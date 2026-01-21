def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Invalid command format. Follow this structure:"
              "cp filename.txt copied_filename.txt")
        return

    operation, old_filename, new_filename = parts

    if operation == "cp" and old_filename != new_filename:

        with (
            open(old_filename, "r") as file_in,
            open(new_filename, "w") as file_out
        ):

            file_out.write(
                file_in.read()
            )
