"""
    Provides a core class for managing form interactions.
"""

from playwright.sync_api import Page


class CoreForm:
    """
        Core form class for managing form interactions.
    """
    def __init__(self, page: Page):
        self.page = page

    async def fill_input(self, selector: str, value: str):
        """
        Fill an input field with the specified value.

        Args:
            selector (str): The CSS selector for the input field.
            value (str): The value to fill in the input field.
        """
        await self.page.fill(selector, value)

    async def select_option(self, selector: str, value: str):
        """
        Select an option from a dropdown.

        Args:
            selector (str): The CSS selector for the dropdown.
            value (str): The value of the option to select.
        """
        await self.page.select_option(selector, value)

    async def check_checkbox(self, selector: str):
        """
        Check a checkbox.

        Args:
            selector (str): The CSS selector for the checkbox.
        """
        if not self.page.is_checked(selector):
            await self.page.check(selector)

    async def uncheck_checkbox(self, selector: str):
        """
        Uncheck a checkbox.

        Args:
            selector (str): The CSS selector for the checkbox.
        """
        if self.page.is_checked(selector):
            await self.page.uncheck(selector)

    async def click_button(self, selector: str):
        """
        Click a button on the page.

        Args:
            selector (str): The CSS selector for the button.
        """
        await self.page.click(selector)

    async def submit_form(self, selector: str):
        """
        Submit a form.

        Args:
            selector (str): The CSS selector for the form.
        """
        await self.page.click(f"{selector} button[type='submit']")

    async def is_input_filled(self, selector: str) -> bool:
        """
        Check if an input field is filled.

        Args:
            selector (str): The CSS selector for the input field.

        Returns:
            bool: True if the input field is filled, False otherwise.
        """
        return bool(self.page.input_value(selector).strip())

    async def is_option_selected(self, selector: str, value: str) -> bool:
        """
        Check if a specific option is selected in a dropdown.

        Args:
            selector (str): The CSS selector for the dropdown.
            value (str): The value of the option to check.

        Returns:
            bool: True if the option is selected, False otherwise.
        """
        selected_option = self.page.selected_option(selector)
        return selected_option == value

    async def is_checkbox_checked(self, selector: str) -> bool:
        """
        Check if a checkbox is checked.

        Args:
            selector (str): The CSS selector for the checkbox.

        Returns:
            bool: True if the checkbox is checked, False otherwise.
        """
        return self.page.is_checked(selector)

    async def is_button_enabled(self, selector: str) -> bool:
        """
        Check if a button is enabled.

        Args:
            selector (str): The CSS selector for the button.

        Returns:
            bool: True if the button is enabled, False otherwise.
        """
        return not self.page.is_disabled(selector)

    async def is_button_visible(self, selector: str) -> bool:
        """
        Check if a button is visible.

        Args:
            selector (str): The CSS selector for the button.

        Returns:
            bool: True if the button is visible, False otherwise.
        """
        return self.page.is_visible(selector)

    async def is_button_present(self, selector: str) -> bool:
        """
        Check if a button is present in the DOM.

        Args:
            selector (str): The CSS selector for the button.

        Returns:
            bool: True if the button is present, False otherwise.
        """
        return self.page.query_selector(selector) is not None

    async def wait_for_form_submission(self, selector: str, timeout: int = 30000):
        """
        Wait for a form submission to complete.

        Args:
            selector (str): The CSS selector for the form.
            timeout (int): Maximum time to wait for the submission in milliseconds.

        Returns:
            bool: True if the form was submitted successfully, False if it timed out.
        """
        return self.page.wait_for_event("submit", selector=selector, timeout=timeout)

    async def is_form_valid(self, selector: str) -> bool:
        """
        Check if a form is valid.

        Args:
            selector (str): The CSS selector for the form.

        Returns:
            bool: True if the form is valid, False otherwise.
        """
        return self.page.evaluate(f"() => document.querySelector('{selector}').checkValidity()")

    async def get_input_value(self, selector: str) -> str:
        """
        Get the value of an input field.

        Args:
            selector (str): The CSS selector for the input field.

        Returns:
            str: The value of the input field.
        """
        return self.page.input_value(selector)

    async def get_selected_option(self, selector: str) -> str:
        """
        Get the selected option from a dropdown.

        Args:
            selector (str): The CSS selector for the dropdown.

        Returns:
            str: The value of the selected option.
        """
        return self.page.selected_option(selector)

    async def reset_form(self, selector: str):
        """
        Reset a form to its initial state.

        Args:
            selector (str): The CSS selector for the form.
        """
        self.page.click(f"{selector} button[type='reset']")
