"""Contains classes for the pages to test."""
from playwright.sync_api import Error, expect


class EcoImpact:
    """Class for the Eco-Impact page. Contains variables and functions for its testing."""

    def __init__(self, page):
        self.page = page
        self.url = "https://www.avito.ru/avito-care/eco-impact"
        # Eco-counter selector. Counters differ from other cards by having values
        self.counter_selector = (
            "//div[contains(@class, \"desktop-impact-item\") "
            "and count(.//div[contains(@class, \"desktop-value\")]) = 1]"
        )

    def screenshot_eco_counter(self, counter_index: int, filename: str):
        """
        Takes a screenshot of an eco counter.
        : param counter_index: number of an eco-counter card
        : param filename: path for the screenshot file
        """
        try:
            counter = self.page.locator("xpath=" + self.counter_selector + f"[{counter_index}]")

            # Take the screenshot
            counter.screenshot(path=filename)

        except Error as e:
            print(f"The counter No. {counter_index} was not found.\n", e)

    def check_text_eco_counter(self, counter_index: int, unit: str, label: str):
        """
        Checks texts of unit and label of an eco counter.
        : param counter_index: number of an eco-counter card
        : param unit: expected text of the measurement unit
        : param label: expected text of the label
        """
        try:
            # Selector for measurement units
            measurement = self.page.locator(
                "xpath=" + self.counter_selector 
                + f"[{counter_index}]//div[contains(@class, \"desktop-unit\")]"
                )
            expect(measurement).to_contain_text(unit)

            # Selector for description text
            description = self.page.locator(
                "xpath=" + self.counter_selector 
                + f"[{counter_index}]//div[contains(@class, \"desktop-label\")]"
                )
            expect(description).to_contain_text(label)

        except Error as e:
            print(f"The counter No. {counter_index} was not found.\n", e)

    def check_eco_impact_not_auth(self, counter_index: int, opacity: str):
        """
        Checks how a non-authorized user sees the eco impact block:
        1) There`s sign in button;
        2) No profile picture is to be seen;
        3) Eco counters are disabled: their values equal zero 
            and their texts are partially transparent.
        : param counter_index: number of an eco-counter card
        : param opacity: opacity value
        """
        # Checking that sign in button is present
        signin_btn = self.page.get_by_text("Авторизоваться")
        expect(signin_btn).to_be_visible()

        # Checking that there is no avatar of the user
        avatar = self.page.locator("xpath=//img[contains(@class, \"desktop-avatar\")]")
        expect(avatar).not_to_be_attached()

        try:
            # Selector for disabled counter
            disability = self.page.locator(
                "xpath=" + self.counter_selector 
                + f"[{counter_index}]//div[contains(@class, \"desktop-disabled\")]"
                )
            expect(disability).to_have_css("opacity", opacity)

            # Selector for value of a counter
            value = self.page.locator(
                "xpath=" + self.counter_selector 
                + f"[{counter_index}]//div[contains(@class, \"desktop-value\")]"
                )
            expect(value).to_contain_text("0")

        except Error as e:
            print(f"The counter No. {counter_index} was not found.\n", e)


    # Я также пыталась пройти процедуру логина, чтобы сделать скриншоты уже заполненных карточек
    # Но при автоматизированном логине, видимо, требуется капча, так что решила это оставить - 
    # Вдруг мне потом аккаунт заблокируют за подозрительную активность, а он мне дорог :)
    def login(self, login: str, password: str):
        """
        Proceeds to log in.
        : param login: user login
        : param password: user password
        """
        # Actions open a new login tab
        with self.page.expect_popup() as popup_info:
            self.page.get_by_text("Авторизоваться").click()

        popup = popup_info.value
        popup.locator("xpath=//input[@name=\"login\"]").fill(login)
        popup.locator("xpath=//input[@name=\"password\"]").fill(password)

        popup.get_by_text("Войти").click()
