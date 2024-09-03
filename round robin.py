def calculate_times(processes, arrival_times, burst_times, time_quantum):
    n = len(processes)
    remaining_burst_times = burst_times[:]
    waiting_times = [0] * n
    turnaround_times = [0] * n
    response_times = [-1] * n
    completion_times = [0] * n
    gantt_chart = []

    current_time = 0
    processes_remaining = n
    queue = []

    while processes_remaining > 0:
        process_executed = False
        for i in range(n):
            if remaining_burst_times[i] > 0:
                if response_times[i] == -1:  # Process not started yet
                    response_times[i] = current_time - arrival_times[i]

                execution_time = min(time_quantum, remaining_burst_times[i])
                gantt_chart.append((processes[i], current_time, current_time + execution_time))

                current_time += execution_time
                remaining_burst_times[i] -= execution_time

                if remaining_burst_times[i] == 0:
                    completion_times[i] = current_time
                    turnaround_times[i] = completion_times[i] - arrival_times[i]
                    waiting_times[i] = turnaround_times[i] - burst_times[i]
                    processes_remaining -= 1

                process_executed = True
        
        if not process_executed:
            break

    return waiting_times, turnaround_times, response_times, completion_times, gantt_chart

def calculate_averages(waiting_times, turnaround_times):
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    return avg_waiting_time, avg_turnaround_time

def calculate_throughput(processes, completion_times):
    total_time = max(completion_times)
    throughput = len(processes) / total_time
    return throughput

def print_gantt_chart(gantt_chart):
    print("\nGantt Chart:")
    for process, start, end in gantt_chart:
        print(f"| {process:<8} ({start}-{end})", end=' ')
    print("|")

def main():
    num_processes = int(input("Enter the number of processes: "))
    
    processes = []
    arrival_times = []
    burst_times = []
    
    for i in range(num_processes):
        process_name = input(f"Enter name for process {i + 1}: ")
        arrival_time = int(input(f"Enter arrival time for process {process_name}: "))
        burst_time = int(input(f"Enter burst time for process {process_name}: "))
        processes.append(process_name)
        arrival_times.append(arrival_time)
        burst_times.append(burst_time)
    
    time_quantum = int(input("Enter the time quantum: "))
    
    # Calculate waiting times, turnaround times, response times, completion times, and Gantt chart
    waiting_times, turnaround_times, response_times, completion_times, gantt_chart = calculate_times(processes, arrival_times, burst_times, time_quantum)
    
    # Calculate averages and throughput
    avg_waiting_time, avg_turnaround_time = calculate_averages(waiting_times, turnaround_times)
    throughput = calculate_throughput(processes, completion_times)
    
    # Print results
    print("\nProcess-wise Metrics:")
    for i in range(num_processes):
        print(f"Process {processes[i]}: Arrival Time: {arrival_times[i]}, Burst Time: {burst_times[i]}, Waiting Time: {waiting_times[i]}, Turnaround Time: {turnaround_times[i]}, Response Time: {response_times[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Throughput: {throughput:.2f} processes per unit time")
    
    # Print Gantt chart
    print_gantt_chart(gantt_chart)

if __name__ == "__main__":
    main()
