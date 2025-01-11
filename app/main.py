def copy_file(command: str) -> None:
    file_index = command.find(" ")
    new_file_index = command.rfind(" ")

    if (file_index == -1 or new_file_index == -1
            or file_index == new_file_index):
        print("Wrong command")
        return

    source_file = command[file_index + 1:new_file_index].strip()
    copied_file = command[new_file_index + 1:].strip()

    if source_file == copied_file:
        return

    try:
        with open(
            source_file,
            mode="r"
        ) as file, open(
            copied_file,
            mode="w"
        ) as new_file:
            data = file.read()
            new_file.write(data)
        print(f"File {source_file} successfully copied to {copied_file}.")
    except FileNotFoundError:
        print(f"Error: file {source_file} not found")
    except IOError as e:
        print(f"Error: {e}")
