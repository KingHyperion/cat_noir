class DialogueManager:
    def speak(self, speaker: str, message: str):
        print(f"\n[{speaker}]: {message}")
        input("     [Press Enter to continue...]")