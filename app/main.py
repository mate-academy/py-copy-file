def copy_file(command: str) -> None:
    command = command.split(" ")
    sourse_file = command[1]
    copied_file = command[2]
    if sourse_file != copied_file:
        with open(sourse_file, "r") as sourse:
            with open(copy_file, "w") as copy:
                copy.write(sourse.read())
