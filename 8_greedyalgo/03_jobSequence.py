def jobScheduling(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sorting by profit (x[2] is the profit)
    
    # Find the maximum deadline
    maxi = max(job[1] for job in jobs)  # Find the maximum deadline
    
    # Initialize result variables
    countJobs = 0
    jobProfit = 0
    
    # Initialize an array to store job schedule (None means no job scheduled)
    ans = [-1] * (maxi + 1)
    
    # Traverse each job in the sorted order
    for job in jobs:
        job_id, job_deadline, job_profit = job# idi same job_id=jobs[0] next[1] ala automatic the python ey ichesiddi corresponding values
        
        # Try to schedule the job starting from its deadline and going backwards
        for j in range(job_deadline, 0, -1):
            if ans[j] == -1:  # If the slot is free
                ans[j] = job_id  # Schedule the job
                countJobs += 1
                jobProfit += job_profit
                break
    
    return countJobs, jobProfit


if __name__ == "__main__":
    # List of jobs (job_id, deadline, profit)
    jobs = [(1, 4, 20), (2, 1, 10), (3, 2, 40), (4, 2, 30)]
    
    # Call jobScheduling function
    count, profit = jobScheduling(jobs)
    
    # Output the result
    print(count, profit)
