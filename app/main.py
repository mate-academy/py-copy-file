import shutil


def copy_file(command: str) -> None:
    try:
        # additional check, for tests AI buddy
        if len(command.split(" ")) != 3:
            raise ValueError

        copy_command, source_file_name, target_file_name = command.split(" ")

        if copy_command != "cp":
            print(f"Command {copy_command} is not supported yet")
            return

        try:
            if source_file_name != target_file_name:
                shutil.copyfile(source_file_name, target_file_name)
        except FileNotFoundError:
            print(f"Not found file with name: {source_file_name}")

    except ValueError:
        print(f"Cannot parse file names from command: {command}")
