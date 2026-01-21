import os


class CommandNotFound(Exception):
    pass


class InvalidSizeCommand(Exception):
    pass


class FileNotFound(Exception):
    pass


class SameFileNames(Exception):
    pass


def copy_file_content(current_file: str, new_file: str) -> None:
    with open(current_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())


def handle_exceptions(command: str) -> None:
    separated_command = command.split()

    try:
        if "cp" not in separated_command:
            raise CommandNotFound("There must be 'cp' in the command")

        if len(separated_command) != 3:
            raise InvalidSizeCommand(f"There must be 3 arguments, "
                                     f"not {len(separated_command)}")

        current_file, new_file = separated_command[1], separated_command[2]

        file_path = os.path.join(os.getcwd(), current_file)

        if not os.path.exists(file_path):
            raise FileNotFound(f"File {current_file} doesn't exist.")

        if current_file == new_file:
            raise SameFileNames("Current and new file names are the same")

        copy_file_content(current_file, new_file)
    except CommandNotFound as cnf:
        print(f"Command not found: {cnf}")
    except InvalidSizeCommand as isc:
        print(f"Invalid size command: {isc}")
    except FileNotFound as fnf:
        print(f"File not found: {fnf}")
    except SameFileNames as sfne:
        print(f"Same file names: {sfne}")
    else:
        print("File copied successfully.")


if __name__ == "__main__":
    handle_exceptions("cp file-copy.txt 2.txt")
