def min_cost_climbing_stairs(cost: list[int]) -> int:
    min_step_costs = []

    for i, cost in enumerate(cost):
        if i < 2:
            min_step_costs.append(cost)
        else:
            min_cost_reach_step = min(min_step_costs[i - 1], min_step_costs[i - 2])
            min_step_costs.append(cost + min_cost_reach_step)

    return min(min_step_costs[-1], min_step_costs[-2])


def main():
    print(min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]))


if __name__ == '__main__':
    main()
