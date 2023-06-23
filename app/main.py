def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        copy_command, file_in_name, file_out_name = command_list
        if copy_command == "cp" and file_in_name != file_out_name:
            with (open(file_in_name, "r") as file_in,
                  open(file_out_name, "w") as file_out):
                file_out.write(file_in.read())


file = open("file.txt", "w")
file.write("17:00 14/09/2022 value error")
file.close()
copy_file("cp file.txt new_file.txt")
