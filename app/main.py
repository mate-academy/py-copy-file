def copy_file(command: str) -> None | str:
    cmd_name, old_file_name, new_file_name = command.split()
    if cmd_name != "cp":
        return "Entered incorrect command!!!"
    if old_file_name != new_file_name:
        try:
            with (open(old_file_name, "r") as old_file,
                  open(new_file_name, "w") as new_file):
                new_file.write(old_file.read())
        except FileNotFoundError:
            return f"There is no file with name {old_file_name}"
        except PermissionError:
            return f"You don't have permission to file {old_file_name}"

