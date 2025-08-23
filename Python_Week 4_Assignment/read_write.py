def file_read_write():
    # Asking user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as f:
            content = f.read()

        # Modifying the content by converting it to uppercase)
        modified_content = content.upper()

        # Writing the modified content to a new file
        with open("modified_output.txt", "w") as f:
            f.write(modified_content)

        print("✅ File has been successfully read and modified_output.txt created!")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Running the created program
file_read_write()

