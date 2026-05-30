from classes.Habit import Habit
from classes.HabitContainer import HabitContainer

def import_habits(habits_file_path: str) -> HabitContainer:
  habit_container: HabitContainer = HabitContainer().import_from_csv(habits_file_path)
  habit_container.print_habits()
  return habit_container

def create_new_habit() -> Habit:
  print("Please enter the required details about your new habit:")
  title: str = input("Habit Title: ")
  unit: str = input("Measurement Unit (Cups, Steps, Sheets, Words, etc..): ")
  target: float = float(input("Target (Floating point number): "))
  return Habit(title, target, unit)
