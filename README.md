# Asteroids: A Classic Arcade Shooter in Python

## Project Status

**Active** — v1 includes the core gameplay loop: a controllable ship, shooting, asteroids spawning from the screen edges, and asteroids splitting into smaller pieces when hit. Expanding to add scoring, lives, power-ups, and visual polish (see the roadmap below).

## Overview

A recreation of the classic arcade game *Asteroids*, built with Python and pygame. The player pilots a ship through a field of drifting asteroids and shoots them down. Large asteroids break into smaller, faster fragments when hit, and the smallest ones are destroyed outright. Colliding with an asteroid ends the game.

This project was built as part of the [Boot.dev](https://www.boot.dev) backend development curriculum, as practice in object-oriented programming, game loops, and working with an external library.

## Tools & Methods

- **Python** — core language
- **pygame** — rendering, input handling, sprite groups, and the game loop
- **uv** — dependency and environment management
- Object-oriented design using a shared `CircleShape` base class for all game objects
- Circle-based collision detection between the player, shots, and asteroids
- Frame-rate-independent movement using delta time (`dt`)

## Controls

| Key | Action |
|---|---|
| **W** | Move forward |
| **S** | Move backward |
| **A** | Rotate left |
| **D** | Rotate right |
| **Space** | Shoot |

## How to Run

**Requirements:** Python 3 and [uv](https://docs.astral.sh/uv/)

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/asteroids.git
   cd asteroids
   ```
2. Run the game:
   ```bash
   uv run main.py
   ```

uv installs pygame and any other dependencies automatically the first time you run the game.

## Next Steps / Roadmap

- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Give the ship a triangular hitbox instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

## Repo Structure

```
├── main.py            # entry point: game loop, sprite groups, collision checks
├── player.py          # player ship: movement, rotation, shooting
├── shot.py            # projectiles fired by the player
├── asteroid.py        # asteroid behavior, including splitting on hit
├── asteroidfield.py   # spawns asteroids from the edges of the screen
├── circleshape.py     # base class with shared position, velocity, and collision logic
├── constants.py       # screen size, speeds, radii, and other tunable values
├── logger.py          # event and game-state logging (provided by Boot.dev)
├── pyproject.toml     # project metadata and dependencies
├── .gitignore
└── README.md
```

## Acknowledgments

Project structure and guidance provided by [Boot.dev](https://www.boot.dev).
