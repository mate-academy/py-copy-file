def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Wrong copy command input")
    cmd, data_file, data_file_copy = command.split()
    if cmd == "cp" and data_file_copy != data_file_copy:
        with (open(data_file, "r") as dfile,
              open(data_file_copy, "w") as cpfile):
            cpfile.write(dfile.read())
