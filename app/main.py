def copy_file(command: str) -> None:
    source_file_name = command.split()
    try:
        if len(source_file_name) == 3:
            if ("cp" == source_file_name[0]
                    and source_file_name[1] != source_file_name[2]):

                with (open(source_file_name[1], "r") as file,
                      open(source_file_name[2], "w") as new_file):

                    new_file.write(file.read())
    except FileNotFoundError:
        return
