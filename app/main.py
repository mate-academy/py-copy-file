def copy_file(command: str) -> None:
    command = command.split()
    if command[0] != "cp":
        raise ValueError("You line should start with cp")
    if len(command) != 3:
        raise ValueError("Write down cp than file name "
                         "where the info is and than "
                         "file name where you w ant to safe that info")
    if command[1] == command[2]:
        raise ValueError("There should be two different names of files")
    elif ".txt" in (command[1] and command[2]):
        with (open(command[1], "r") as file_in,
              open(command[2], "w") as file_out):
            file_out.write(file_in.read())
