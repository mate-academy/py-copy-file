def copy_file(command: str) -> None:
    file_split = command.split()
    if len(file_split) != 3:
        print("Invalid command. Usage: cp <source_file> <destination_file>")
        return
    command_name, file_in_name, file_out_name = file_split
    if command_name != "cp":
        print("Invalid command. Usage: cp <source_file> <destination_file>")
        return
    if file_in_name != file_out_name:
        with open(
                file_in_name, "r") as file_in, open(
                file_out_name, "w") as file_out:
            file_out.write(file_in.read())
