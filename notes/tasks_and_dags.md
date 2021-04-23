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

- kwargs - you can get a lot of info by printing kwargs out
- ds - date
- you can pass your own params: `op_kwargs={'my_param': 42}`

## Sensors

- if you need to wait for something, say for a file to land, this is what you use to do it
- if you don't see your tool in admin -> add connection, you need to install the provider and then you can get the connection
- by default, the `extra` and `password` fields are encrypted
  - fernet key is used to encrypt data
- `poke_interval` determines the frequency at which the sensor checks

## Bash Operator

- easy to import and use

## Define the path

- set upstream - after.set_upstream(before)
- set downstream - before.set_downstream(after)
- bitshift operators - much easier!
  - first task >> second task >> third task
  - > >
  - <<
- chain() - list all tasks in order with commas
- cross_downstream() - the dependencies criss-cross in the DAG

## Exchanging Data

- xcoms allows you to exchange a small about of data between tasks
- ti.xcom_pull()
- ti.xcom_push()
- xcom is stored into database of airflow, so there is a size limitation -
  - sqlite - 2 GB in one xcom
  - postgres - 1 GB
  - SQL - 64 KB
- do NOT process data using xcoms not the least because of size limitations
- use them to share states and small amounts of data
