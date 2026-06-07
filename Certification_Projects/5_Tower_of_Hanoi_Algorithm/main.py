def hanoi_recursive_algorithm(disk_count: int, tower_dictionary: dict[str, list[int]], source_tower: str, destination_tower: str, auxiliary_tower: str) -> str:
    solution_steps: str = ""
    if disk_count == 1:
        tower_dictionary[destination_tower].append(tower_dictionary[source_tower].pop())
        return f"{str(tower_dictionary["tower1"])} {str(tower_dictionary["tower2"])} {str(tower_dictionary["tower3"])}\n"

    solution_steps += hanoi_recursive_algorithm(disk_count - 1, tower_dictionary, source_tower, auxiliary_tower, destination_tower)
    tower_dictionary[destination_tower].append(tower_dictionary[source_tower].pop())
    solution_steps += f"{str(tower_dictionary["tower1"])} {str(tower_dictionary["tower2"])} {str(tower_dictionary["tower3"])}\n"
    solution_steps += hanoi_recursive_algorithm(disk_count - 1, tower_dictionary, auxiliary_tower, destination_tower, source_tower)
    return solution_steps


def hanoi_solver(disk_count: int) -> str:

    tower_dictionary: dict[str, list[int]] = {
        "tower1": [disk for disk in range(disk_count, 0, -1)],
        "tower2": [],
        "tower3": []
    }

    solution_steps = f"{str(tower_dictionary['tower1'])} {str(tower_dictionary['tower2'])} {str(tower_dictionary['tower3'])}\n{hanoi_recursive_algorithm(disk_count, tower_dictionary, 'tower1', 'tower3', 'tower2').rstrip('\n')}"
    return solution_steps


def main() -> None:
    print(f"hanoi_solver(2):\n{hanoi_solver(2)}\n")
    print(f"hanoi_solver(3):\n{hanoi_solver(3)}\n")
    print(f"hanoi_solver(4):\n{hanoi_solver(4)}\n")
    print(f"hanoi_solver(5):\n{hanoi_solver(5)}\n")


if __name__ == "__main__":
    main()
