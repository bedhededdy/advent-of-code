def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = list(filter(lambda x: x != "", [line.strip() for line in lines]))
    return lines

def game_is_possible(game, red_ct, blue_ct, green_ct):
    draws = game.split("; ")
    for draw in draws:
        draw_by_color = draw.split(", ")
        blue_drawn = 0
        red_drawn = 0
        green_drawn = 0
        for color_draw in draw_by_color:
            ct, color = color_draw.split(" ")
            if color == "blue":
                blue_drawn += int(ct)
            elif color == "red":
                red_drawn += int(ct)
            elif color == "green":
                green_drawn += int(ct)
        if blue_drawn > blue_ct or red_drawn > red_ct or green_drawn > green_ct:
            return False
    return True

def game_power(game):
    draws = game.split("; ")
    min_red = 0
    min_blue = 0
    min_green = 0

    for draw in draws:
        draw_by_color = draw.split(", ")
        blue_drawn = 0
        red_drawn = 0
        green_drawn = 0
        for color_draw in draw_by_color:
            ct, color = color_draw.split(" ")
            if color == "blue":
                blue_drawn += int(ct)
            elif color == "red":
                red_drawn += int(ct)
            elif color == "green":
                green_drawn += int(ct)
        min_red = max(red_drawn, min_red)
        min_blue = max(blue_drawn, min_blue)
        min_green = max(green_drawn, min_green)

    return min_red * min_blue * min_green

def part1():
    games = get_input("p2-1.txt")
    id = 1
    sum = 0
    for game in games:
        if (game_is_possible(game.split(": ")[1], 12, 14, 13)):
            sum += id
        id += 1
    print(sum)

def part2():
    games = get_input("p2-1.txt")
    power_sum = 0
    for game in games:
        power_sum += game_power(game.split(": ")[1])
    print(power_sum)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
