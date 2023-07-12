hour, minutes, wait_time = map(int, [input() for _ in range(3)])
m = minutes + wait_time
hour += 1 if m > 60 else 0
m %= 60
print(f"{str(hour).rjust(2, '0')}:{str(m).rjust(2, '0')}")
