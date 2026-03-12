def copy_file(command: str) -> None:
    file_content = command.split()
    if len(file_content) == 3 and file_content[0] == "cp":
        origin_name = file_content[1]
        new_name = file_content[2]
        try:
            if origin_name != new_name:
                with open(f"{origin_name}", "r") as old_file:
                    content_for_copy = old_file.read()
                with open(f"{new_name}", "w") as new_file:
                    new_file.write(f"{content_for_copy}")
        except FileNotFoundError:
            pass
