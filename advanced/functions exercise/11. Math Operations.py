from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    while numbers:
        for key, value in kwargs.items():
            if numbers:
                current_number = numbers.popleft()
                if key == "a":
                    kwargs[key] += current_number
                elif key == "s":
                    kwargs[key] -= current_number
                elif key == "d":
                    if current_number == 0:
                        continue
                    else:
                        kwargs[key] /= current_number
                elif key == "m":
                    kwargs[key] *= current_number
            else:
                break
    test = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result = ""
    for key, value in test:
        result += f"{key}: {value:.1f}" + "\n"
    return result.strip()


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))



