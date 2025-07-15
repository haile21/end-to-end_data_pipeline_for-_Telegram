from dagster import ScheduleDefinition
from jobs import ethiomed_data_pipeline

daily_schedule = ScheduleDefinition(
    job=ethiomed_data_pipeline,
    cron_schedule="0 6 * * *",  # Every day at 6 AM
    name="daily_data_ingestion",
)
