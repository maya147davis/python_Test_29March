def find_median(numbers: list[float]) -> float:
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    median = n // 2

    if n % 2 == 1:
        return sorted_nums[median]
    else:
        return (sorted_nums[median - 1] + sorted_nums[median]) / 2


list = input("Enter numbers separated by spaces: ")
numbers = [float(x) for x in list.split()]
print("Median:", find_median(numbers))