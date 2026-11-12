import math


def parse_plan(code):
    if not isinstance(code, str):
        return None
    parts = code.split('-')
    if len(parts) != 2:
        return None
    plan = parts[0].strip()
    months_str = parts[1].strip()
    if not plan or not months_str:
        return None
    try:
        months = int(months_str)
    except ValueError:
        return None
    if months <= 0:
        return None
    return plan.upper(), months


def calculate_bmi(data):
    if not isinstance(data, str):
        return None
    parts = data.split(',')
    if len(parts) != 2:
        return None
    weight_str = parts[0].strip()
    height_str = parts[1].strip()
    if not weight_str or not height_str:
        return None
    try:
        weight = float(weight_str)
        height = float(height_str)
    except ValueError:
        return None
    if not (math.isfinite(weight) and math.isfinite(height)):
        return None
    if weight <= 0 or height <= 0:
        return None
    try:
        height_sq = height ** 2
        if height_sq == 0 or not math.isfinite(height_sq):
            return None
        bmi = weight / height_sq
        if not math.isfinite(bmi):
            return None
        return round(bmi, 1)
    except (OverflowError, ZeroDivisionError, ValueError):
        return None


def average_workout(minutes):
    if not isinstance(minutes, str):
        return None
    tokens = minutes.split()
    if not tokens:
        return None
    values = []
    for token in tokens:
        try:
            val = int(token)
        except ValueError:
            return None
        if val < 0:
            return None
        values.append(val)
    return sum(values) // len(values)


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    if result is None:
        print("Invalid plan code. Please use PLAN-MONTHS (e.g. GOLD-12) with positive months.")
    else:
        print("Plan and Months:", result)

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    if result is None:
        print("Invalid input. Please enter positive weight,height (e.g. 70,1.75).")
    else:
        print("BMI:", result)

    print("\n==== Running average_workout ====")
    user_input = input("Enter workout minutes separated by spaces (e.g. 45 60 30): ")
    result = average_workout(user_input)
    if result is None:
        print("Invalid input. Please enter non-negative integers separated by spaces (e.g. 45 60 30).")
    else:
        print("Average Minutes:", result)


if __name__ == "__main__":
    main()
