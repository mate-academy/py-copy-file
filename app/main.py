import os


def copy_file(command: str) -> None:
    if command != "":
        file_names = command.split(" ")

        if len(file_names) != 3 or file_names[0] != "cp":
            return

        source_file = file_names[1]
        target_file = file_names[2]

        if "/" in source_file or "/" in target_file:
            return
        if "\\" in source_file or "\\" in target_file:
            return

        if os.path.exists(source_file) and source_file != target_file:
            with (open(source_file, "r") as file_in,
                  open(target_file, "w") as file_out):
                content = file_in.read()
                file_out.write(content)
