# write your code here
def copy_file(command: str) -> None:
    command_list = command.split(" ")

    if command_list[1] == command_list[2]:
        return
    else:

        old_file = command_list[1]
        new_file = command_list[2]

        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            string_file = file_in.read()
            file_out.write(string_file)
