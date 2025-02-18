import os


def copy_file(command: str) -> None:

    command_list = command.split(" ")
    if len(command_list) == 3:
        command_name = command_list[0]
        src_file = command_list[1]
        dest_file = command_list[2]
        if (command_name == "cp"
                and src_file != dest_file
                and os.path.exists(src_file)):
            with (open(src_file, "r") as file_in,
                  open(dest_file, "w") as file_out):
                file_out.write(file_in.read())
