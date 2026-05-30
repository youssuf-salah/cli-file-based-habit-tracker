def check_if_file_exists(path: str) -> bool:
  try:
    file = open(path, 'r', encoding="utf-8")
    file.close()
    return True
  except FileNotFoundError:
    print(f"There's no such file {path}. Please enter a valid path.")
    return False

def input_file_path() -> dict:
  habits_path = ""
  streaks_path = ""
  
  while True:
    print("habits.csv path:")
    habits = input()
    if check_if_file_exists(habits):
      habits_path = habits
      break
  while True:
    print("streaks.csv path:")
    streaks = input()
    if check_if_file_exists(streaks):
      streaks_path = streaks
      break
  
  return {"habits_path": habits_path, "streaks_path": streaks_path}
