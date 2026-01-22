def copy_file(command: str) -> None:
    cp = command.split()[0]
    if cp != "cp"\
            or command.split()[1] == command.split()[2]:
        print("Does nothing")
        return
    with open(command.split()[1], "r") as file_in,\
            open(command.split()[2], "w") as file_out:
        file_out.write(file_in.read())
