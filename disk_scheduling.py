import sys

def read_requests(file_path):
    requests = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.isdigit():
                requests.append(int(line))
    return requests

def fcfs(initial_head, requests):
    current_head = initial_head
    total_head_movement = 0
    for request in requests:
        total_head_movement += abs(current_head - request)
        current_head = request
    return total_head_movement

def scan(initial_head, requests, direction):
    requests.sort()
    current_head = initial_head
    total_head_movement = 0

    if direction == "inward":
        left = [r for r in requests if r < current_head]
        right = [r for r in requests if r >= current_head]

        for request in reversed(left):
            total_head_movement += abs(current_head - request)
            current_head = request

        total_head_movement += current_head
        current_head = 0

        for request in right:
            total_head_movement += abs(current_head - request)
            current_head = request

    elif direction == "outward":
        left = [r for r in requests if r <= current_head]
        right = [r for r in requests if r > current_head]

        for request in right:
            total_head_movement += abs(current_head - request)
            current_head = request

        total_head_movement += (4999 - current_head)
        current_head = 4999

        for request in reversed(left):
            total_head_movement += abs(current_head - request)
            current_head = request

    return total_head_movement

def c_scan(initial_head, requests):
    requests.sort()
    current_head = initial_head
    total_head_movement = 0

    left = [r for r in requests if r < current_head]
    right = [r for r in requests if r >= current_head]

    for request in right:
        total_head_movement += abs(current_head - request)
        current_head = request

    total_head_movement += (4999 - current_head)
    current_head = 0

    for request in left:
        total_head_movement += abs(current_head - request)
        current_head = request

    return total_head_movement

def main():
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py <initial_head_position> <file_path>")
        sys.exit(1)

    initial_head = int(sys.argv[1])
    file_path = sys.argv[2]

    requests = read_requests(file_path)

    fcfs_movements = fcfs(initial_head, requests)
    scan_movements = scan(initial_head, requests, direction="inward")
    c_scan_movements = c_scan(initial_head, requests)

    print(f"FCFS Total Head Movements: {fcfs_movements}")
    print(f"SCAN Total Head Movements: {scan_movements}")
    print(f"C-SCAN Total Head Movements: {c_scan_movements}")

if __name__ == "__main__":
    main()
