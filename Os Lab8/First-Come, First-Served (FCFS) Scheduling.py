def fcfs_scheduling(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x['arrival_time'])

    current_time = 0
    waiting_time = 0

    for process in processes:
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']
        waiting_time += current_time - process['arrival_time']
        current_time += process['burst_time']

    avg_waiting_time = waiting_time / len(processes)
    return avg_waiting_time
