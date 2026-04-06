import os


def copy_file(command: str) -> None:
    command_to_list = command.split()

    if len(command_to_list) == 3 and command_to_list[0] == "cp":
        source_file_name = command_to_list[1]
        destination_file_name = command_to_list[2]

        if source_file_name == destination_file_name:
            return

        if os.path.isfile(source_file_name):
            with (open(source_file_name, "r") as file_in,
                  open(destination_file_name, "w") as file_out):
                file_out.write(file_in.read())
