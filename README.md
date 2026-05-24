# CLI Habit Tracker

A simple CLI-based habit tracker built with Python.  
This is my first no-tutorial Python project. The goal is not perfection — the goal is learning by building.

---

# 🎯 Objective

Track habits using CSV files and monitor consistency through streak systems.

The project focuses on:

- Saving habits to CSV files
- Loading habits from CSV files
- Updating habit data dynamically
- Tracking:
    - Current chain streak 🔥
    - Current break streak 💀
    - Maximum chain streak
    - Maximum break streak

### Main Philosophy

- Keep `current_chain_streak` growing
- Never let `current_break_streak` become larger than `1`

---

# 📦 Entities

---

## 1. Habit

Represents a single habit.

### Attributes

| Attribute | Type    | Description                                |
| --------- | ------- | ------------------------------------------ |
| `title`   | `str`   | Habit name                                 |
| `slug`    | `str`   | Auto-generated slug from title             |
| `target`  | `float` | Daily target amount                        |
| `unit`    | `str`   | Measurement unit (hours, reps, cups, etc.) |

---

### Methods

#### `Habit.set_title(new_title: str) -> Habit`

Updates the habit title and automatically regenerates the slug.

---

#### `Habit.set_target(new_target: float) -> Habit`

Updates the habit target.

---

#### `Habit.set_unit(new_unit: str) -> Habit`

Updates the habit measurement unit.

---

### Example

```py
habit = Habit("Workout", 50, "reps")

print(habit)
# Workout (x50 reps)
```

---

## 2. HabitContainer

Stores and manages multiple habits.

### Attributes

| Attribute     | Type          | Description                |
| ------------- | ------------- | -------------------------- |
| `habits_list` | `list[Habit]` | List containing all habits |

---

### Methods

#### `HabitContainer.import_from_csv(csv_path: str) -> HabitContainer`

Reads habits from a CSV file and loads them into memory.

Expected CSV format:

```csv
title,target,unit
Workout,50,reps
Reading,2,hours
```

---

#### `HabitContainer.save_to_csv(csv_path: str) -> None`

Saves all habits from memory into a CSV file.

---

#### `HabitContainer.print_habits() -> None`

Prints all habits in a readable CLI format.

---

### Example

```py
container = HabitContainer()

container.import_from_csv("./habits.csv")

container.print_habits()

container.save_to_csv("./habits.csv")
```

---

## 3. HabitProgress

Tracks streaks and consistency progress for a single habit.

### Attributes

| Attribute      | Type       | Description                              |
| -------------- | ---------- | ---------------------------------------- |
| `streak`       | `dict`     | Stores current/max chain & break streaks |
| `last_updated` | `datetime` | Last time streaks were updated           |

---

### Streak Structure

```py
{
    "current_chain_streak": 0,
    "current_break_streak": 0,
    "max_chain_streak": 0,
    "max_break_streak": 0
}
```

---

### Methods

#### `HabitProgress.done_today() -> HabitProgress`

Marks the habit as completed today.

Effects:

- Increases chain streak
- Resets break streak

---

#### `HabitProgress.undone_today() -> HabitProgress`

Marks the habit as missed today.

Effects:

- Increases break streak
- Resets chain streak

---

#### `HabitProgress.load_from_container(streak: dict, last_updated: datetime)`

Loads saved streak data and automatically updates missed days based on the time difference.

Example:

If the app was closed for 3 days, the break streak updates automatically.

---

### Example

```py
progress = HabitProgress()

progress.done_today()
progress.done_today()

print(progress.streak)
```

Possible output:

```py
{
    "current_chain_streak": 2,
    "current_break_streak": 0,
    "max_chain_streak": 2,
    "max_break_streak": 0
}
```

---

## 4. ProgressContainer

Stores and manages progress data for all habits.

---

### Internal Structure

```py
[
    {
        "slug": "habit-slug",
        "streak": {
            "current_chain_streak": int,
            "current_break_streak": int,
            "max_chain_streak": int,
            "max_break_streak": int
        },
        "last_updated": datetime
    }
]
```

---

### Attributes

| Attribute   | Type         | Description                                |
| ----------- | ------------ | ------------------------------------------ |
| `container` | `list[dict]` | List containing all habit progress records |

---

### Methods

#### `ProgressContainer.import_from_csv(csv_path: str) -> ProgressContainer`

Loads progress records from a CSV file.

Expected CSV format:

```csv
slug,current_chain_streak,max_chain_streak,current_break_streak,max_break_streak,last_updated
workout,5,10,0,2,2026-05-24 12:30:00
```

---

#### `ProgressContainer.write_to_csv(csv_path: str) -> ProgressContainer`

Saves all progress records into a CSV file.

---

#### `ProgressContainer.print_progress() -> None`

Prints all progress records in a readable CLI format.

Example output:

```txt
|================|
|=== Progress ===|
|================|

Workout
    Streak: 5              |   Best Streak: 10
    Break Streak: 0        |   Longest Break Streak: 2
    Last Updated At: 2026-05-24 12:30:00
-----------------------
```

---

#### `ProgressContainer.print_progress_by_slug(slug: str) -> None`

Prints progress data for a specific habit using its slug.

---

### Example

```py
progress_container = ProgressContainer()

progress_container.import_from_csv("./progress.csv")

progress_container.print_progress()

progress_container.print_progress_by_slug("workout")

progress_container.write_to_csv("./progress.csv")
```

---

# 🗂 Current Project Structure

```txt
project/
│
├── classes/
│   ├── Habit.py
│   ├── HabitContainer.py
│   ├── HabitProgress.py
│   └── ProgressContainer.py
│
├── habits.csv
├── progress.csv
│
└── main.py
```

---

# 📄 CSV Structures

## habits.csv

```csv
title,target,unit
Workout,50,reps
Reading,2,hours
Meditation,15,minutes
```

---

## progress.csv

```csv
slug,current_chain_streak,max_chain_streak,current_break_streak,max_break_streak,last_updated
workout,5,12,0,3,2026-05-24 12:30:00
reading,2,7,0,4,2026-05-24 12:30:00
```

---

# 🛠 Current Features

- [x] Create habits
- [x] Auto-generate slugs
- [x] Update habit data
- [x] Save habits to CSV
- [x] Load habits from CSV
- [x] Print habits in CLI
- [x] Track chain streaks
- [x] Track break streaks
- [x] Track maximum streaks
- [x] Auto-detect missed days
- [x] Save progress to CSV
- [x] Load progress from CSV
- [x] Print all progress records
- [x] Print progress by habit slug

---

# 🚧 Planned Features

- [ ] Interactive CLI menu
- [ ] Mark habits as done directly from CLI
- [ ] Better CSV parsing using Python's `csv` module
- [ ] Better exception handling
- [ ] Data validation
- [ ] Statistics dashboard
- [ ] Colored terminal output
- [ ] Persistent auto-sync system
- [ ] Unit tests
- [ ] JSON support
- [ ] SQLite support

---

# 📚 What I'm Learning

Through this project I'm practicing:

- Python OOP
- File handling
- CSV processing
- Dataclasses
- CLI application architecture
- State management
- Time/date handling
- Data persistence
- Clean code organization
- Problem solving without tutorials

---

# ⚠️ Notes

This project is intentionally beginner-level.

The focus is:

- consistency
- experimentation
- learning through mistakes
- improving structure gradually
- understanding how real projects evolve over time
