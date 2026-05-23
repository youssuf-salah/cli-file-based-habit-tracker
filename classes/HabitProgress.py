from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class HabitProgress:
  streak: dict
  last_updated: datetime

  def __init__(self: "HabitProgress") -> None:
    self.streak = {"current_chain_streak": 0, "current_break_streak": 0, "max_chain_streak": 0, "max_break_streak": 0}
    self.last_updated = datetime.now()
  
  def __increment_streak(self: "HabitProgress", type: str) -> "HabitProgress":
    self.streak[f"current_{type}_streak"] += 1
    if self.streak[f"max_{type}_streak"] < self.streak[f"current_{type}_streak"]:
      self.streak[f"max_{type}_streak"] = self.streak[f"current_{type}_streak"]
    return self
  
  def __break_streak(self: "HabitProgress", type: str) -> "HabitProgress":
    if self.streak[f"max_{type}_streak"] < self.streak[f"current_{type}_streak"]:
      self.streak[f"max_{type}_streak"] = self.streak[f"current_{type}_streak"]
    self.streak[f"current_{type}_streak"] = 0
    return self
  
  def __update_streak(self: "HabitProgress", increment_type: str, decrement_type: str) -> "HabitProgress":
    self.__increment_streak(increment_type).__break_streak(decrement_type)
    self.last_updated = datetime.now()
    return self

  def done_today(self: "HabitProgress") -> "HabitProgress":
    self.__update_streak("chain", "break")
    return self

  def undone_today(self: "HabitProgress") -> "HabitProgress":
    self.__update_streak("break", "chain")
    return self
  
  def load_from_container(self: "HabitProgress", streak: dict, last_updated: datetime):
    self.streak = streak
    
    days_diff: int = (datetime.now() - last_updated).days
    if days_diff >= 1:
      for i in range (0, days_diff):
        self.undone_today()

    return self
