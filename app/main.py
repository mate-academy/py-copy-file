def copy_file(command: str):
    split_command = command.split()
    if split_command[1] != split_command[2]:
        with open(split_command[1], 'r') as f1:
            lines = f1.readlines()
            with open(split_command[2], "w") as f2:
                for line in lines:
                    f2.write(line)
                print(f"File {split_command[1]} copied successfully!")
