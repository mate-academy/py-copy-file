def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3 or parts[0] != "copy" or parts[1] == parts[2]:
        return

    _, source_file, destination_file = parts

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        content = file_in.read()
        file_out.write(content)
