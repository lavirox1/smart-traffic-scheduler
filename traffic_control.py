def pick_signal(traffic: dict) -> str:
    if sum(traffic.values()) == 0:
        return "none"
    order = ["North", "East", "West", "South"]
    lane = max(traffic, key=lambda x: (traffic[x], -order.index(x)))
    return lane

def calculate_waiting_time(traffic: dict, green_lane: str, green_time: int) -> tuple[dict, int]:
    if traffic[green_lane] >= green_time:
        traffic[green_lane] -= green_time
        cleared_cars = green_time
    else:
        cleared_cars = traffic[green_lane]
        traffic[green_lane] = 0
    return traffic, cleared_cars

def simulate_signal(traffic: dict, max_green_time: int) -> dict:
    total_cleared = 0
    cycle_logs = []
    initial_traffic = traffic.copy()
    
    while sum(traffic.values()) > 0:
        lane = pick_signal(traffic)
        if lane == "none":
            break
        cars_before = traffic[lane]
        green_time = min(cars_before, max_green_time)
        traffic, cleared_this_cycle = calculate_waiting_time(traffic, lane, green_time)
        total_cleared += cleared_this_cycle
        cycle_logs.append((lane, cars_before, green_time, cleared_this_cycle))
    
    stats = {
        "initial_traffic": initial_traffic,
        "total_cleared": total_cleared,
        "remaining": traffic,
        "cycles_run": len(cycle_logs),
        "cycle_logs": cycle_logs
    }
    return stats

def print_stats(stats):
    print()
    print(f"{'Cycle':<6}{'Green Lane':<12}{'Cars Before':<12}{'Green Time':<12}{'Cleared':<8}")
    print("-" * 60)
    for i, (lane, cars_before, green_time, cleared) in enumerate(stats['cycle_logs'], 1):
        print(f"{i:<6}{lane:<12}{cars_before:<12}{green_time:<12}{cleared:<8}")
    print("\nSummary:")
    print(f"Total cars cleared: {stats['total_cleared']}")
    print("Initial Traffic:", stats['initial_traffic'])
    print(f"Remaining traffic: {stats['remaining']}")
    print(f"Cycles run: {stats['cycles_run']}")

def get_values():
    traffic = {}
    lanes = ['North', 'East', 'West', 'South']
    for lane in lanes:
        traffic[lane] = int(input(f"Enter traffic in {lane} lane: "))
    max_green_time = int(input("Enter maximum green time per signal: "))
    return traffic, max_green_time

def main():
    traffic, max_green_time = get_values()
    stats = simulate_signal(traffic, max_green_time)
    print_stats(stats)

if __name__ == "__main__":
    main()
