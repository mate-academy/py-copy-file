import shutil


def copy_file(command: str) -> None:
    path = command.split()
    if len(path) == 3 and path[1] != path[2]:
        with open(path[1], "r") as file_in, open(path[2], "w") as file_out:
            shutil.copyfile(file_in, file_out)
            file_out.close()
    else:
        print("Your command don't allow to copy file")
