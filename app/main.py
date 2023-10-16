def copy_file(files_name: str) -> None:
    command, name_old_file, name_new_file = files_name.split(" ")
    print(command, name_old_file, name_new_file)

    if name_old_file != name_new_file and command == "cp":
        with (open(name_new_file, "w") as new_file,
              open(name_old_file, "r") as old_file):
            new_file.write(old_file.read())
