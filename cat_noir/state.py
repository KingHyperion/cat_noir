class GameState:
    def __init__(self):
        self._journal = []
    
    def get_journal(self):
        return self._journal
    
    def add_journal_entry(self, entry: str):
        if entry not in self._journal:
            self._journal.append(entry)
            print("\n>> Entry saved to journal.")
            input("     [Press Enter to continue...]")