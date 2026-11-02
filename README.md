# Cat Noir: Moddable Mystery Engine

A modular, text-based terminal mystery game built in Python. Play as Detective Paw to investigate crime scenes, verify alibis, interrogate suspects, and solve complex cases.

## Download and Play

No Python needed. Grab the file for your system from the [latest release](../../releases/latest):

| System  | File                    |
|---------|-------------------------|
| Windows | `cat_noir-windows.exe`  |
| macOS   | `cat_noir-macos`        |
| Linux   | `cat_noir-linux`        |

1. Download the file for your system and put it in its own folder (your save file is created next to it).
2. **Windows:** double-click it. If SmartScreen says "Windows protected your PC", click **More info**, then **Run anyway**. The warning appears because the app isn't code-signed.
3. **macOS / Linux:** open a terminal in the download folder and run `chmod +x cat_noir-macos` (or `cat_noir-linux`) once, then launch it with `./cat_noir-macos` (or `./cat_noir-linux`).

## Running from Source

1. Install Python 3.
2. Download or clone this repository.
3. From the project root, run:
   ```bash
   python main.py
   ```

## Project File Structure

Everything lives in the repository root, alongside this README:

```
cat_noir/
├── main.py            # Entry point, menu system, and game loop
├── engine.py          # Generic rules evaluator & investigator
├── state.py           # GameState tracking (acts, time, journal, saves)
├── dialogue.py        # Dialogue pacing and `=-=` clue prompt UI
├── data_loader.py     # OOP classes (Suspect, Location, CaseData)
├── README.md
├── data/
│   └── case_1.py      # Official Case: The Case of the Golden Tuna
└── .github/
    └── workflows/
        └── release.yml    # Builds the executables when a release tag is pushed
```

## Core Features

* **Engine and Story Data Separated:** Suspects, locations, and dialogue are declared in case files inside the `data/` folder, apart from the engine code.
* **Manual Pacing:** Interactive pause prompts (`[Press Enter to continue...]`) keep text readable.
* **Organic Investigation Loops:** Act progression and plot twists trigger naturally through gameplay actions (such as verifying alibis in Town Square).
* **Customizable Journal & Saves:** Save default clues or write your own custom notes. Progress is saved to `savegame.json` in the folder you run the game from.

## Creating a Custom Case

1. Add a new `.py` file to the `data/` folder that builds a `CaseData` object with your own suspects, locations, and dialogue (use `data/case_1.py` as a template).
2. In `main.py`, import your case and pass it to `DetectiveEngine` in place of `case_1`.
3. Run the game from source with `python main.py`.

## Building the Executables

Executables are built automatically with PyInstaller by GitHub Actions. To publish a new version, create a new release on GitHub with a new tag (for example `v1.0.1`). The workflow builds the Windows, macOS, and Linux files and attaches them to that release.
