# write your code here
def copy_file(command: str) -> None:
    command, source_file, target_file = command.split()

    if command != "cp":
        return

    if source_file == target_file:
        return

    with open(source_file, "r") as source, open(target_file, "w") as target:
        target.write(source.read())
