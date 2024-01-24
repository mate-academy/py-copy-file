def copy_file(command: str) -> None:
    operator, input_file, output_file = command.split()
    if input_file != output_file and operator == "cp":
        try:

            with (open(input_file, "r") as file_in,
                  open(output_file, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"File {input_file} not found.")
        except Exception as error:
            print(f"An error occurred: {error}")
