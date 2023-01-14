# write your code here
def copy_file(command: str) -> None:
    command_index = 0
    source_file_index = 1
    target_file_index = 2

    if command.split()[command_index] != "cp":
        return

    source_file = command.split()[source_file_index]
    target_file = command.split()[target_file_index]

    if source_file == target_file:
        return

    with open(source_file, "r") as source, open(target_file, "w") as target:
        target.write(source.read())
