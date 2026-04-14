def get_cp_arguments(command: str) -> dict:
    result = dict()
    arguments = command.split()

    try:
        if arguments[0] != "cp":
            return {}

        result["start"] = arguments[0]
        result["source"] = arguments[1]
        result["destination"] = arguments[2]
    except IndexError:
        return {}

    return result


def copy_file(command: str) -> bool:
    pass
