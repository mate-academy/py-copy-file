def copy_file(command: str) -> None:
    names = command.split()
    if names[1] == names[2]:
        print("you can not create files with simular names")
    else:
        with open(names[1], "r") as file_in, open(names[2], "w") as file_out:
            file_out.write(file_in.read())
