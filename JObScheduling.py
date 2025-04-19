class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

n = int(input("Enter the no of Job you want to enter: "))
jobs = []
print("Enter the details of the Job:")
for i in range(n):
    print("Job", i + 1, ":")
    id = int(input("Enter the id of Job: "))
    deadline = int(input("Enter the deadline of Job: "))
    profit = int(input("Enter the profit of Job: "))
    jobs.append(Job(id, deadline, profit))

jobs.sort(key=lambda x: x.profit, reverse=True)

maxDeadline = max(job.deadline for job in jobs)

slots = [0] * (maxDeadline + 1)

totalProfit = 0
for job in jobs:
    for i in range(job.deadline, 0, -1):
        if slots[i] == 0:
            slots[i] = job.id
            totalProfit += job.profit
            break

print("Scheduled Jobs:", end=" ")
for i in range(1, len(slots)):
    if slots[i] != 0:
        print(slots[i], end=" ")
print("\nTotal Profit:", totalProfit)