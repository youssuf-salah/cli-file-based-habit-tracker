## CLI Habit Tracker

Hi! This is my first ever no-tutorial Python project. It will probably suck, but the goal isn't perfection, it's just to learn.

### Objective

Save, access and update habits (in/to CSV files) and dynamically see chain streaks and break streaks.
The goal, is not to have "0" in the chain streak, and not to have more than "1" in the break streak.

### Entities

- **Habit**:
    - _Attributes_:
        1. [str]`title` (mandatory)
        2. [str]`slug` (dynamically created from `title`)
        3. [float]`target` (number or reps needed daily)
        4. [str]`unit` (how do you measure that habit (hours, reps, cups, etc..))
    - _Methods_:
        1. `Habit.set_title(self: "Habit", new_title: str) -> "Habit"` -> Changes the current `title` and `slug` based on `new_title`
        2. `Habit.set_target(self: "Habit", new_target: float) -> "Habit"` -> Changes the current `target` based on `new_target`
        3. `Habit.set_target(self: "Habit", new_unit: str) -> "Habit"` -> Changes the current `unit` based on `new_unit`
- **HabitContainer**:
    - _Attributes_:
        1. [list[Habit]]`habits_list` (mandatory)
    - _Methods_:
        1. `HabitContinainer.import_from_csv(self: "HabitContainer", csv_path: str) -> "HabitContainer"` -> Reads all rows (except the header) from a CSV and loads it into `self.habits_list`
        2. `HabitContinainer.save_to_csv(self: "HabitContainer", csv_path: str) -> "HabitContainer"` -> Saves the current habits in the `self.habits_list` to a CSV file with the structure `title,target,unit`
        3. `HabitContinainer.print_habits(self: "HabitContainer") -> None` -> Prints all the habit in the container in a readable way
