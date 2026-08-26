import os


def copy_file(command: str) -> None:
    cmd_ls = command.split()

    if len(cmd_ls) != 3:
        return None

    original_file = cmd_ls[1]
    copied_file = cmd_ls[2]

    cwd_path = os.getcwd()
    original_f_path = os.path.join(cwd_path, original_file)
    copied_f_path = os.path.join(cwd_path, copied_file)

    if original_file == copied_file or cmd_ls[0] != "cp":
        return None

    try:
        with open(original_f_path, "r") as file_in, \
                open(copied_f_path, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        print("File not found")
