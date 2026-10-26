from dialogue import DialogueManager
from data.case_1 import test_suspect

def main():
    ui = DialogueManager()
    ui.speak(test_suspect.get_name(), test_suspect.get_dialogue())
    print("Test complete.")

if __name__ == "__main__":
    main()