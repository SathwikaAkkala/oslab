class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = 0
        self.completion_time = 0

def sjf_scheduling(processes):
    processes.sort(key=lambda p: (p.arrival_time, p.burst_time))
    n = len(processes)
    
    time = 0
    completed = 0
    ready_queue = []
    index = 0
    
    while completed < n:
        while index < n and processes[index].arrival_time <= time:
            ready_queue.append(processes[index])
            ready_queue.sort(key=lambda p: p.burst_time)  # Sort by burst time (shortest job first)
            index += 1
        
        if ready_queue:
            current_process = ready_queue.pop(0)
            start_time = time
            current_process.response_time = start_time - current_process.arrival_time
            time += current_process.burst_time
            current_process.completion_time = time
            current_process.waiting_time = start_time - current_process.arrival_time
            current_process.turnaround_time = current_process.waiting_time + current_process.burst_time
            completed += 1
        else:
            time += 1  # Move time forward if no processes are ready yet

def calculate_metrics(processes):
    total_waiting_time = sum(p.waiting_time for p in processes)
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    num_processes = len(processes)
    
    average_waiting_time = total_waiting_time / num_processes
    average_turnaround_time = total_turnaround_time / num_processes
    throughput = num_processes / (processes[-1].completion_time if processes else 1)  # Avoid division by zero
    
    return average_waiting_time, average_turnaround_time, throughput

def print_processes(processes):
    print(f"{'Process ID':<12}{'Arrival Time':<15}{'Burst Time':<10}{'Response Time':<15}{'Waiting Time':<15}{'Turnaround Time':<20}{'Completion Time':<20}")
    for process in processes:
        print(f"{process.process_id:<12}{process.arrival_time:<15}{process.burst_time:<10}{process.response_time:<15}{process.waiting_time:<15}{process.turnaround_time:<20}{process.completion_time:<20}")

def print_gantt_chart(processes):
    max_completion_time = max(p.completion_time for p in processes)
    
    print("\nGantt Chart:")
    time_line = [" "] * (max_completion_time + 1)
    process_start_times = {}
    
    for process in processes:
        for t in range(process.response_time, process.completion_time):
            time_line[t] = process.process_id
        process_start_times[process.process_id] = process.response_time
    
    # Print the time line with process IDs
    print("".join(time_line))
    print(" ".join(f"{i:2}" for i in range(max_completion_time + 1)))
    
    # Print the process IDs above the timeline
    ids_line = [" "] * (max_completion_time + 1)
    for process_id, start_time in process_start_times.items():
        ids_line[start_time] = process_id[0]  # Print the first character of the process ID
    
    print("".join(ids_line))

def main():
    processes = []
    n = int(input("Enter the number of processes: "))

    for i in range(n):
        process_id = f"P{i+1}"
        arrival_time = int(input(f"Enter arrival time for process {process_id}: "))
        burst_time = int(input(f"Enter burst time for process {process_id}: "))
        processes.append(Process(process_id, arrival_time, burst_time))
    
    sjf_scheduling(processes)
    
    avg_waiting_time, avg_turnaround_time, throughput = calculate_metrics(processes)
    
    print_processes(processes)
    
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Throughput: {throughput:.2f} processes/unit time")
    
    print_gantt_chart(processes)

if __name__ == "__main__":
    main()
