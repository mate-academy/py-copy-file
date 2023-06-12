def copy_file(command: str) -> None:
    com, first_file, second_file = command.split()

    if first_file != second_file and com == "cp":
        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):
            file_out.write(file_in.read())
            print(f"The data was successfully copied from the "
                  f"{first_file} to a {second_file}")
    print("Copy error! The command should be 'cp' "
          "and the files should have different names!")
