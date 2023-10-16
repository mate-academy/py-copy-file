from typing import Any


def copy_file(command: str) -> Any:

    res_list = command.split(" ")
    if res_list[1] == res_list[2]:
        return
    with open(res_list[1], "r") as file_in, open(res_list[2], "w") as file_out:
        file_out.write(file_in.read())


copy_file("cp file.txt file.txt")
# copy_file("cp file.txt new_file.txt")
# print(open("file.txt").read() == open("new_file.txt").read())
