from decimal import Decimal


def decimal_list(start, end, step):
    decimal_list = []
    decimal_list.append(Decimal(start))
    while True:
        value = decimal_list[-1] + Decimal(step)
        decimal_list.append(Decimal(value))
        if decimal_list[-1] == end:
            break
    return decimal_list


def run_exercise_three():
    print(decimal_list(2, 5.5, 0.5))


if __name__ == "__main__":
    run_exercise_three()
