import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# Example test cases:
def test_monthly_plan():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_can_enter():
    assert can_enter(10, True, False, "M") is True


# Test cases for Code Coverage (Line Coverage >= 90%)
def test_unknown_plan():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("invalid_plan", 25, False, False)


def test_too_young():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 12, False, False)


def test_senior_discount():
    assert membership_cost("monthly", 65, False, False) == 1125


def test_student_discount():
    assert membership_cost("monthly", 20, True, False) == 1350


def test_yearly_with_trainer():
    assert membership_cost("yearly", 25, False, True) == 13500


def test_inactive_plan():
    assert can_enter(10, False, False, "M") is False


def test_early_hour():
    assert can_enter(4, True, False, "M") is False


def test_women_only_slot_female():
    assert can_enter(10, True, True, "F") is True


def test_invalid_height():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, 0)


def test_bmi_underweight():
    assert bmi_category(45, 1.7) == "underweight"


def test_bmi_normal():
    assert bmi_category(65, 1.7) == "normal"


def test_bmi_overweight():
    assert bmi_category(75, 1.7) == "overweight"


def test_bmi_obese():
    assert bmi_category(95, 1.7) == "obese"
