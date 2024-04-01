def copy_file(command: str) -> globals():
    copy_command, file_name_to_copy, new_file_name = command.split()
    if file_name_to_copy == new_file_name:
        print("Does nothing")
    elif copy_command == "cp" and file_name_to_copy != new_file_name:
        try:
            with (open(file_name_to_copy, "r") as file_in,
                  open(new_file_name, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print("You did not make a file.txt")
