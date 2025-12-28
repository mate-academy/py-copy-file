def copy_file(command: str) -> None:
    c_files_list = command.split()
    if c_files_list and c_files_list[0] == "cp" and len(c_files_list) == 3:
        source_file, destination_file = c_files_list[1], c_files_list[2]
        if source_file != destination_file:
            try:
                with (open(source_file, "r") as file_in,
                      open(destination_file, "w") as file_out):
                    file_out.write(file_in.read())
                    print(f"File {source_file} was successfully "
                          f"copied to {destination_file}.")
            except FileNotFoundError:
                print(f"File {source_file} was not found in the directory.")
            except PermissionError:
                print(f"Permission denied while accessing '{source_file}' or '{destination_file}'.")
            except IOError as e:
                print(f"An I/O error occurred: {e}")
