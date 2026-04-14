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
    arguments = get_cp_arguments(command)

    if len(arguments) != 3:
        return False

    if arguments["source"] == arguments["destination"]:
        return False

    content = None

    try:
        with open(arguments["source"], "rb") as file_desc:
            content = file_desc.read()
    except FileNotFoundError:
        print("Source file " + arguments["source"] + " not found")
        return False

    with open(arguments["destination"], "wb") as file_desc:
        file_desc.write(content)

    return True
