def copy_file(command: str) -> None:
    command_list = command.split("")
    if (
        len(command_list) == 0
        or len(command_list) < 3
        or command_list[0] != "cp"
        or command_list[1] == command_list[2]
    ):
        return

    orig_file_name = command_list[1]
    new_file_name = command_list[2]

    try:
        with (open(orig_file_name, "r") as orig,
              open(new_file_name, "w") as new):
            orig_content = orig.read()
            new.write(orig_content)
    except FileNotFoundError:
        print(f"No such file or directory: '{orig_file_name}'")
        return
