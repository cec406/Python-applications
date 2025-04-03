import datetime
import os
from colorama import init, Fore, Style

# Initialize Colorama for colored output
init()

def get_journal_file():
    """Prompt for a title and return the corresponding filename."""
    while True:
        title = input(f"{Fore.GREEN}Enter journal title (e.g., 'Dune Notes', 'Bible Study'): {Style.RESET_ALL}")
        if title.strip():
            # Replace spaces with underscores and ensure it ends with .txt
            filename = f"{title.replace(' ', '_')}.txt"
            print(f"{Fore.CYAN}Journal will be saved as: {filename}{Style.RESET_ALL}")
            return filename
        print(f"{Fore.RED}Title cannot be empty. Try again.{Style.RESET_ALL}")

def initialize_journal(journal_file):
    """Initialize the journal with the current date as the first line if it doesn't exist."""
    if not os.path.exists(journal_file):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        with open(journal_file, "w") as f:
            f.write(f"Date: {current_date}\n")
        print(f"{Fore.CYAN}New journal created with date: {current_date}{Style.RESET_ALL}")

def add_note(journal_file):
    """Add a new note to the specified journal file without timestamps."""
    initialize_journal(journal_file)  # Ensure the file exists with the date
    print(f"{Fore.GREEN}Enter your note (or type 'done' to finish):{Style.RESET_ALL}")
    while True:
        note = input("> ")
        if note.lower() == "done":
            break
        if note.strip():  # Only save non-empty notes
            with open(journal_file, "a") as f:
                f.write(f"{note}\n")
            print(f"{Fore.CYAN}Note saved!{Style.RESET_ALL}")

def show_journal(journal_file):
    """Display the full journal content."""
    initialize_journal(journal_file)  # Ensure the file exists with the date
    with open(journal_file, "r") as f:
        content = f.read()
    print(f"{Fore.MAGENTA}=== {os.path.basename(journal_file)} Content ==={Style.RESET_ALL}")
    print(content)
    print(f"{Fore.MAGENTA}===================={Style.RESET_ALL}")
    return content

def append_summary(journal_file, summary):
    """Append an AI-generated summary to the journal without a timestamp."""
    initialize_journal(journal_file)  # Ensure the file exists with the date
    with open(journal_file, "a") as f:
        f.write(f"\nAI Summary:\n{summary}\n")
    print(f"{Fore.GREEN}Summary appended to journal!{Style.RESET_ALL}")

def main():
    # Get the journal title once at the start
    journal_file = get_journal_file()

    while True:
        print(f"\n{Fore.BLUE}=== Note-Taking App ({os.path.basename(journal_file)}) ==={Style.RESET_ALL}")
        print("1. Add a note")
        print("2. Show journal")
        print("3. Add AI summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_note(journal_file)
        elif choice == "2":
            show_journal(journal_file)
        elif choice == "3":
            journal_content = show_journal(journal_file)
            if journal_content:
                print(f"{Fore.YELLOW}Please provide a summary based on the content above:{Style.RESET_ALL}")
                summary = input("Enter AI summary here: ")
                if summary.strip():
                    append_summary(journal_file, summary)
                else:
                    print(f"{Fore.RED}No summary provided.{Style.RESET_ALL}")
        elif choice == "4":
            print(f"{Fore.GREEN}Goodbye! Journal saved as {journal_file}{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid option. Try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
