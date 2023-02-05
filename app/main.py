import shutil


def copy_file(command: str) -> str:
    file_1, file_2 = command.split()[1], command.split()[2]
    with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
        if file_in == file_out:
            pass
        return shutil.copyfile(file_1, file_2)


# copy_file("cp file1.txt file2.txt")
