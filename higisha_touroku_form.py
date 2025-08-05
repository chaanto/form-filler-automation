"""
    新入被疑者の登録
"""

from playwright.sync_api import Page
from core_playwright import PlaywrightCore
from core_form import CoreForm
from exceptions import PageNavigationError
from constants import (
    BrowswerType,
    LoginMenu,
    base_service_url
)


async def ensure_navigation_page(page: Page):
    """
    Ensure that the navigated page is initialized.

    Args:
        page (Page): The Playwright page object.

    Raises:
        PageNavigationError: If the page is not initialized.
    """
    if not page:
        raise PageNavigationError("The page is not initialized after navigation.")


async def higisha_touroku_form(browser_type: BrowswerType):
    """
    Function to handle the higisha registration form using Playwright.

    Args:
        page (Page): The Playwright page object.
        browser_type (BrowswerType): The type of browser to use.

    Returns:
        None
    """

    try:
        # Initialize Playwright service
        service: PlaywrightCore = PlaywrightCore(headless=False)
        await service.start(browser_type)

        # Navigate to base service URL
        login_page: Page = await service.navigate_to(base_service_url)
        form: CoreForm = CoreForm(login_page)

        # Login using KOUJI MACHI
        kouji_machi = f"button.login-btn:has-text({LoginMenu.KOUJI_MACHI})"

        if not form.is_button_present(kouji_machi):
            raise ValueError(f"Login button for {LoginMenu.KOUJI_MACHI} not found.")

        main_page: Page = await form.click_button(kouji_machi)

        if not main_page:
            raise PageNavigationError("Failed to navigate to the main menu after login.")

        # Navigate to registration page

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the browser is closed after operations
        await service.close()
        print("Browser closed successfully.")

