def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        comm, source_file, destination_file = command.split()
        if comm == "cp" and source_file != destination_file:
            try:
                with (open(source_file) as file_in,
                      open(destination_file, "w") as file_out):
                    content = file_in.read()
                    file_out.write(content)
            except FileNotFoundError:
                pass
