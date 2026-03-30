def copy_file(command: str) -> None:
    try:
        cmnd, file_name, copied_file = command.split(" ")
        if cmnd == "cp":
            if file_name != copied_file:
                with (open(file_name, "r") as original_file,
                      open(copied_file, "w") as new_file):
                    content = original_file.read()
                    new_file.write(content)
    except ValueError:
        pass
    except FileNotFoundError:
        pass
