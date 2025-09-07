import random as r


def add_traffic(traffic: dict, traffic_condition:str = 'medium') -> tuple[dict, dict]:
    # traffic coming following normal distribution (mean =2, sd = 2)
    
    match traffic_condition:
        case 'high':
            mean = 5
        case 'medium':
            mean = 3
        case 'low':
            mean = 1
    

    new_added = {}
    for d in traffic:
        new_cars = max(0, int(r.gauss(mean, 1)))
        traffic[d] += new_cars
        new_added[d] = new_cars
    return traffic, new_added


def clear_traffic(traffic: dict, cycles: int = 10, traffic_condition : str = 'medium'):
    # uses weighted adaptive round robin scheduling
    for cycle in range(1, cycles + 1):
        print(f"\n\n===== Cycle {cycle} =====")

        total = sum(traffic.values())
        if total == 0:
            print("No traffic waiting.")
        else:
            print(f"{'Direction':<11} {'Before':<9} {'Quantum':<9} {'Cleared':<9} {'Remaining':<10}")
            print("-" * 55)

            for direction in list(traffic.keys()):
                before = traffic[direction]  # store before removal
                if before > 0:
                    q = max(1, before // 4)  # adaptive quantum
                    cleared = min(q, before)
                    traffic[direction] -= cleared
                    print(
                        f"{direction.capitalize():<11} {before:<9} {q:<9} {cleared:<9} {traffic[direction]:<10}"
                    )
                else:
                    print(f"{direction.capitalize():<11} {0:<9} {0:<9} {0:<9} {0:<10}")

        # new cars arrive
        traffic, new_added = add_traffic(traffic, traffic_condition)

        print("\nNew cars this cycle:")
        for d, n in new_added.items():
            print(f"{d.capitalize():<7}: +{n}")

        print("\nUpdated traffic:")
        for d, n in traffic.items():
            print(f"{d.capitalize():<7}: {n}")

    print("\nSimulation complete!!!!!")


def get_values():
    traffic = {}
    print()
    traffic['north'] = int(input("Enter number of cars in North Lane: "))
    traffic['east'] = int(input("Enter number of cars in East Lane: "))
    traffic['south'] = int(input("Enter number of cars in South Lane: "))
    traffic['west'] = int(input("Enter number of cars in West Lane: "))

    cycles = int(input("Enter number of cycles to run: "))

    traffic_condition = input("Enter traffic conditions (high, medium, low) : ")

    return traffic,cycles,traffic_condition


def main():
    
    traffic,cycles,traffic_condition = get_values()

    print("\nInitial traffic:")
    for d, n in traffic.items():
            print(f"{d.capitalize():<7}: {n}")
    clear_traffic(traffic, cycles, traffic_condition)


if __name__ == "__main__":
    main()
