from dataclasses import dataclass
from Habit import Habit

@dataclass
class HabitContainer:
  habits_list: list[Habit]

  def __init__(self: "HabitContainer") -> None:
    self.habits_list = []

  def import_from_csv(self: "HabitContainer", csv_path: str) -> "HabitContainer":
    try:
      with open(csv_path, "r", encoding="utf-8") as f:
        # Line format:
        # title,target,unit
        next(f)
        for line in f:
          splitted = line.strip().split(",")
          new_habit: Habit = Habit(splitted[0].strip(), float(splitted[1].strip()), splitted[2].strip())
          self.habits_list.append(new_habit)
      return self
    except FileNotFoundError:
      print(f"Can't find file in {csv_path}")
      exit(1)
  
  def save_to_csv(self: "HabitContainer", csv_path: str) -> None:
    try:
      with open(csv_path, "w", encoding="utf-8") as f:
        f.write("title,target,unit\n")
        for habit in self.habits_list:
          f.write(f"{habit.title},{habit.target},{habit.unit}\n")
    except:
      print(f"Unable to save habits to `{csv_path}`")
      exit(1)

  def print_habits(self: "HabitContainer") -> None:
    print("""\
|==============|
|=== Habits ===|
|==============|\
""")
    for habit in self.habits_list:
      print(f"""\
- Title: {habit.title}
- Target: x{habit.target} {habit.unit}
-----------------------\
""")
