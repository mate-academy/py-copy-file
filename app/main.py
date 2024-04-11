def copy_file(command: str) -> None:
    try:
        cmd = command.split()
        command_name = cmd[0]
        source_name = cmd[1]
        copy_name = cmd[2]
    except Exception:
        print("Error in command argument!")
        return None

    if command_name == "cp":
        if source_name != copy_name:
            with open(source_name) as source, open(copy_name, "w") as copy:
                data = source.read()
                copy.write(data)


