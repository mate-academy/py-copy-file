def copy_file(command: str) -> None:
    coped_file = command.split()[1]
    new_file = command.split()[2]

    if coped_file == new_file:
        return

    with (open(coped_file, "r") as c_file,
          open(new_file, "w") as n_file):
        n_file.write("".join(c_file.readlines()))
