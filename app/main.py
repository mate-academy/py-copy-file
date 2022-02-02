def copy_file(command: str):
    split_command = command.split()
    if split_command[1] != split_command[2]:
        with open(split_command[1], 'r') as source:
            lines = source.readlines()
            with open(split_command[2], "w") as destination:
                for line in lines:
                    destination.write(line)
                print(f"File {split_command[1]} copied successfully!")
