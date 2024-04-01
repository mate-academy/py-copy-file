def copy_file(files_name: str) -> None:
    files_name_arr = files_name.split(" ")

    if len(files_name_arr) != 3:
        print("Invalid command format. "
              "Please use 'cp old_file new_file'")
        return

    if files_name_arr[1] != files_name_arr[2]:
        with (open(files_name_arr[1], "r") as first_file,
              open(files_name_arr[2], "w") as second_file):
            second_file.write(first_file.read())
