import os


def copy_file(command: str) -> None:
    if len(command):
        command_list = command.split()
        if "cp" == command_list[0] and len(command_list) == 3:
            org_file = command_list[1]
            if not os.path.exists(org_file):
                return
            copy_file_name = command_list[2]
            if org_file != copy_file_name:
                with (
                    open(org_file, "r") as file,
                    open(copy_file_name, "w") as copy
                ):
                    copy.write(file.read())
