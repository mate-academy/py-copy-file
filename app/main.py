def copy_file(command: str) -> None:
    copied_file = command.split()[1]
    new_file = command.split()[2]

    if copied_file != new_file:
        with (open(copied_file, "r") as c_file,
              open(new_file, "w") as n_file):
            n_file.write(c_file.read())
