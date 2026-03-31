# IPL Scheduler 🏏

A Python-based IPL (Indian Premier League) match scheduler that generates a full tournament schedule including league matches, venue assignment, day/time slots, and playoffs.

## Features
- Supports any number of teams (even or odd)
- Home & away round-robin match generation
- Automatic day and time scheduling (weekday/weekend logic)
- Venue assignment (home grounds or rotating stadiums)
- Rescheduling support mid-tournament
- Full playoff bracket (Qualifier 1, Eliminator, Qualifier 2, Final)

## How to Run
```bash
python main.py
```

## Requirements
Python 3.x — no external libraries needed.

## Project Structure
```
ipl-scheduler/
├── main.py
├── scheduler/
│   ├── matches.py
│   ├── days.py
│   ├── venue.py
│   ├── playoffs.py
│   └── display.py
├── README.md
└── .gitignore
```
