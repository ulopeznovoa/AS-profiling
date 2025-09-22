import time

def slow_function():
    result = []
    for i in range(1000):
        for j in range(1000):
            result.append(i * j)
    return result

def redundant_sorting(data):
    sorted_data = sorted(data)
    for _ in range(10):
        sorted_data = sorted(sorted_data)
    return sorted_data

def simulate_wait():
    for _ in range(5):
        time.sleep(0.1)

def main():
    data = slow_function()
    sorted_data = redundant_sorting(data)
    simulate_wait()
    print("Done:", len(sorted_data))

if __name__ == "__main__":
    main()
