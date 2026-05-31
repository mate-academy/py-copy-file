import os


def copy_file(command: str) -> None:
    if command:
        check_list = command.split()

        if check_list[0] == "cp" and len(check_list) == 3:
            if os.path.exists(check_list[1]):
                if check_list[1] != check_list[2]:
                    with open(f"{check_list[1]}", "r") as f_org:
                        all_lines = f_org.read()
                        with open(f"{check_list[2]}", "w") as f_copy:
                            f_copy.write(all_lines)
