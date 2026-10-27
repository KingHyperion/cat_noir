from dialogue import DialogueManager
from data.case_1 import test_suspect
from state import GameState

def main():
    ui = DialogueManager()
    state = GameState()
    
    while True:
        print("\n=-=-= Main Menu =-=-=")
        print("1. Talk to Suspect")
        print("2. View Journal")
        print("3. Quit")
        choice = input("Choice (1-3): ").strip()

        if choice == "1":
            ui.speak(test_suspect.get_name(), test_suspect.get_dialogue())
            clue = f"{test_suspect.get_name()}: {test_suspect.get_alibi()}"
            state.add_journal_entry(clue)
        
        elif choice == "2":
            print("=-=-= Detective Journal =-=-=")
            entries = state.get_journal()
            if not entries:
                print("Journal is empty. Talk to Suspects to collect clues and notes.")
            else:
                for i, entry in enumerate(entries, 1):
                    print(f"{i}. {entry}")
            
            input("     [Press Enter to continue...]")
        
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()