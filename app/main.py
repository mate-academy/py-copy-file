import shutil


def copy_file(command: str) -> None:
    inner_command = command.split()
    if inner_command[0] == "cp" and inner_command[1] != inner_command[2]:
        with open(f"{inner_command[1]}", "w") as file_1:
            shutil.copyfile(f"{file_1.name}", f"{inner_command[2]}")
