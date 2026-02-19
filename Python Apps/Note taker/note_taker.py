#!/usr/bin/env python3
"""
Grizzly Note Taker - Console Edition
Simple offline journaling tool
Built by Grizzly System Engineering – East Helena, Montana
https://grizzlyse.com | (406) 439-8127 | info@grizzlyse.com

INSTRUCTIONS:
- Enter journal title when asked
- Menu options:
  1. Add notes     → keeps accepting lines until you type 'done'
  2. Show journal  → displays current saved content
  3. Add summary   → shows journal first, then asks for summary
  4. Exit          → closes the app
- Notes are saved continuously as you type them
- All files saved in the same folder as this script
"""

import datetime
import os
from colorama import init, Fore, Style

init(autoreset=True)

# Force files to save in script's own folder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_journal_file():
    print(f"{Fore.BLUE}Grizzly Note Taker - Private & Offline Journaling{Style.RESET_ALL}")
    while True:
        title = input(f"{Fore.GREEN}Journal title (e.g. 'Bible Study', 'Dune Notes'): {Style.RESET_ALL}").strip()
        if title:
            filename = f"{title.replace(' ', '_')}.txt"
            full_path = os.path.join(SCRIPT_DIR, filename)
            print(f"{Fore.CYAN}Journal will be saved as: {full_path}{Style.RESET_ALL}")
            return full_path
        print(f"{Fore.RED}Title cannot be empty. Try again.{Style.RESET_ALL}")


def initialize_journal(journal_file):
    if not os.path.exists(journal_file):
        current_date = datetime.date.today().isoformat()
        try:
            with open(journal_file, "w", encoding="utf-8") as f:
                f.write(f"Date: {current_date}\n\n")
            print(f"{Fore.CYAN}New journal created – started on {current_date}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error creating journal: {e}{Style.RESET_ALL}")


def add_note(journal_file):
    initialize_journal(journal_file)
    print(f"{Fore.GREEN}Enter notes (type 'done' on a new line to finish):{Style.RESET_ALL}")
    while True:
        line = input("> ").rstrip()
        if line.lower() == "done":
            print(f"{Fore.CYAN}Finished adding notes.{Style.RESET_ALL}")
            break
        if line.strip():
            try:
                with open(journal_file, "a", encoding="utf-8") as f:
                    f.write(f"{line}\n")
            except Exception as e:
                print(f"{Fore.RED}Error saving line: {e}{Style.RESET_ALL}")
                break


def show_journal(journal_file, pause=True):
    initialize_journal(journal_file)
    try:
        with open(journal_file, "r", encoding="utf-8") as f:
            content = f.read().rstrip()
        word_count = len(content.split())
        print(f"{Fore.MAGENTA}=== {os.path.basename(journal_file)} ({word_count:,} words) ==={Style.RESET_ALL}")
        print(content)
        print(f"{Fore.MAGENTA}==================={Style.RESET_ALL}")
        if pause:
            input(f"{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
        return content
    except Exception as e:
        print(f"{Fore.RED}Cannot read journal: {e}{Style.RESET_ALL}")
        return ""


def append_summary(journal_file):
    # Show journal first, but DON'T pause (so it flows straight to summary prompt)
    show_journal(journal_file, pause=False)
    print(f"{Fore.YELLOW}Enter your summary below (or press Enter to skip):{Style.RESET_ALL}")
    summary = input("> ").strip()
    if summary:
        try:
            with open(journal_file, "a", encoding="utf-8") as f:
                f.write(f"\nSummary:\n{summary}\n\n")
            print(f"{Fore.GREEN}Summary added!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error adding summary: {e}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}No summary added.{Style.RESET_ALL}")


def main():
    journal_file = get_journal_file()

    while True:
        clear_screen()
        print(f"{Fore.BLUE}=== Grizzly Note Taker ({os.path.basename(journal_file)}) ==={Style.RESET_ALL}")
        print(f"  File: {os.path.abspath(journal_file)}")
        print("1. Add notes (type 'done' when finished)")
        print("2. Show journal")
        print("3. Add summary")
        print("4. Exit")
        print(f"{Fore.YELLOW}Tip: Type 'done' to finish adding notes. Ctrl+C to quit anytime.{Style.RESET_ALL}")
        try:
            choice = input("Choose (1-4): ").strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Goodbye! Journal saved.{Style.RESET_ALL}")
            break

        if choice == "1":
            add_note(journal_file)
        elif choice == "2":
            show_journal(journal_file, pause=True)
        elif choice == "3":
            append_summary(journal_file)
        elif choice == "4":
            print(f"{Fore.GREEN}Goodbye! Journal saved as:{Style.RESET_ALL}")
            print(f"  → {os.path.abspath(journal_file)}")
            input("Press Enter to close...")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1, 2, 3, or 4.{Style.RESET_ALL}")
            input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Exiting cleanly.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")
        input("Press Enter to close...")