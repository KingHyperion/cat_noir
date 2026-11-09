class DialogueManager:
    def speak(self, speaker: str, message: str):
        print(f"\n[{speaker}]: {message}")
        input("     [Press Enter to continue...]")

    def prompt_note_creation(self, default_clue: str):
        print("\n=-= Clue Discovered =-=")
        print(f'Default Note: "{default_clue}"')
        print("1. Save default note")
        print("2. Save custom note")
        print("3. Skip saving")

        choice = input("Choice (1-3): ").strip()
        if choice == "1":
            return default_clue
        elif choice == "2":
            custom = input("Enter your custom note: ").strip()
            if custom:
                return f"[Custom] {custom}"
            return None
        return None