import os


def copy_file(command: str) -> None:
    if command.count(".txt") < 2:
        print("Error: Command must contain exactly two .txt files.")
        return
    command_list = command.split()
    if command_list[0] != "cp":
        print("Error: Command must start with 'cp'")
        return
    source_file = command_list[1]
    if not os.path.exists(source_file):
        print(f"Error: File {source_file} does not exist.")
        return
    new_file = command_list[2]
    if source_file == new_file:
        print(f"Error: You can't copy {source_file} to {new_file} file.")
        return
    with open(source_file, "r") as file_out, open(new_file, "w") as file_in:
        file_in.write(file_out.read())
    print("File copied successfully.")
