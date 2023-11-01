def copy_file(command: str) -> None:
    parts = command.split()
    old_filename = parts[1]
    new_filename = parts[2]

    if len(parts) != 3:
        print("Invalid command format. Follow this structure:"
              "cp filename.txt copied_filename.txt")
        return

    if parts[0] == "cp" and old_filename != new_filename:

        with (
            open(old_filename, "r") as file_in,
            open(new_filename, "w") as file_out
        ):

            file_out.write(
                file_in.read()
            )
