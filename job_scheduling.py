# Job Scheduling using Greedy Algorithm

class Job:
    def __init__(self, job_id, deadline, profit, time):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit
        self.time = time


def job_scheduling(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)
    schedule = [None] * max_deadline
    total_profit = 0

    for job in jobs:
        for j in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if schedule[j] is None:
                schedule[j] = job
                total_profit += job.profit
                break

    return schedule, total_profit


jobs = [
    Job('J1', 2, 100, 1),
    Job('J2', 1, 19, 1),
    Job('J3', 2, 27, 1),
    Job('J4', 1, 25, 1),
    Job('J5', 3, 15, 1)
]

schedule, total_profit = job_scheduling(jobs)

print("Final Schedule:")
for i, job in enumerate(schedule):
    if job:
        print(f"Slot {i+1}: {job.job_id}")

print("Total Profit:", total_profit)
