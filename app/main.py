import os.path


def copy_file(command: str) -> None:
    if command.startswith("cp"):
        command_list = command.split()
        if len(command_list) == 3:
            source_file, destination_file = command_list[1:]
            if os.path.exists(source_file) and source_file != destination_file:
                try:
                    with (
                        open(source_file, "r", encoding="utf-8")
                        as source_file_object,
                        open(destination_file, "w", encoding="utf-8")
                        as destination_file_object
                    ):
                        destination_file_object.write(
                            source_file_object.read()
                        )
                except OSError as e:
                    print(f"Error while copying file: {e}")
            else:
                print(
                    f"The specified file '{source_file}' "
                    f"could not be found. "
                    f"Please check if the file name and path are correct, "
                    f"and ensure that the file exists in the "
                    f"expected directory."
                )
