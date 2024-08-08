"""Tests for the Ico-Impact page."""
import pytest
from page_objects import EcoImpact

@pytest.fixture(scope="session", autouse=True)
def start_page(page):
    """Goes to the Eco-Impact page"""
    eco_impact = EcoImpact(page)
    # Open the Eco Impact page
    page.goto(eco_impact.url)
    yield

@pytest.mark.parametrize("counter_number", [1, 2, 3])
def test_screenshot_eco_counter(page, counter_number):
    """Test taking a screenshot of a given eco-counter"""
    eco_impact = EcoImpact(page)
    eco_impact.screenshot_eco_counter(counter_number, f"outro/test1-{counter_number}.png")

@pytest.mark.parametrize("counter_number, text_unit, text_label", [(1, "кг CO₂", "не попало в атмосферу"), (2, "л воды", "было сохранено"), (3, "кВт⋅ч энергии", "было сэкономлено")])
def test_units_label_colors_eco_counter(page, counter_number, text_unit, text_label):
    """Test checking texts of measurement unit and label of a given eco-counter"""
    eco_impact = EcoImpact(page)
    eco_impact.check_text_eco_counter(counter_number, text_unit, text_label)

@pytest.mark.parametrize("counter_number, opacity_value", [(1, "0.3"), (2, "0.3"), (3, "0.3")])
def test_eco_impact_not_auth(page, counter_number, opacity_value):
    """Test checking eco impact block without user signing in"""
    eco_impact = EcoImpact(page)
    eco_impact.check_eco_impact_not_auth(counter_number, opacity_value)