def get_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def get_seeds(spec):
    seeds = spec[0].split(": ")[1].split(" ")
    return [int(seed) for seed in seeds]

def get_ranges(spec, search_str):
    idx = spec.index(search_str) + 1
    ranges = []
    while idx < len(spec) and spec[idx] != "":
        rnge = spec[idx].split(" ")
        ranges.append((int(rnge[0]), int(rnge[1]), int(rnge[2])))
        idx += 1
    return ranges

def get_id(range_map, src_value):
    for rnge in range_map:
        src_rnge_begin = rnge[1]
        rng_end = rnge[2]
        if src_value >= src_rnge_begin and src_value < src_rnge_begin + rng_end:
            return rnge[0] + (src_value - src_rnge_begin)
    return src_value

def part1():
    spec = get_input("p5-1.txt")
    nearest_loc = ""
    seeds = get_seeds(spec)
    seed_to_soil = get_ranges(spec, "seed-to-soil map:")
    soil_to_fertilizer = get_ranges(spec, "soil-to-fertilizer map:")
    fertilizer_to_water = get_ranges(spec, "fertilizer-to-water map:")
    water_to_light = get_ranges(spec, "water-to-light map:")
    light_to_temperature = get_ranges(spec, "light-to-temperature map:")
    temperature_to_humidity = get_ranges(spec, "temperature-to-humidity map:")
    humidity_to_location = get_ranges(spec, "humidity-to-location map:")
    for seed in seeds:
        soil = get_id(seed_to_soil, seed)
        fertilizer = get_id(soil_to_fertilizer, soil)
        water = get_id(fertilizer_to_water, fertilizer)
        light = get_id(water_to_light, water)
        temperature = get_id(light_to_temperature, light)
        humidity = get_id(temperature_to_humidity, temperature)
        location = get_id(humidity_to_location, humidity)
        if nearest_loc == "" or location < nearest_loc:
            nearest_loc = location
    print(nearest_loc)

def get_seed_ranges(seeds):
    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append((seeds[i], seeds[i + 1] + seeds[i]))
    return ranges

def part2():
    # FIXME: THIS WORKS, BUT IS TOO SLOW FOR THE LARGE INPUT
    #        NEED TO FIGURE OUT A WAY TO OPTIMIZE THIS
    #        COULD DO THAT BY MORE OR LESS COMPUTING A DIRECT RANGE MAPPING
    #        UPFRONT FROM ALL THE SEED NUMBERS TO LOCATIONS
    #        AND THEN CHECKING IT AGAINST EACH SEED NUMBER
    #        SO SOMETHING LIKE, SEED 1 TO 10 MAPS TO LOCATIONS 50 TO 60
    #        YOU PROBABLY DON'T NEED TO RANGE MAP FOR ALL OF THESE, BECAUSE
    #        WE PREVOUSLY KNOW THAT SOIL -> LOCATION IS PRETTY FAST
    #        SO WE MAY JUST DO A RANGE COALESCE FOR SEED RANGES -> SOIL RANGES
    #        AND THEN JUST DO THE "BRUTE FORCE" APPROACH FROM THERE
    #        YOU DO NEED TO CONSOLIDATE THE WHOLE MAP FOR PERFORMANCE
    spec = get_input("p5-1.txt")
    nearest_loc = ""
    seeds = get_seeds(spec)
    seed_ranges = get_seed_ranges(seeds)
    seed_to_soil = get_ranges(spec, "seed-to-soil map:")
    soil_to_fertilizer = get_ranges(spec, "soil-to-fertilizer map:")
    fertilizer_to_water = get_ranges(spec, "fertilizer-to-water map:")
    water_to_light = get_ranges(spec, "water-to-light map:")
    light_to_temperature = get_ranges(spec, "light-to-temperature map:")
    temperature_to_humidity = get_ranges(spec, "temperature-to-humidity map:")
    humidity_to_location = get_ranges(spec, "humidity-to-location map:")
    for seed_range in seed_ranges:
        print("Range: ", seed_range)
        for seed in range(seed_range[0], seed_range[1]):
            soil = get_id(seed_to_soil, seed)
            fertilizer = get_id(soil_to_fertilizer, soil)
            water = get_id(fertilizer_to_water, fertilizer)
            light = get_id(water_to_light, water)
            temperature = get_id(light_to_temperature, light)
            humidity = get_id(temperature_to_humidity, temperature)
            location = get_id(humidity_to_location, humidity)
            if nearest_loc == "" or location < nearest_loc:
                nearest_loc = location
    print(nearest_loc)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
