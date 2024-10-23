def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Wrong copy command input")
    cmd = command.split()[0]
    data_file = command.split()[1]
    data_file_copy = command.split()[2]
    if cmd == "cp" and data_file_copy != data_file_copy:
        with (open(data_file, "r") as dfile,
              open(data_file_copy, "w") as cpfile):
            cpfile.write(dfile.read())
