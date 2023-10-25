def priority_scheduling(processes):
    processes.sort(key=lambda x: x['priority'])
    current_time = 0
    waiting_time = 0

    for process in processes:
        waiting_time += max(0, current_time - process['arrival_time'])
        current_time += process['burst_time']

    avg_waiting_time = waiting_time / len(processes)
    return avg_waiting_time
