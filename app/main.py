def copy_file(command: str) -> None:
    instruction, source_file, destination_file = command.split()

    if instruction != "cp":
        return

    if source_file != destination_file:
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out,
        ):
            file_out.write(file_in.read())
