from dataclasses import dataclass

@dataclass
class Habit:
  title: str
  slug: str
  target: float
  unit: str

  def __init__(self: "Habit", title: str, target: float, unit: str) -> None:
    self.title = title
    self.target = target
    self.unit = unit
    self.slug = '-'.join(title.lower().split())
  
  def set_title(self: "Habit", new_title: str) -> "Habit":
    self.title = new_title
    self.slug = '-'.join(new_title.lower().split())
    return self
  
  def set_target(self: "Habit", new_target: float) -> "Habit":
    self.target = new_target
    return self
  
  def set_unit(self: "Habit", new_unit: str) -> "Habit":
    self.unit = new_unit
    return self
  
  def __repr__(self: "Habit") -> str:
    return f"Habit(title='{self.title}', slug='{self.slug}', target={self.target}, unit='{self.unit}')"
  
  def __str__(self: "Habit") -> str:
    return f"{self.title} (x{self.target} {self.unit})"