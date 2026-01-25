def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        comm, source_file, destination_file = parts
        if comm == "cp" and source_file != destination_file:
            try:
                with (open(source_file) as file_in,
                      open(destination_file, "w") as file_out):
                    content = file_in.read()
                    file_out.write(content)
            except FileNotFoundError:
                pass
