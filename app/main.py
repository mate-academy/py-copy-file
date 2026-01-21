

def copy_file(command: str) -> None:
    list_of_command = command.split()
    if len(list_of_command) != 3:
        return
    file_to_copy = list_of_command[1]
    destination_file = list_of_command[2]
    if list_of_command[0] != "cp":
        return
    if command != str(f"cp {file_to_copy} {destination_file}"):
        return
    if file_to_copy == destination_file:
        return
    try:
        open(file_to_copy)
    except FileNotFoundError:
        return
    with (open(file_to_copy, "r") as file_in,
          open(destination_file, "w") as file_out):
        for line in file_in.readlines():
            file_out.write(line)
