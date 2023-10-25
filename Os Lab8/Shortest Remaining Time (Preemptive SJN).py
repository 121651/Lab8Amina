def srt_scheduling(processes):
    current_time = 0
    remaining_time = [process['burst_time'] for process in processes]
    waiting_time = 0

    while True:
        min_time = float('inf')
        next_process = None

        for i, process in enumerate(processes):
            if process['arrival_time'] <= current_time and remaining_time[i] < min_time:
                min_time = remaining_time[i]
                next_process = i

        if next_process is None:
            current_time += 1
            continue

        remaining_time[next_process] -= 1
        current_time += 1

        if remaining_time[next_process] == 0:
            waiting_time += current_time - processes[next_process]['arrival_time']

        if sum(remaining_time) == 0:
            break

    avg_waiting_time = waiting_time / len(processes)
    return avg_waiting_time
