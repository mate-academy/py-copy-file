def copy_file(command: str) -> None:

    command, first_file, second_file = command.split()

    if first_file != second_file:

        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):

            content_of_first_file = []
            for line in file_in:
                content_of_first_file.append(line)

            file_out.writelines(content_of_first_file)
