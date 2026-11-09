import json
import os
from dialogue import DialogueManager
from state import GameState

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
