import os


def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    cp_command, source_file_name, target_file_name = command_parts
    if cp_command != "cp":
        return
    if source_file_name == target_file_name:
        return
    if not os.path.exists(source_file_name):
        return

    with open(source_file_name, "r", encoding="utf-8") as file_in, \
         open(target_file_name, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())
