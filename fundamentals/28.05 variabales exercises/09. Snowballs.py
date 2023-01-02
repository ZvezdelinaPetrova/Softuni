number = int(input())

quality = 0
snow = 0
time = 0
last_value = 0
value = 0

for i in range(1, number + 1):
    current_snow = int(input())
    current_time = int(input())
    current_quality = int(input())
    value = int((current_snow / current_time) ** current_quality)
    if value >= last_value:
        last_value = value
        quality = current_quality
        snow = current_snow
        time = current_time
print(f"{snow} : {time} = {last_value} ({quality})")
