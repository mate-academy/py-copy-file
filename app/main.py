import shutil


def copy_file(command: str) -> None:
    path = command.split(" ")
    if len(path) == 3:
        with open(path[1], "r") as file_in, open(path[2], "w") as file_out:
            if file_in == file_out:
                pass
            else:
                shutil.copyfile(file_in, file_out)
        file_out.close()
