import os


def copy_file(command : str) -> None:
    if command is None or "cp" not in command:
        print('Command empty or not "cp". Returning...')
        return
    else:
        cli_arguments = command.split(" ")

    if len(cli_arguments) != 3 or cli_arguments[0] != "cp":
        print("Usage: cp source_file destination_file")
        return
    src_file_name = cli_arguments[1]
    dest_file_name = cli_arguments[2]

    if os.path.exists(src_file_name) and src_file_name != dest_file_name:
        with open(src_file_name, "r") as source, \
             open(dest_file_name, "w") as dest:
            for line in source.readlines():
                dest.write(line)
    else:
        print("Error! Invalid input files.")
