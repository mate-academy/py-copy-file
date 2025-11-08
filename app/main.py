def copy_file(command: str) -> None:
    if command == "":
        return
    command_list = command.strip().split()
    if command_list[0] != "cp" or len(command_list) != 3:
        return

    try:
        file_in = command_list[1]
        file_out = command_list[2]
        if file_in == file_out:
            return

        with (open(file_in, "r") as file_to_copy,
              open(file_out, "w") as file_to_insert):
            file_to_copy_content = file_to_copy.read()
            file_to_insert.write(file_to_copy_content)
    except FileNotFoundError:
        print("FIle not found!!!")
    except IndexError:
        print("Print correct command!!!")
