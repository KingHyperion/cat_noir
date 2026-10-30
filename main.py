import os
from data.case_1 import case_1
from engine import DetectiveEngine


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