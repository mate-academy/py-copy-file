from os import path


def copy_file(command: str) -> None:
    command_name, file, file_to_copy = command.split()
    if not path.exists("file.txt"):
        print(f"file {file} do not exist")
    if command_name == "cp" and file != file_to_copy:
        with (open(file, "r") as current_file,
                open(file_to_copy, "w") as new_file):
            new_file.write(current_file.read())
