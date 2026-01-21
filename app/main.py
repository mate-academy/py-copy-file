def copy_file(command: str) -> None:
    cp, source_file, destination_file = command.split()

    if cp == "cp" and source_file != destination_file:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
