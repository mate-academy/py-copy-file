def copy_file(command: str) -> None:
    # Split the command into parts
    parts = command.split()

    # Ensure the command has 3 parts
    if len(parts) != 3:
        print("Invalid command format. "
              "Usage: cp <source_file> <destination_file>")
        return

    # Extract source and destination file names
    source_file = parts[1]
    destination_file = parts[2]

    # Check if source and destination file names are the same
    if source_file == destination_file:
        print("Source and destination file names are the same. "
              "No action taken.")
        return

    try:
        # Open the source file for reading
        with open(source_file, "r") as file_in:
            # Read the content of the source file
            content = file_in.read()

            # Check if content is not empty
            if content:
                # Open the destination file for writing
                with open(destination_file, "w") as file_out:
                    # Write the content to the destination file
                    file_out.write(content)
                print(f"File '{source_file}' "
                      f"copied to '{destination_file}' successfully.")
            else:
                print(f"File '{source_file}' is empty. No action taken.")
    except FileNotFoundError:
        print("One or both files not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
