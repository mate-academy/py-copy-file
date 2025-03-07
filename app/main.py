import os


def copy_file(command: str) -> None:
    cp_list = command.split()
    if (len(cp_list) == 3
            and cp_list[0] == "cp"
            and os.path.exists(cp_list[1])):
        if cp_list[1] != cp_list[2]:
            with (open(cp_list[1], "r") as file_in,
                  open(cp_list[2], "w") as file_out):
                content = file_in.read()
                file_out.write(content)
