import math
from hypothesis import given, strategies as st
from gym_membership import parse_plan, calculate_bmi, average_workout


@given(st.text() | st.none())
def test_parse_plan_no_crash(s):
    try:
        result = parse_plan(s)
        if result is not None:
            plan, months = result
            assert isinstance(plan, str) and len(plan) > 0
            assert isinstance(months, int) and months > 0
    except Exception as e:
        assert False, f"parse_plan crashed with: {e}"


@given(st.text(), st.integers())
def test_parse_plan_edge_cases(plan, months):
    try:
        result = parse_plan(f"{plan}-{months}")
        if result is not None:
            p, m = result
            assert isinstance(p, str) and len(p) > 0
            assert isinstance(m, int) and m > 0
    except Exception as e:
        assert False, f"parse_plan crashed with: {e}"


@given(st.text() | st.none())
def test_calculate_bmi_no_crash(s):
    try:
        result = calculate_bmi(s)
        if result is not None:
            assert isinstance(result, float) and math.isfinite(result) and result >= 0
    except Exception as e:
        assert False, f"calculate_bmi crashed with: {e}"


@given(st.floats(), st.floats())
def test_calculate_bmi_edge_cases(weight, height):
    try:
        result = calculate_bmi(f"{weight},{height}")
        if result is not None:
            assert isinstance(result, float) and math.isfinite(result) and result >= 0
    except Exception as e:
        assert False, f"calculate_bmi crashed with: {e}"


@given(st.text() | st.none())
def test_average_workout_no_crash(s):
    try:
        result = average_workout(s)
        if result is not None:
            assert isinstance(result, int) and result >= 0
    except Exception as e:
        assert False, f"average_workout crashed with: {e}"


@given(st.lists(st.integers()))
def test_average_workout_edge_cases(values):
    try:
        result = average_workout(" ".join(str(v) for v in values))
        if result is not None:
            assert isinstance(result, int) and result >= 0
    except Exception as e:
        assert False, f"average_workout crashed with: {e}"
