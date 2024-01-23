import shutil


def copy_file(command: str) -> None:
    filenames = command.split()
    source_filename = filenames[1]
    destination_filename = filenames[2]
    if source_filename == destination_filename:
        return
    with open(source_filename, "r") as file_in, \
            open(destination_filename, "w") as file_out:
        shutil.copyfileobj(file_in, file_out)
