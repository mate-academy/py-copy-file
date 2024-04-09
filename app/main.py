import shutil


def copy_file(command: str) -> None:
    spl_com = command.split(" ")
    with open(spl_com[1], "r") as file_in, open(spl_com[2], "w") as file_out:
        if file_in == file_out:
            pass
        else:
            shutil.copyfile(file_in, file_out)
    file_out.close()
