# write your code here
def copy_file(command: str) -> None:
    command = command.split()
    if len(command) > 0  and len(command) == 3 and command[0] == "cp":
        if not command[1] == command[2]:
            try:
                with (open(f"{command[1]}", "r") as file_in,
                      open(f"{command[2]}", "w") as file_out):
                    string = file_in.readlines()
                    file_out.writelines(string)
            except FileNotFoundError:
                print("No such file or directory")
