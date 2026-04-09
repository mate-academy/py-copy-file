import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        command, source_file, dest_file = parts
        if (command == "cp"
                and source_file != dest_file
                and os.path.exists(source_file)):
            with (open(source_file, "r") as file_in,
                  open(dest_file, "w") as file_out):
                content = file_in.read()
                file_out.write(content)
