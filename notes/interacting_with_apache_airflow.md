# Interacting with Apache Airflow

## 3 ways to Interact

- UI
  - check dag runs
- Command Line Interface (CLI)
  - upgrade airflow
  - initialize airflow
  - if you don't have access to the UI
- REST API
  - when you want to build something on top of airflow
  - or when you want to trigger a dag in relation to something that happens in a customer-facing app

## DAG View - UI

- can toggle a DAG off and on
- view the owner of the DAG
- runs
  - status of current and past DAG runs
- schedule
  - interval of time at which the DAG is triggered
- last run
  - last time the DAG ran - executing date is the beginning of the scheduled period
- recent tasks
  - see the status of recent tasks
  - only current or most recent
- actions
  - trigger manually (needs toggle on)
  - delete the dag - it doesn't delete the file, only the metadata
- links to other views

## Tree View

- squares - DAG runs
- circles - tasks
- dark green - success
- light green - running
- red - failure

## Graph View

- check the dependencies
- get the status of the latest dag run
- hover over the tasks to get information
- hover over one task and the blue outlines show the relationships between the tasks
- the background of the tasks corresponds to the type of task, so look at the legend in the top right
- auto-refresh toggle on to automatically update the view as your pipeline progresses

## Gantt View

- the gantt view shows how long tasks are running
- looking at the overlaps, we can see which tasks are running parallel
- especially good at IDing bottlenecks

## Graph View

- if you click on a node -> `log` -> to look at logs
- `instance details` provides more information about the task instance attributes
- `Rendered` - gives you the output of the data you inject into your task at runtime
- `Log` - task instance logs
- `All Instances` - check all task instances across all dag runs
- `Filter Upstream` - your task plus upstream tasks

### Task Actions

- `Run` - run task instance
- `Clear` - if a task is in failure, fix the issue, then clear it to RETRY
- `Mark Failed` - figure out how tasks depending on your current task behave
- `Mark Success` - ditto

## Commands to Know

- `docker exec -it <container-id> /bin/bash`
- once inside airflow
  - `airflow db init` - execute this first, initializes the db and gives you the files and folders you need
  - `airflow db upgrade` - upgrade the airflow instance
  - `airflow db reset` - hard reset - use with caution
- `airflow webserver`
- `airflow scheduler`
- `airflow celery worker`

### Interact with DAGS

- `airflow dags pause` or `airflow dags unpause`
- `airflow dags trigger` - trigger a DAG from the CLI
  - specify an execution date with the `-e`
- `airflow dags list`
- `airflow tasks test example_dag bash_print_date1 2021-01-01` - test task before committing
- `airflow dags backfill -s 2021-01-01 2021-01-04 --reset_dagruns example_dag` - rerun past DAG runs
