def copy_file(command_str: str) -> None:
    if len(command_str.split()) == 3:
        command, old_file_name, new_file_name = command_str.split()

        if command == "cp" and (old_file_name != new_file_name):
            try:
                with open(old_file_name, "r") as old_file:
                    text = old_file.read()
            except FileNotFoundError:
                print("No such file or directory")
            else:
                with open(new_file_name, "w") as new_file:
                    new_file.write(text)
