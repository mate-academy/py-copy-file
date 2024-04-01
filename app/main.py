import shutil


def copy_file(command: str) -> None | str:
    command_list = command.split()
    if command_list[0] == "cp" and len(command_list) == 3:
        _, first_file, second_file = command_list
    else:
        return f"Wrong command line please double check it: {command}"

    try:
        shutil.copy(first_file, second_file)
        return f"File '{second_file}' was created"
    except FileNotFoundError:
        return f"File '{first_file}' doesn't exist"
    except OSError:
        return f"Invalid file name '{second_file}'"
    except Exception:
        """Incase some unknown error still exist that I don't know of"""
        raise Exception
