class BankersAlgorithm:
    def __init__(self, max_resources, allocation):
        self.max_resources = max_resources
        self.allocation = allocation
        self.num_processes = len(allocation)
        self.num_resources = len(max_resources[0])
        self.available = self.calculate_available()
        self.need = self.calculate_need()

    def calculate_available(self):
        total_resources = [sum(r) for r in zip(*self.max_resources)]
        allocated_resources = [sum(r) for r in zip(*self.allocation)]
        return [total - allocated for total, allocated in zip(total_resources, allocated_resources)]

    def calculate_need(self):
        return [[self.max_resources[i][j] - self.allocation[i][j] for j in range(self.num_resources)]
                for i in range(self.num_processes)]

    def is_safe(self, request):
        available = self.available[:]
        allocation = [self.allocation[i][:] for i in range(self.num_processes)]
        need = [self.need[i][:] for i in range(self.num_processes)]

        # Temporarily allocate resources
        for i in range(self.num_processes):
            allocation[i] = [allocation[i][j] + request[j] if i == i else allocation[i][j] for j in range(self.num_resources)]
            need[i] = [need[i][j] - request[j] if i == i else need[i][j] for j in range(self.num_resources)]
        
        # Check for a safe sequence
        finish = [False] * self.num_processes
        safe_sequence = []
        while len(safe_sequence) < self.num_processes:
            found_process = False
            for i in range(self.num_processes):
                if not finish[i] and all(need[i][j] <= available[j] for j in range(self.num_resources)):
                    available = [available[j] + allocation[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    safe_sequence.append(i)
                    found_process = True
            if not found_process:
                return False
        return True

    def request_resources(self, process_index, request):
        if any(request[i] > self.need[process_index][i] for i in range(self.num_resources)):
            raise ValueError("Request exceeds maximum need.")
        if any(request[i] > self.available[i] for i in range(self.num_resources)):
            raise ValueError("Resources not available.")

        # Check if granting the request leaves the system in a safe state
        if self.is_safe(request):
            # Allocate resources
            self.available = [self.available[i] - request[i] for i in range(self.num_resources)]
            self.allocation[process_index] = [self.allocation[process_index][i] + request[i] for i in range(self.num_resources)]
            self.need[process_index] = [self.need[process_index][i] - request[i] for i in range(self.num_resources)]
            return True
        return False

def main():
    # Input number of processes and resources
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of resource types: "))

    # Input maximum resources for each process
    print("Enter the maximum resource matrix (each row separated by spaces):")
    max_resources = []
    for i in range(num_processes):
        max_resources.append(list(map(int, input(f"Max resources for Process {i}: ").strip().split())))

    # Input currently allocated resources for each process
    print("Enter the allocation matrix (each row separated by spaces):")
    allocation = []
    for i in range(num_processes):
        allocation.append(list(map(int, input(f"Allocated resources for Process {i}: ").strip().split())))

    banker = BankersAlgorithm(max_resources, allocation)

    # Request resources from the user
    process_index = int(input("Enter the process index to request resources (0 to {}): ".format(num_processes - 1)))
    request = list(map(int, input("Enter the resource request (space-separated): ").strip().split()))

    try:
        if banker.request_resources(process_index, request):
            print("Request granted.")
        else:
            print("Request denied.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
