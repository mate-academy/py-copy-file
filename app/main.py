def copy_file(command: str) -> None:
    components = command.split()
    file_in, file_out = components[1], components[2]
    if components[1] == components[2]:
        print("No action to be taken")
        return

    with (
        open(file_in, "r") as source_file,
        open(file_out, "w") as destination_file
    ):

        destination_file.write(source_file.read())
