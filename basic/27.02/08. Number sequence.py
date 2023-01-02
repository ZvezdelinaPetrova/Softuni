import sys

n = int(input())

greater = - sys.maxsize
smaller = sys.maxsize


# kogato tarsim minimum i maximum, sazdavame dve promenilii i kazvame che sa ravni-maximuma na nai-malkoto otricatelno
# chislo zashtoto tarsim dali maximuma e po-golyam ot nai-malkoto chislo, za da stane po-golyamo, nachalnata tochka
# ni e nai-niskoto chilso
# MIN da e raven na nai-golyamoto polojitelno chislo

for i in range(1, n + 1):
    number = int(input())
    if number > greater:
        greater = number
    if number < smaller:
        smaller = number


print(f"Max number: {greater}")
print(f"Min number: {smaller}")

