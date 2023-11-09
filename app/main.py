# write your code here
def copy_file(cmd: str) -> None:
    cmd_list = cmd.split()

    if len(cmd_list) == 3 and cmd_list[0] == "cp":
        _, existing_file, new_file = cmd_list

        if existing_file != new_file:

            with open(existing_file, "r") as file_in:
                with open(new_file, "w") as file_out:

                        file_out.write(file_in.read())
