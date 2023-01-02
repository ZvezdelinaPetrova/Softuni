def stock_availability(new_list, command, *args):
    if command == "sell":
        if not args:
            new_list.pop(0)
        else:
            for el in range(len(args)):
                new = args[el]
                result = isinstance(new, int)
                if result:
                    number = new
                    while number > 0:
                        if not new_list:
                            break
                        new_list.pop(0)
                        number -= 1
                else:
                    to_sell = args[el]
                    if to_sell in new_list:
                        while to_sell in new_list:
                            new_list.remove(to_sell)
    elif command == "delivery":
        for x in args:
            new_list.append(x)
    return new_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
