def copy_file(command: str) -> None:
    command, original_file, copy_file = command.split()
    if command == "cp" and original_file != copy_file:
        with (open(original_file, "r") as file_in,
              open(copy_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
