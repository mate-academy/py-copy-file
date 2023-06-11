def copy_file(command: str) -> None | str:
    if not command.startswith("cp ") or len(command.split(" ")) != 3:
        return "Entered incorrect command!!!"
    old_file_name = command.split(" ")[1]
    new_file_name = command.split(" ")[2]
    if old_file_name != new_file_name:
        try:
            with (open(old_file_name, "r") as old_file,
                  open(new_file_name, "w") as new_file):
                new_file.write(old_file.read())
        except FileNotFoundError:
            print(f"There is no file with name {old_file_name}")
        except PermissionError:
            print(f"You don't have permission to file {old_file_name}")
