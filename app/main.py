def copy_file(command: str) -> None:
    if command.startswith("cp"):
        command = command.replace("cp ", "")
    else:
        print("Unknown command")
        return
    list_of_files_name = command.split(" ")
    if (list_of_files_name[0] != list_of_files_name[1]
            and len(list_of_files_name) == 2):
        try:
            with (
                open(list_of_files_name[0], "r")
                as first_file,
                open(list_of_files_name[1], "w")
                as second_file
            ):
                second_file.write(first_file.read())
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The file '{first_file}' does not exist."
            )
        except Exception as error:
            raise RuntimeError(
                f"An error occurred while copying the file: {error}"
            )
