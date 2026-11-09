import json
import os

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

class Suspect:
    def __init__(self, suspect_id: str, name: str, alibi: str, dialogue: str):
        self._suspect_id = suspect_id
        self._name = name
        self._alibi = alibi
        self._dialogue = dialogue

    def get_id(self): return self._suspect_id
    def get_name(self): return self._name
    def get_alibi(self): return self._alibi
    def get_dialogue(self): return self._dialogue

class Location:
    def __init__(self, location_id: str, name: str, description: str, suspect_ids: list = None):
        self._location_id = location_id
        self._name = name
        self._description = description
        self._suspect_ids = suspect_ids if suspect_ids else []

    def get_name(self): return self._name
    def get_description(self): return self._description
    def get_suspect_ids(self): return self._suspect_ids

class CaseData:
    def __init__(self, title: str, initial_suspect_ids: list, locations: dict, suspects: dict):
        self._title = title
        self._initial_suspect_ids = initial_suspect_ids
        self._locations = locations
        self._suspects = suspects

    def get_title(self): return self._title
    def get_initial_suspect_ids(self): return self._initial_suspect_ids
    def get_locations(self): return self._locations
    def get_suspects(self): return self._suspects

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

case_1 = CaseData(
    title="The Case of the Golden Tuna",
    initial_suspect_ids=["groundskeeper", "maid", "cook", "pool_boy"],
    suspects={
        "groundskeeper": Suspect("groundskeeper", "Groundskeeper", "Claims he was trimming hedges at 10 PM.", "I was trimming hedges at 10 PM sharp... Stop putting your nose in my business!"),
        "pool_boy": Suspect("pool_boy", "Pool Boy", "Claims he was testing pool chemicals at 10 PM.", "I was at the pool. But I saw the Maid leaving early."),
        "maid": Suspect("maid", "Maid", "Claims she was cleaning the Manor study at 10 PM.", "I was in the study! The Cook was acting nervous."),
        "cook": Suspect("cook", "Cook", "Claims he was prepping fish at the Restaurant all evening.", "I was in the kitchen! Sir Meowbert locked his office late."),
        "courier": Suspect("courier", "Suspicious Courier", "Spotted delivering a heavy locked box from the manor after midnight.", "I was paid big bucks to ship a box from Meowbert's manor at midnight!"),
        "meowbert": Suspect("meowbert", "Sir Meowbert", "Owner of the estate.", "I just want my golden statue back!")
    },
    locations={
        "grounds": Location("grounds", "Manor Grounds", "The lush outdoor property of the Meowbert estate.", ["groundskeeper", "pool_boy"]),
        "interior": Location("interior", "Manor Interior", "The grand hall and private rooms of the estate.", ["maid", "cook"]),
        "town": Location("town", "Town Square", "The bustling heart of the town.", [])
    }
)

save_file = "savegame.json"

