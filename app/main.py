def copy_file(command: str) -> None:
    command_type, input_file, output_file = command.split()
    if input_file != output_file and command_type == "cp":
        try:

            with (open(input_file, "r") as file_in,
                  open(output_file, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File {input_file} not found.")
        except Exception as error:
            print(f"An error occurred: {error}")
