from typing import Any


def copy_file(command: str) -> Any:

    res_list = command.split()
    if res_list[1] == res_list[2]:
        return
    if len(res_list) == 3 and res_list[0] == "cp":
        with (open(res_list[1], "r") as file_in,
              open(res_list[2], "w") as file_out):
            file_out.write(file_in.read())
