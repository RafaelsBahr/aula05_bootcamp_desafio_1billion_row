import os
import random
import time


def build_weather_station_name_list():
    station_names = []
    with open('./data/weather_stations.csv', 'r', encoding='utf-8') as file:
        file_contents = file.read()
    for station in file_contents.splitlines():
        if '#' in station:
            continue
        station_names.append(station.split(';')[0])
    return list(set(station_names))


def convert_bytes(num):
    for x in ['bytes', 'KiB', 'MiB', 'GiB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def format_elapsed_time(seconds):
    if seconds < 60:
        return f"{seconds:.3f} seconds"
    elif seconds < 3600:
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes)} minutes {int(seconds)} seconds"
    else:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if minutes == 0:
            return f"{int(hours)} hours {int(seconds)} seconds"
        return f"{int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds"


def build_test_data(weather_station_names, num_rows_to_create):
    start_time = time.time()
    coldest_temp = -99.9
    hottest_temp = 99.9
    station_names_10k_max = random.choices(weather_station_names, k=10_000)
    batch_size = 10000

    with open("./data/measurements.txt", 'w', encoding='utf-8') as file:
        for _ in range(0, num_rows_to_create // batch_size):
            batch = random.choices(station_names_10k_max, k=batch_size)
            prepped_deviated_batch = '\n'.join(
                [f"{station};{random.uniform(coldest_temp, hottest_temp):.1f}" for station in batch]
            )
            file.write(prepped_deviated_batch + '\n')

    end_time = time.time()
    file_size = os.path.getsize("./data/measurements.txt")
    human_file_size = convert_bytes(file_size)
    print("Arquivo escrito com sucesso em data/measurements.txt")
    print(f"Tamanho final:  {human_file_size}")
    print(f"Tempo decorrido: {format_elapsed_time(end_time - start_time)}")


def main():
    num_rows_to_create = 1000000
    weather_station_names = build_weather_station_name_list()
    build_test_data(weather_station_names, num_rows_to_create)


if __name__ == "__main__":
    main()
