def copy_file(command: str) -> None:
    command_parts = command.split()
    if command_parts[0] != "cp" or command_parts[1] == command_parts[2]:
        print("Command is not 'cp' or source "
              "and destination files are the same.")
        return

    with (open(command_parts[1], "r") as file_in,
          open(command_parts[2], "w") as file_out):
        file_out.write(file_in.read())
    print(f"Copied contents from {command_parts[1]} to {command_parts[2]}")
