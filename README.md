# Fruit Slicer

A fun **Fruit Ninja**-style arcade game made with **Pygame** as a school
project.

Slice fruits flying across the screen by pressing the **first letter of
each fruit name in French** before they disappear. Beware of bombs!

## Screenshots

*(Add gameplay, menu and game over screenshots here when ready)*

## Features

-   Different fruit types: watermelon, pineapple, ice, bomb\
-   Predefined curved flight paths\
-   Scoring system\
-   3 lives (hearts)\
-   Main menu screen\
-   Game Over screen with final score display\
-   Background music\
-   Winter mode (alternative background)

## Controls

The controls are based on the **first letter of the fruit name in
French**, making the game intuitive and easy to learn.

  Key   Fruit (French)   Action
  ----- ---------------- ------------------------------------
  P     Ananas           Slice pineapple
  P     Pastèque         Slice watermelon
  G     Glaçon           Activate ice / winter mode
  B     Bombe            Trigger bomb (penalty)
  ESC   ---              Quit (depending on current screen)

## Installation & Running

### Requirements

-   Python 3.8+
-   Pygame (`pip install pygame`)

### Steps

``` bash
# Clone the repository
git clone https://github.com/your-username/fruit-slicer.git
cd fruit-slicer

# (optional) virtual environment
python -m venv venv
source venv/bin/activate          # Linux / macOS
venv\Scripts\activate           # Windows

# Install dependency
pip install pygame

# Launch the game
python main.py
```

## Project Structure

``` text
fruit-slicer/
├── main.py                 # Entry point & main loop
├── menu.py                 # Start menu
├── gameplay_typing.py      # Core gameplay logic
├── game_over.py            # Game over screen
├── coordinates.py          # Fruit movement paths
├── final_score.py          # (generated) last score
├── Assets/
│   ├── images/             # sprites, backgrounds, UI elements
│   └── music/              # background music & sounds
├── README.md
└── .gitignore
```

## Planned / Possible Improvements

-   Multiple fruits moving simultaneously\
-   Real slicing animation & particle effects\
-   Combo system & score multipliers\
-   Sound effects (slice, explosion...)\
-   High-score table with persistence\
-   Difficulty progression\
-   Pause menu & settings\
-   Mobile / touch controls (future)

## Authors

-   **Narasoa Andoniaina**
-   **Childebert Bouachi** 🍉🔪

## License

School project --- All rights reserved\
*(You may switch to MIT if you decide to open-source it)*

*Last updated: February 2026*
