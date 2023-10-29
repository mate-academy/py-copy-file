# write your code here
def copy_file(cmd: str) -> None:
    cmd_list = cmd.split()
    if len(cmd_list) == 3:
        _, existing_file, new_file = cmd_list
    else:
        print("cmd_list should have a length of 3.")

    with open(existing_file, "r") as file_in, open(new_file, "w") as file_out:

        if existing_file == new_file:
            try:
                with open(source_filename, 'r') as file_in, open(destination_filename, 'w') as file_out:
                    file_out.write(file_in.read())
                return True
            except FileNotFoundError:
                print("File not found.")
                return False
