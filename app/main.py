def copy_file(command: str) -> None:
    command, orig_name, copy_name = command.split()

    if orig_name != copy_name and command == "cp":
        with (open(orig_name, "r") as orig_file,
              open(copy_name, "w") as copy_file):
            copy_file.write(orig_file.read())
