import os.path


def copy_file(command: str) -> None:
    operation, source_file, target_file = command.split()
    if (operation == "cp") and \
            (source_file != target_file) and \
            os.path.exists(source_file):
        with open(source_file, "r") as file_in, \
                open(target_file, "w") as file_out:
            file_out.write(file_in.read())
