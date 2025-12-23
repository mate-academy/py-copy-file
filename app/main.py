import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        operation, file1_name, file2_name = parts
        if file1_name != file2_name and operation == "cp" and os.path.exists(file1_name):
            with open(file1_name, "r") as file_in, open(file2_name, "w") as file_out:
                for line in file_in.readlines():
                    file_out.write(line)
