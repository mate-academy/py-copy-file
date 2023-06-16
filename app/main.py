def copy_file(command: str) -> None:
    words = command.split()
    if len(words) != 3:
        raise ValueError(
            "Invalid command. "
            "Expected three parts: mode, source file, destination file."
        )
    mode = words[0]
    source_file = words[1]
    destination_file = words[2]
    if mode == "cp" and source_file != destination_file:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
