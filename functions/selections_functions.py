def input_selection_number(range: tuple) -> int:
  try:
    selection_str = input()
    selection = int(selection_str)
    if selection < range[0] or selection > range[1]:
      raise ValueError(f"Selection must be between {range[0]} & {range[1]}. You selected:", selection)
    return selection
  except TypeError or ValueError:
    print(f"Invalid value of {selection_str}. Please enter a straight number between {range[0]} & {range[1]}.")

def select_functionality() -> int:
  print("Please select one of the functionalities below (by typing its number):")
  print("1. Manage habits.")
  print("2. Manage progress.")
  print("3. Update file pathes (To import & save habits and streaks to).")
  print("4. Quit the app.")
  return input_selection_number((1, 4))

def habit_operation_selection() -> int:
  print("Please select one of the functionalities below (by typing its number):")
  print("1. Inspect habits.")
  print("2. Add habit.")
  print("3. Delete habit.")
  print("4. Edit habit.")
  print("5. Save habits to csv (recommended before going back to main screen).")
  print("6. Go back to main screen.")
  return input_selection_number((1, 6))

def streak_operation_selection() -> int:
  print("Please select one of the functionalities below (by typing its number):")
  print("1. Inspect habits streaks.")
  print("2. Inspect specific habit streak.")
  print("3. Mark habit as done today.")
  print("4. Save streaks to csv (recommended before going back to main screen).")
  print("5. Go back to main screen.")
  return input_selection_number((1, 5))
