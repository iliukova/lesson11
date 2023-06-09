def total_expenses(file_name):
    s = 0
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            _, *name, price, _ = line.split()
            s += float(price.replace("$", "").strip())
    return s


def category_expenses(file_name):
    total_by_category = {}

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            *_, price, category = line.split()
            price = float(price.replace("$", "").strip())
            if category in total_by_category:
                total_by_category[category] += price
            else:
                total_by_category[category] = price
    return total_by_category


def main():
    res = total_expenses("test.txt")
    print(res)
    res = category_expenses("test.txt")
    print(res)


if __name__ == "__main__":
    main()
