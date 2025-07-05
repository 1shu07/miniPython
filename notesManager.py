import os

FILENAME = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(FILENAME, "a") as f:
        f.write(note + "\n")
    print("Note added.\n")

def view_notes():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            content = f.read()
            if content.strip():
                print("\nYour Notes:\n" + content)
            else:
                print("\nNo notes yet.")
    else:
        print("\nNo notes file found.")

def delete_notes():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
        print("All notes deleted.")
    else:
        print("No notes to delete.")

def main():
    while True:
        print("\n--- Personal Notes Manager ---")
        print("1. Add a note")
        print("2. View notes")
        print("3. Delete all notes")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Exiting. Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
