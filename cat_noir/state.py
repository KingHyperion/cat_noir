class GameState:
    def __init__(self, initial_suspects: list):
        self._act = 1
        self._time_hour = 8
        self._interrogated_suspects = set()
        self._active_suspects = list(initial_suspects)
        self._journal = []
    
    def get_act(self): return self._act
    def get_time_hour(self): return self._time_hour
    def get_time_string(self):
        if self._time_hour <= 12:
            return f"{self._time_hour}:00 PM"
        else:
            return f"{self._time_hour - 12}:00 AM"
            
    def get_interrogated_suspects(self): return self._interrogated_suspects
    def get_active_suspects(self): return self._active_suspects
    def get_journal(self): return self._journal

    def set_act(self, act: int):
        if act > 0: self._act = act

    def advance_time(self, hours: int = 1):
        self._time_hour += hours

    def add_journal_entry(self, entry: str):
        if entry not in self._journal:
            self._journal.append(entry)
            print("\n>> Entry saved to journal.")
            input("     [Press Enter to continue...]")

    def record_interrogation(self, suspect_id: str):
        self._interrogated_suspects.add(suspect_id)

    def add_active_suspect(self, suspect_id: str):
        if suspect_id not in self._active_suspects:
            self._active_suspects.append(suspect_id)

    def to_dict(self):
        return {
            "act": self._act,
            "time_hour": self._time_hour,
            "interrogated_suspects": list(self._interrogated_suspects),
            "active_suspects": self._active_suspects,
            "journal": self._journal
        }

    def load_from_dict(self, data: dict):
        self._act = data.get("act", 1)
        self._time_hour = data.get("time_hour", 8)
        self._interrogated_suspects = set(data.get("interrogated_suspects", []))
        self._active_suspects = data.get("active_suspects", [])
        self._journal = data.get("journal", [])