# File read & write challenge with error handling in Python programming

def main():
    # --- Create and write to the file (w mode) ---
    filename = "myFile.txt"
    with open(filename, "w") as f:
        f.write("This is Python programming.\n")
        f.write("The topic today was File Handling\n")
    print("✅ File of text type was created and written in 'w' mode.")

    # --- Append more content (a mode) ---
    with open(filename, "a") as f:
        f.write("After the class, the tutor gave us an assignment.\n")
        f.write("We need to complete the assignment by Tuesday next week.\n")
    print("✅ Extra two lines were added in 'a' mode to the file.")

    # --- Ask user for filename ---
    user_filename = input("\nEnter the filename to read: ")

    # --- Try to read the file ---
    try:
        with open(user_filename, "r") as file:
            content = file.read()
        print("\n✅ File found! Here is its content:\n")
        print(content)

        # --- Modify the content (uppercase) ---
        modified_content = content.upper()

        # --- Write modified content to a new file ---
        new_filename = "modified_" + user_filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"\n✅ File processed successfully! Modified content saved as {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
