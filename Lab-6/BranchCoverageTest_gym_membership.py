import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# ==========================================
# Branch Coverage Tests for membership_cost
# ==========================================

def test_monthly_plan_regular():
    # Covers: valid monthly plan, age between 14 and 59, no student, no trainer
    assert membership_cost("monthly", 30, False, False) == 1500


def test_quarterly_plan_regular():
    # Covers: quarterly plan price mapping
    assert membership_cost("quarterly", 30, False, False) == 4000


def test_yearly_plan_regular():
    # Covers: yearly plan price mapping
    assert membership_cost("yearly", 30, False, False) == 12000


def test_unknown_plan_error():
    # Covers: if plan not in PLAN_PRICE (True branch)
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("daily", 25, False, False)


def test_age_below_minimum_error():
    # Covers: if age < 14 (True branch)
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


def test_minimum_age_boundary():
    # Covers: age == 14 (False branch of age < 14 at exact boundary)
    assert membership_cost("monthly", 14, False, False) == 1500


def test_senior_discount_boundary():
    # Covers: age == 60 (True branch of age >= 60 at exact boundary, 25% discount)
    assert membership_cost("monthly", 60, False, False) == 1125


def test_senior_discount_above_boundary():
    # Covers: age > 60
    assert membership_cost("monthly", 70, False, False) == 1125


def test_student_discount():
    # Covers: age < 60 and is_student == True (10% discount)
    assert membership_cost("monthly", 20, True, False) == 1350


def test_senior_takes_precedence_over_student():
    # Covers: age >= 60 even if is_student is True (senior discount applies)
    assert membership_cost("monthly", 65, True, False) == 1125


def test_yearly_with_trainer():
    # Covers: with_trainer == True AND plan == "yearly" (discount 500)
    assert membership_cost("yearly", 25, False, True) == 13500


def test_monthly_with_trainer():
    # Covers: with_trainer == True AND plan != "yearly" (False branch 16->18)
    assert membership_cost("monthly", 25, False, True) == 3500


def test_quarterly_with_trainer():
    # Covers: with_trainer == True AND plan == "quarterly" (False branch 16->18)
    assert membership_cost("quarterly", 25, False, True) == 6000


# ==========================================
# Branch Coverage Tests for can_enter
# ==========================================

def test_can_enter_plan_inactive():
    # Covers: if not plan_active (True branch)
    assert can_enter(10, False, False, "M") is False


def test_can_enter_hour_below_opening():
    # Covers: hour < 5 (True branch)
    assert can_enter(4, True, False, "M") is False


def test_can_enter_hour_above_closing():
    # Covers: hour > 22 (True branch)
    assert can_enter(23, True, False, "M") is False


def test_can_enter_opening_boundary_hour():
    # Covers: hour == 5 (valid opening boundary)
    assert can_enter(5, True, False, "M") is True


def test_can_enter_closing_boundary_hour():
    # Covers: hour == 22 (valid closing boundary)
    assert can_enter(22, True, False, "M") is True


def test_can_enter_regular_hour():
    # Covers: standard daytime entry
    assert can_enter(10, True, False, "M") is True


def test_can_enter_women_slot_female():
    # Covers: is_women_only_slot == True, gender == "F" -> True
    assert can_enter(10, True, True, "F") is True


def test_can_enter_women_slot_male():
    # Covers: is_women_only_slot == True, gender != "F" -> False
    assert can_enter(10, True, True, "M") is False


# ==========================================
# Branch Coverage Tests for bmi_category
# ==========================================

def test_bmi_invalid_height_zero():
    # Covers: height_m <= 0 (height == 0, True branch)
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, 0)


def test_bmi_invalid_height_negative():
    # Covers: height_m <= 0 (height < 0, True branch)
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, -1.75)


def test_bmi_underweight():
    # Covers: bmi < 18.5 (True branch)
    assert bmi_category(45, 1.7) == "underweight"


def test_bmi_normal():
    # Covers: 18.5 <= bmi < 25 (True branch)
    assert bmi_category(65, 1.7) == "normal"


def test_bmi_overweight():
    # Covers: 25 <= bmi < 30 (True branch)
    assert bmi_category(75, 1.7) == "overweight"


def test_bmi_obese():
    # Covers: bmi >= 30 (False branch of bmi < 30)
    assert bmi_category(95, 1.7) == "obese"

