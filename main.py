def total_expenses(file_name):
    s = 0
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            _, *name, price, _ = line.split()
            s += float(price.replace("$", "").strip())
    return s


def main():
    ...


if __name__ == "__main__":
    main()
