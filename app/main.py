def copy_file(command: str) -> None:
    (copy_command,
     file_name_1,
     file_name_2) = command.split(" ")
    if file_name_1 != file_name_2 and copy_command == "cp":
        try:
            with (open(file_name_1, "r") as source_file,
                  open(file_name_2, "w") as destination_file):
                data_copy = source_file.readlines()
                destination_file.writelines(data_copy)
        except FileNotFoundError:
            print("File not found")
        except PermissionError:
            print("Permission denied")
