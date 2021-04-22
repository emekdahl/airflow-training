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
- you can define start dates in the future
- you can also define start dates in the past - airflow with run all the non-triggered dag runs between the scheduled date and the current date
- DO NOT define the start date dynamically (datetime.now())

## Schedule interval

- use crontab.guru
- @daily
- @weekly
- @hourly
- timedelta(days=1) - superior to cron for things like "every 3 days" which can fall apart between end of feb and beginning of march
- None - dag will NEVER be automatically triggered by the scheduler - for manual or external trigger

## Backfilling and Catchup

- catchup=True - if we miss a DAG run, the DAG will attempt to run all prior missed DAGs when it skips
  - what happens when the start date is set in the past? if we set catchup parameter to false
- max_active_runs=1 - only one DAG can run at a time

## Focus on Operators

- if you put extracting and cleaning data on the same operator, then you will have to retry both tasks even if only one failed
- ONE OPERATOR, ONE TASK
- OPERATORS SHOULD BE IDEMPOTENT
- retry=5 - retry 5x
- retry_delay=timedelta(minutes=5)
- avoid repeating yourself by defining dictionary of default args
- if you specify parameters inside the class, those override the default_args
- check out the base operator meta in the airflow docs

## Executing Python Functions
