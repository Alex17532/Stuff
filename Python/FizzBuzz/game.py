count = 0

for i in range(1,101):
    found = False
    if i % 3 == 0:
        print("Fizz", end='')
        found = True
        count += 1

    if i % 5 == 0:
        print("Buzz")
        count += 1
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end='')
        count += 1
        continue
    
    if not found:
        print(i)
        count += 1
    
    else:
        print("")
        count += 1

print(count)