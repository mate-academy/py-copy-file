def copy_file(command: str) -> None:
    name_parts = command.split()

    if len(name_parts) == 3 and name_parts[0] == "cp":
        start_filename, new_filename = name_parts[1], name_parts[2]

        if start_filename != new_filename:
            with (
                open(start_filename, "r") as file_in,
                open(new_filename, "w") as file_out
            ):
                file_out.write(file_in.read())
            print(f"File {start_filename} "
                  f"copied to {new_filename}")
