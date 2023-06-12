def copy_file(command: str) -> None:
    com, first_file, second_file = command.split()
    if first_file != second_file:
        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):
            data = file_in.read()
            file_out.write(data)
            print(f"The data was successfully copied from the "
                  f"{first_file} to a {second_file}")
    print("The files have the same names. Copy error!")
