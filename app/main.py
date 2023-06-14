import os


def copy_file(command: str) -> None:
    cp_command, source_file, destination_file = command.split()

    if (
            source_file != destination_file
            and os.path.isfile(source_file)
            and cp_command == "cp"
    ):
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
