class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = 0
        self.completion_time = 0

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort processes by arrival time
    
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time  # Wait for the process to arrive
        process.response_time = current_time - process.arrival_time
        process.waiting_time = process.response_time
        process.turnaround_time = process.waiting_time + process.burst_time
        process.completion_time = current_time + process.burst_time
        current_time += process.burst_time  # Move to the end of the current process

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
    
    for process in processes:
        for t in range(process.response_time, process.completion_time):
            time_line[t] = process.process_id
    
    # Printing the time line
    print("".join(time_line))
    print(" ".join(f"{i:2}" for i in range(max_completion_time + 1)))

def main():
    processes = []
    n = int(input("Enter the number of processes: "))

    for i in range(n):
        process_id = f"P{i+1}"
        arrival_time = int(input(f"Enter arrival time for process {process_id}: "))
        burst_time = int(input(f"Enter burst time for process {process_id}: "))
        processes.append(Process(process_id, arrival_time, burst_time))
    
    fcfs_scheduling(processes)
    
    avg_waiting_time, avg_turnaround_time, throughput = calculate_metrics(processes)
    
    print_processes(processes)
    
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Throughput: {throughput:.2f} processes/unit time")
    
    print_gantt_chart(processes)

if __name__ == "__main__":
    main()

