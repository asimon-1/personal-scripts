import numpy as np

## Part 1
input_number = 368078

ring_i = np.ceil((np.sqrt(input_number) + 1) / 2) - 1
max_ring = (2 * ring_i + 1) ** 2
period = ring_i
num_in_ring = 8 * period
min_steps = period
max_steps = 2 * period

ring_list = np.arange(max_ring, max_ring - num_in_ring, -1)
step_list = np.concatenate(
    (np.arange(max_steps, min_steps, -1), np.arange(min_steps, max_steps, 1))
)
step_list = np.concatenate((step_list, step_list, step_list, step_list))
print(step_list[np.where(ring_list == input_number)])

## Part 2
input_number = 368078
size = 101
container = np.zeros((size, size))
center_row, center_column = int(np.ceil(size / 2.0)), int(np.ceil(size / 2.0))
direction = "right"

container[center_row][center_column] = 1
current_row, current_column = int(np.ceil(size / 2.0)), int(np.ceil(size / 2.0))

for i in range(100):
    print(container[current_row][current_column])
    if container[current_row][current_column] > input_number:
        print(container[current_row][current_column])
        break

    if direction == "right":
        current_column += 1
        container[current_row][current_column] += container[current_row - 1][
            current_column - 0
        ]
        container[current_row][current_column] += container[current_row - 1][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row - 0][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column + 0
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column + 1
        ]
        container[current_row][current_column] += container[current_row + 0][
            current_column + 1
        ]
        container[current_row][current_column] += container[current_row - 1][
            current_column + 1
        ]
        if container[current_row + 1][current_column] == 0:
            direction = "up"
        else:
            direction = "right"
        continue

    if direction == "up":
        current_row += 1
        container[current_row][current_column] += container[current_row - 1][
            current_column - 0
        ]
        container[current_row][current_column] += container[current_row - 1][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row - 0][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column + 0
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column + 1
        ]
        container[current_row][current_column] += container[current_row + 0][
            current_column + 1
        ]
        container[current_row][current_column] += container[current_row - 1][
            current_column + 1
        ]
        if container[current_row][current_column - 1] == 0:
            direction = "left"
        else:
            direction = "up"
        continue

    if direction == "left":
        current_column -= 1
        container[current_row][current_column] += container[current_row - 1][
            current_column - 0
        ]
        container[current_row][current_column] += container[current_row - 1][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row - 0][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column + 0
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column + 1
        ]
        container[current_row][current_column] += container[current_row + 0][
            current_column + 1
        ]
        container[current_row][current_column] += container[current_row - 1][
            current_column + 1
        ]
        if container[current_row - 1][current_column] == 0:
            direction = "down"
        else:
            direction = "left"
        continue

    if direction == "down":
        current_row -= 1
        container[current_row][current_column] += container[current_row - 1][
            current_column - 0
        ]
        container[current_row][current_column] += container[current_row - 1][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row - 0][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column - 1
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column + 0
        ]
        container[current_row][current_column] += container[current_row + 1][
            current_column + 1
        ]
        container[current_row][current_column] += container[current_row + 0][
            current_column + 1
        ]
        container[current_row][current_column] += container[current_row - 1][
            current_column + 1
        ]
        if container[current_row][current_column + 1] == 0:
            direction = "right"
        else:
            direction = "down"
        continue
