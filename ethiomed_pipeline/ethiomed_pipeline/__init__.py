#Then register the scheduler  in your ethiomed_pipeline/__init__.py:
from .jobs import ethiomed_data_pipeline
from .schedules import daily_schedule

__all__ = ["ethiomed_data_pipeline", "daily_schedule"]

