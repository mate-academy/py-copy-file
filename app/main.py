def copy_file(command_copy: str) -> None:
    list_of_files = command_copy.split()
    if (len(list_of_files) == 3
            and (list_of_files[1] != list_of_files[2])
            and list_of_files[0] == "cp"):
        try:
            with (open(list_of_files[1], "r") as file_in,
                  open(list_of_files[2], "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print("File not found")
