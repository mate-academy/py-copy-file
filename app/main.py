# write your code here

def copy_file(command: str) -> None:
    if len(command.split()) == 3 and "cp" in command:
        _, source_path, destination_path = command.split()
    if source_path != destination_path:
        with open(source_path, "r") as source_file, open(destination_path, "w") as destination_file:
            destination_file.write(source_file.read())
