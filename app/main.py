def copy_file(files_name: str) -> None:
    cp_parameter, old_file_name, new_file_name = files_name.split()

    if cp_parameter != "cp":
        print("Invalid command format. "
              "Please use 'cp old_file new_file'")
        return

    if old_file_name != new_file_name:
        with (open(old_file_name, "r") as old_file,
              open(new_file_name, "w") as new_file):
            new_file.write(old_file.read())
