import heapq


def connect_cables(cables):
    heap = cables[:]
    heapq.heapify(heap)
    visualize_connections = ""
    expenses = 0

    while len(heap) > 1:
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)

        merged_cable = (cable1[0] + cable2[0], f"{cable1[1]}{cable2[1]}")
        visualize_connections += f"({cable1[1]} > {cable2[1]}) { '-> ' if len(heap) >= 1 else ''}"

        heapq.heappush(heap, merged_cable)
        expenses += merged_cable[0]

    return expenses, visualize_connections


if __name__ == "__main__":
    cables = [(3, "Black"), (5, "Blue"), (2, "Red"), (8, "Grey"),
              (1, "Yellow"), (4, "Green"), (6, "White")]
    total_expenses, result_visualize = connect_cables(cables)

    print(f"З'єднання кабелів: {result_visualize}")
    print(f"Загальна вартість з'єднання: {total_expenses}")
