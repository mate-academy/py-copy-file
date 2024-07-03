def copy_file(command: str) -> None:
    command_to_arr = command.split()
    if len(command_to_arr) != 3 or command_to_arr[0] != "cp":
        return

    source = command_to_arr[1]
    destination = command_to_arr[2]

    if source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
        print(f"File {source} has been copied to {destination}")
    except FileNotFoundError:
        print(f"File {source} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")
