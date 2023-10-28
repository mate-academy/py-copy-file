# write your code here
def copy_file(cmd: str) -> None:
    cmd_list = cmd.split()
    existing_file = cmd_list[1]
    new_file = cmd_list[2]
    with open(existing_file, "r") as file_in, open(new_file, "w") as file_out:

        if existing_file == new_file:
            return

        for line in file_in:
            file_out.write(line)
