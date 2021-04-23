# Executors

## Default Executor

- k8s
- behind the scenes, there is always a queue where tasks get pushed and pulled by workers
- sequential executor - tasks in order, one after the other (no parallel) b/c it is based on sqlite

## Concurrency

- parallelism - the max number of tasks that you can execute at the same time (by default 32)
- dag_concurrency - the number of tasks for a given dag that can be executed in parallel (by default 16)
- max_active_runs_per_dag - number of dag runs that can run at the same time for a given dag (by default 16)
- if parallelism is limited to 4, then regardless of max_active_runs_per_dag being 16, the concurrency will be 4
- max_active_runs - is in the dag object
- concurrency - param in the dag object that we can use to limit for a specific dag

## Scaling

- local executor - limited
- celery executor - as many tasks as you want - celery distributed task queue
- allows you to scale out and add as many machines and workers as you need
