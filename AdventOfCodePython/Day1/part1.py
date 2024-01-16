import timeit

start_time = timeit.default_timer()


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

with open("input.txt", "r") as f:
    lines = f.read()

lines = lines.split("\n")


final_numbers = []
for line in lines:
    line_numbers = []
    for each in line:
        try:
            if int(each) in numbers:
                line_numbers.append(each)
        except:
            continue

    final_number = line_numbers[0] + line_numbers[-1]

    final_numbers.append(int(final_number))


print(final_numbers)

print(sum(final_numbers))

print(timeit.default_timer() - start_time)
