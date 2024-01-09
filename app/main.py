def copy_file(command: str) -> None:
    command_parts = command.split()
    orig_name = command_parts[1]
    copy_name = command_parts[2]

    if orig_name != copy_name:
        with (open(orig_name, "r") as orig_file,
              open(copy_name, "w") as copy_file):
            for line in orig_file:
                copy_file.write(line)
