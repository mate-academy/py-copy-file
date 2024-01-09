def copy_file(command: str) -> None:
    cp, orig_name, copy_name = command.split()

    if orig_name != copy_name:
        with (open(orig_name, "r") as orig_file,
              open(copy_name, "w") as copy_file):
            copy_file.write(orig_file.read())
