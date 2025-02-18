def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        source_file, destination_file = parts[1], parts[2]

        if source_file != destination_file:
            with (
                open(source_file, "r") as file_in,
                open(destination_file, "w") as file_out
            ):
                file_out.write(file_in.read())
            print(f"File {source_file} "
                  f"copied to {destination_file}")
