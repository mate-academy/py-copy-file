import os


def copy_file(command: str) -> None:
    if command != "":

        command_without_command = command.replace("cp ", "")
        command_split_by_space = command_without_command.split(" ")

        if len(command_split_by_space) == 2:

            files_names = [command_split_by_space[0],
                           command_split_by_space[1]]

            if (files_names[0] != files_names[1]
                    and os.path.exists(files_names[0])):

                with (open(files_names[0], "r") as file_in,
                      open(files_names[1], "w") as file_out):
                    for line in file_in.readlines():
                        file_out.write(line)
