
def copy_file_using_cp_command(command: str) -> None:
    command_parsed = command.split(" ")
    src_file_name = command_parsed[1]
    dst_file_name = command_parsed[2]

    if src_file_name == dst_file_name:
        print(f"File wasn't copied: source file '{src_file_name}' "
              f"has the same name as the destination file.")
    else:
        with open(src_file_name, "r") as src_file, \
             open(dst_file_name, "w") as dst_file:

            file_in_data = src_file.readline()
            dst_file.writelines(file_in_data)
