def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    user_string = input()
    string_list = user_string.split(",")
    float_list = []
    for num in string_list:
        float_list.append(float(num))
    return float_list
def calc_average(temp_list):
    total = 0
    for temp in temp_list:
        total += temp
    average = total / len(temp_list)
    return average
def find_min_max(temp_list):
    min_temp = temp_list[0]
    max_temp = temp_list[0]
    for temp in temp_list:
        if temp < min_temp:
            min_temp = temp
        if temp > max_temp:
            max_temp = temp
    return [min_temp, max_temp]
def sort_temperature(temp_list):
    sorted_list = temp_list.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list
def calc_median_temperature(temp_list):
    sorted_list = sort_temperature(temp_list)
    n = len(sorted_list)
    if n % 2 != 0:
        median = sorted_list[n // 2]
    else:
        mid_left = sorted_list[n // 2 - 1]
        mid_right = sorted_list[n // 2]
        median = (mid_left + mid_right) / 2.0
    return median
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    avg = calc_average(num_list)
    min_max = find_min_max(num_list)
    sorted_temps = sort_temperature(num_list)
    median = calc_median_temperature(num_list)
    print("Average:", avg)
    print("Min and Max:", min_max)
    print("Sorted Temperatures:", sorted_temps)
    print("Median Temperature:", median)
if __name__ == "__main__":
    main()