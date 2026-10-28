# Cat Noir: Moddable Mystery Engine

A modular, text-based terminal mystery game built in Python featuring dynamic case loading and community mod pack support. Play as Detective Paw to investigate crime scenes, verify alibis, interrogate suspects, and solve complex cases.

## Architecture & Modding

The game engine is completely decoupled from story data. All triggers, suspects, locations, and custom endings are declared directly inside case files located in the `cases/` directory.

### Project File Structure
```
cat_noir/
├── main.py            # Dynamic case loader, menu system, and game loop
├── engine.py          # Generic rules evaluator & investigator
├── state.py           # GameState tracking (acts, time, journal, saves)
├── dialogue.py        # Dialogue pacing and `=-=` clue prompt UI
├── data_loader.py     # OOP classes (Suspect, Location, CaseData)
└── cases/
    └── case_1.py      # Official Case: The Case of the Golden Tuna
```

## Core Features

* **Dynamic Case Loader:** Automatically scans the `cases/` folder on startup so you can drop in new custom mystery files without modifying core engine code.
* **Manual Pacing:** Interactive pause prompts (`[Press Enter to continue...]`) keep text readable.
* **Organic Investigation Loops:** Act progression and plot twists trigger naturally through gameplay actions (such as verifying alibis in Town Square).
* **Customizable Journal & Saves:** Save default clues or write your own custom notes. Progress is serialized per case to unique JSON save files (`savegame_<case_id>.json`).

## Running the Game

1. Ensure your folder structure matches the layout above with a `cases/` subfolder.
2. Run the entry point:
   ```bash
   python main.py
   ```
3. Select your case from the terminal menu and begin your investigation.

## Creating a Custom Case

To create a mod pack, add a new `.py` file to the `cases/` directory, instantiate a `CaseData` object with your own custom dialogue and triggers, and run the game!
