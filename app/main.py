def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        print("Invalid command format. "
              "Please use 'cp source_file destination_file'.")
        return

    input_file = command_parts[1]
    output_file = command_parts[2]

    if input_file == output_file:
        print("In and out files are the same. Nothing to copy.")
        return

    try:
        with (open(input_file, "r") as file_in,
              open(output_file, "w") as file_out):
            file_out.write(file_in.read())
        print(f"File '{input_file}' copied to '{output_file}' successfully.")
    except FileExistsError:
        pass
    except Exception:
        pass
