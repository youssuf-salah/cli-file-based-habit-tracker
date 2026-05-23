# CLI Habit Tracker

A simple CLI-based habit tracker built with Python.  
This is my first no-tutorial Python project. The goal is not perfection — the goal is learning by building.

---

## 🎯 Objective

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

### Methods

#### `Habit.set_title(new_title: str) -> Habit`

Updates the habit title and automatically regenerates the slug.

```py
habit.set_title("Read Books")
```

---

#### `Habit.set_target(new_target: float) -> Habit`

Updates the habit target.

```py
habit.set_target(2)
```

---

#### `Habit.set_unit(new_unit: str) -> Habit`

Updates the habit measurement unit.

```py
habit.set_unit("hours")
```

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

Example output:

```txt
|==============|
|=== Habits ===|
|==============|

- Title: Workout
- Target: x50 reps
-----------------------
```

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

Tracks streaks and consistency progress.

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

Loads saved streak data and automatically updates missed days based on time difference.

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

# 🗂 Current Project Structure

```txt
project/
│
├── classes/
│   ├── Habit.py
│   ├── HabitContainer.py
│   └── HabitProgress.py
│
└── main.py
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

---

# 🚧 Planned Features

- [ ] Interactive CLI menu
- [ ] Habit completion logging
- [ ] Multiple habit progress tracking
- [ ] Better CSV structure
- [ ] Persistent streak storage
- [ ] Statistics system
- [ ] Colored terminal output
- [ ] Unit tests
- [ ] Better error handling

---

# 📚 What I'm Learning

Through this project I'm practicing:

- Python OOP
- File handling
- CSV processing
- Dataclasses
- State management
- CLI application structure
- Clean code organization
- Problem solving without tutorials

---

# ⚠️ Notes

This project is intentionally beginner-level.

The focus is:

- consistency
- experimentation
- learning through mistakes
- improving project structure over time

```

```
