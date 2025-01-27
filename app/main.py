import shutil


def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if command_list[0] == "cp" and len(command_list) == 3:
        src_path = f"{command_list[1]}"
        dst_path = f"{command_list[2]}"
        shutil.copy(src_path, dst_path)
