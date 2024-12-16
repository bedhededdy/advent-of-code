from math import ceil, floor, sqrt

def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def get_nums(line):
    lst = line.split(" ")
    return [int(x) for x in lst if x != "" and ":" not in x]

def concat_nums(lst):
    return int("".join([str(x) for x in lst]))

def part1():
    races = get_input("p6-1.txt")
    times = get_nums(races[0])
    distances = get_nums(races[1])
    # More time charging = faster speed
    # Need to find the inflection points where the time charging
    # gets us the distance and then figure out what to do from there
    # First sampel race = 7 ms and distance is 9mm
    # We know that the speed * time = distance
    # The speed we travel is secs_charging * 0 + (total_time - secs_charging) * speed
    # We also know that secs_charging = speed
    # So we can say that (total_time - secs_charging) * secs_charging > distance
    # -secs_charging^2 + total_time * secs_charging - distance > 0
    # So Since this is a downward parabola, we know the points between the two zeroes
    # will give us the winning points
    # So therefore, we will just solve this equation using the quadratic formula
    # [-total_time +/- sqrt(total_time^2 - 4 * -1 * -distance)] / [2 * -1]
    # [-total_time +/- sqrt(total_time^2 - 4 * distance)] / -2
    # If we solve wtih the first example, we get the following
    # -7 +/- sqrt(49 - 36) / -2 = -7 +/- sqrt(13) / -2
    # -7 +/- 3.6 / -2
    # We get the following inflection points
    # 1.7 and 5.3
    # For the lower 0, we must round up and for the higher 0 we must round down
    # Because both ends of the parabola would be below y=0 prior to the first 0 and after the second 0
    # So we get that 2, 3, 4, and 5 are the winning points
    # Also, since we don't have negative time, we can throw out any negative numbers
    num_winning_solutions_product = 1
    for i in range(len(times)):
        integral_x0 = False
        integral_x1 = False
        total_time = times[i]
        distance = distances[i]
        discriminant = total_time * total_time - 4 * distance
        # We know that the subtraction case will end up being larger since -total_time is always negative and -/- = +
        x0 = (-total_time + sqrt(discriminant)) / -2
        x1 = (-total_time - sqrt(discriminant)) / -2
        if x0 == floor(x0):
            integral_x0 = True
        if x1 == floor(x1):
            integral_x1 = True
        x0 = max(0, ceil(x0))
        x1 = max(0, floor(x1))
        num_winning_solutions = x1 - x0 + 1
        # If we somehow got a perfect square discriminant, we cannot
        # count the solution itself as it equals zero instead of exceeding zero
        if integral_x0:
            num_winning_solutions -= 1
        if integral_x1:
            num_winning_solutions -= 1
        if (num_winning_solutions < 0):
            num_winning_solutions = 0
        num_winning_solutions_product *= num_winning_solutions
    print(num_winning_solutions_product)

def part2():
    races = get_input("p6-1.txt")
    times = get_nums(races[0])
    distances = get_nums(races[1])
    # Now we must turn the times and distances as one time by treating as a string
    time = concat_nums(times)
    distance = concat_nums(distances)
    integral_x0 = False
    integral_x1 = False
    total_time = time
    discriminant = total_time * total_time - 4 * distance
    # We know that the subtraction case will end up being larger since -total_time is always negative and -/- = +
    x0 = (-total_time + sqrt(discriminant)) / -2
    x1 = (-total_time - sqrt(discriminant)) / -2
    if x0 == floor(x0):
        integral_x0 = True
    if x1 == floor(x1):
        integral_x1 = True
    x0 = max(0, ceil(x0))
    x1 = max(0, floor(x1))
    num_winning_solutions = x1 - x0 + 1
    # If we somehow got a perfect square discriminant, we cannot
    # count the solution itself as it equals zero instead of exceeding zero
    if integral_x0:
        num_winning_solutions -= 1
    if integral_x1:
        num_winning_solutions -= 1
    if (num_winning_solutions < 0):
        num_winning_solutions = 0
    print(num_winning_solutions)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
