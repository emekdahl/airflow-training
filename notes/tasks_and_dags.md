# DAGs and Tasks

## Demystifying scheduling

- `start_date`
- `schedule_interval` - frequency at which the DAG will be triggered
  - if you have a start date of january 1 2021 10 am and a schedule interval of 10 minutes, your DAG will be effectively triggered at 10:10 AM on January 1, 2021
  - airflow effectively runs the start date plus the scheduled interval has elapsed
  - the beginning of this period (10:00 AM) is the `execution date`
  - 10:10 am is the start_date
  - at 10:20 am, the second dag run will be created and run immediately
  - the execution date for dag run two is 2021-01-01 at 10:10 am and the start date is 10:20 am
- `end_date` - the date at which your dag won't be scheduled any more

## Playing with Start Date

- do NOT have one start date at the dag level and another at the operator level
- datetime is in UTC by default - this is a BEST PRACTICE
-
