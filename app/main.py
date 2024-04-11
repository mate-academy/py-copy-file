def copy_file(command: str) -> None:
    try:
        cmd = command.split()
        command_name, source_name, copy_name = cmd
    except Exception:
        print("Error in command argument!")
        return

    if (command_name == "cp") and (source_name != copy_name):
        with open(source_name) as source, open(copy_name, "w") as copy:
            data = source.read()
            copy.write(data)