class DetectiveEngine:
    def __init__(self, case_data):
        self._case = case_data
        self._state = GameState(case_data.get_initial_suspect_ids())
        self._ui = DialogueManager()

    def get_case(self):
        return self._case

    def get_state(self):
        return self._state

    def save_game(self):
        with open(save_file, "w") as f:
            json.dump(self._state.to_dict(), f, indent=4)
        print("\n>> Game progress saved.")
        input("      [Press Enter to continue...]")

    def load_game(self):
        if os.path.exists(save_file):
            with open(save_file, "r") as f:
                data = json.load(f)
                self._state.load_from_dict(data)
            print("\n>> Save file loaded.")
            input("     [Press Enter to continue...]")
            return True
        return False

    def investigate_location(self, loc_id: str):
        locations = self._case.get_locations()
        if loc_id not in locations:
            return

        location = locations[loc_id]
        self._state.advance_time(1)

        print(f"\n=-= {location.get_name()} ({self._state.get_time_string()}) =-=")
        print(location.get_description())
        input("     [Press Enter to continue...]")

        if loc_id == "town":
            if self._state.get_act() == 1:
                if "groundskeeper" in self._state.get_interrogated_suspects():
                    self._ui.speak("Diner Owner", "Groundskeeper was here eating soup at 10 PM. His alibi checks out completely!")
                    self._state.set_act(2)
                    print("\n" + "=" * 50)
                    print("=-= Plot Twist: Red Herring Detected! =-=")
                    print("The Groundskeeper was a red herring! New leads have opened up in town.")
                    print("=" * 50)
                    input("     [Press Enter to continue...]")
                else:
                    self._ui.speak("Diner Owner", "Can't say I noticed anything unusual around here lately.")
            else:
                self._interrogate_suspect("courier")
                if len(self._state.get_interrogated_suspects()) >= 5:
                    if self._state.get_act() == 2:
                        self._state.set_act(3)
                        if "meowbert" not in self._state.get_active_suspects():
                            self._state.add_active_suspect("meowbert")
                            print("\n" + "=" * 50)
                            print("=-= Breakthrough: Insurance Fraud =-=")
                            print("Financial records show Sir Meowbert insured the tuna.")
                            print("Sir Meowbert added to your Suspect List.")
                            print("=" * 50)
                            input("     [Press Enter to continue...]")
        else:
            for s_id in location.get_suspect_ids():
                self._interrogate_suspect(s_id)

    def _interrogate_suspect(self, suspect_id: str):
        suspects = self._case.get_suspects()
        suspect = suspects[suspect_id]

        self._ui.speak(suspect.get_name(), suspect.get_dialogue())

        clue_text = f"{suspect.get_name()}: {suspect.get_alibi()}"
        saved_note = self._ui.prompt_note_creation(clue_text)
        if saved_note:
            self._state.add_journal_entry(saved_note)

        self._state.record_interrogation(suspect_id)

        if len(self._state.get_interrogated_suspects()) >= 5 and self._state.get_act() == 2:
            self._state.set_act(3)
            if "meowbert" not in self._state.get_active_suspects():
                self._state.add_active_suspect("meowbert")
                print("\n" + "=" * 50)
                print("=-= Breakthrough: Insurance Fraud =-=")
                print("Financial records show Sir Meowbert insured the tuna.")
                print("Sir Meowbert added to your Suspect List.")
                print("=" * 50)
                input("     [Press Enter to continue...]")

    def accuse(self):
        if len(self._state.get_journal()) < 2:
            print("\n[!] You need at least 2 clues in your journal first.")
            input("     [Press Enter to continue...]")
            return False

        if self._state.get_act() < 3:
            print("\n[!] You don't have enough evidence linking anyone to a major conspiracy yet. Keep investigating!")
            input("     [Press Enter to continue...]")
            return False

        active_suspects = self._state.get_active_suspects()
        all_suspects = self._case.get_suspects()

        print("\n=-= Suspect List =-=")
        for idx, s_id in enumerate(active_suspects, 1):
            print(f"{idx}. {all_suspects[s_id].get_name()}")

        choice = input("Accuse suspect #: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(active_suspects):
                if active_suspects[idx] == "meowbert":
                    self._trigger_ending()
                    return True
                else:
                    print("\nDetective Paw: The evidence doesn't point to them. Keep digging.")
                    input("     [Press Enter to continue...]")
        return False

    def _trigger_ending(self):
        print("\n" + "=" * 50)
        print("Case Closed: Sir Meowbert staged the theft for insurance.")
        print("=" * 50)
        self._ui.speak("Sir Meowbert", "Curses! How did you figure out I hired the courier?!")
        self._ui.speak("Detective Paw", "The financial records and the courier's testimony don't lie. You staged the whole thing.")
        print("\n=-= Post-Game =-=")
        self._ui.speak("Detective Paw", "The gold flakes off the statue—it's cheap plastic! The REAL Golden Tuna is still missing...")
        print("\n[To be continued in Cat Noir 2... ]\n")

def choose_location(engine):
    locations = engine.get_case().get_locations()
    print("\nSelect Location:")
    loc_keys = list(locations.keys())

    for i, loc_id in enumerate(loc_keys, 1):
        print(f"{i}. {locations[loc_id].get_name()}")

    choice = input("Choice #: ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(loc_keys):
            engine.investigate_location(loc_keys[idx])


def display_journal(state):
    print("\n" + "=" * 15 + " Detective Journal " + "=" * 15)
    entries = state.get_journal()
    if not entries:
        print("No clues collected yet.")
    else:
        for i, entry in enumerate(entries, 1):
            print(f"{i}. {entry}")
    print("=" * 49)
    input("     [Press Enter to continue...]")


def main():
    engine = DetectiveEngine(case_1)

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(f" Cat Noir: {engine.get_case().get_title().upper()} ")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    input("     [Press Enter to start...]")

    if os.path.exists("savegame.json"):
        if input("Save file found. Load game? (y/n): ").strip().lower() in [
            "y",
            "yes",
        ]:
            engine.load_game()

    while True:
        state = engine.get_state()
        print(f"\nMain Menu [{state.get_time_string()}]:")
        print("1. Investigate Locations")
        print("2. Read Journal")
        print("3. Accuse Suspect")
        print("4. Save Progress")
        print("5. Save & Quit")

        choice = input("Select action (1-5): ").strip()

        if choice == "1":
            choose_location(engine)
        elif choice == "2":
            display_journal(state)
        elif choice == "3":
            if engine.accuse():
                break
        elif choice == "4":
            engine.save_game()
        elif choice == "5":
            if input("Save before quitting? (y/n): ").strip().lower() in [
                "y",
                "yes",
            ]:
                engine.save_game()
            print("\nGoodbye, Detective Paw.")
            break


if __name__ == "__main__":
    main()