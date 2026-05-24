from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProgressContainer:
  # [
  #   {
  #     "slug": "habit-slug",
  #     "streak": {
  #       "current_chain_streak": int,
  #       "current_break_streak": int,
  #       "max_chain_streak": int,
  #       "max_break_streak": int
  #     },
  #     "last_updated": datetime
  #   },
  #   ...
  # ]
  container: list[dict]

  def __init__(self: "ProgressContainer") -> None:
    self.container = []
  
  def import_from_csv(self: "ProgressContainer", csv_path: str) -> "ProgressContainer":
    try:
      with open(csv_path, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
          # slug,current_chain_streak,max_chain_streak,current_break_streak,max_break_streak,last_updated
          splitted = line.strip().split(",")

          last_updated_date = [int(item) for item in splitted[5].split(" ")[0].split("-")]
          last_updated_time = [int(item) for item in splitted[5].split(" ")[1].split(":")]
          last_updated_datetime = datetime(last_updated_date[0], last_updated_date[1], last_updated_date[2], last_updated_time[0], last_updated_time[1], last_updated_time[2])

          progress_dict = {
            "slug": splitted[0],
            "streak": {
              "current_chain_streak": int(splitted[1]),
              "max_chain_streak": int(splitted[2]),
              "current_break_streak": int(splitted[3]),
              "max_break_streak": int(splitted[4]),
            },
            "last_updated": last_updated_datetime
          }
          self.container.append(progress_dict)
      return self
    except FileNotFoundError:
      print(f"Error: Couldn't find the file `{csv_path}`.")
      exit(1)

  def write_to_csv(self: "ProgressContainer", csv_path: str) -> "ProgressContainer":
    try:
      with open(csv_path, "w", encoding="utf-8") as f:
        f.write("slug,current_chain_streak,max_chain_streak,current_break_streak,max_break_streak,last_updated\n")
        for record in self.container:
          f.write(f"{record["slug"]},{record["streak"]["current_chain_streak"]},{record["streak"]["max_chain_streak"]},{record["streak"]["current_break_streak"]},{record["streak"]["max_break_streak"]},{record["last_updated"]}\n")
      return self
    except:
      print(f"Error: Couldn't save progress to `{csv_path}`.")
      exit(1)

  def __print_progress_list(self: "ProgressContainer", progress_list: list[dict]) -> None:
    print("""\
|================|
|=== Progress ===|
|================|\
""")
    for record in progress_list:
      print(" ".join(record["slug"].split("-")).capitalize())
      print(f"\tStreak: {record["streak"]["current_chain_streak"]}\t\t|\tBest Streak: {record["streak"]["max_chain_streak"]}")
      print(f"\tBreak Streak: {record["streak"]["current_break_streak"]}\t\t|\tLongest Break Streak: {record["streak"]["max_break_streak"]}")
      print(f"\tLast Updated At: {record["last_updated"]}")
      print("-----------------------")

  def print_progress(self: "ProgressContainer") -> None:
    self.__print_progress_list(self.container)
  
  def print_progress_by_slug(self: "ProgressContainer", slug: str) -> None:
    progress_list = [item for item in self.container if item["slug"] == slug]
    self.__print_progress_list(progress_list)