import os.path


def copy_file(command: str) -> None:
    file_content = command.split()
    if len(file_content) == 3 and file_content[0] == "cp":
        source_file = file_content[1]
        new_file = file_content[2]
        if source_file != new_file and os.path.exists(source_file) is True:
            with open(
                    f"{new_file}", "w"
            ) as new_file, open(f"{source_file}", "r") as old_file:
                copy_content = old_file.read()
                new_file.write(f"{copy_content}")
