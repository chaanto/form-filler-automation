"""
    Provides a core class for managing Playwright browser interactions.
"""

from playwright.async_api import async_playwright
from playwright.async_api import Page, Browser, BrowserContext, Playwright
from exceptions import PageNotInitializedError, BrowserClosedError
from constants import BrowswerType


class PlaywrightCore:
    """
    A core class for managing Playwright browser interactions.
    """

    def __init__(self, headless: bool = True):
        self.playwright: Playwright = None
        self.browser: Browser = None
        self.context: BrowserContext = None
        self.page: Page = None
        self.headless = headless

    async def start(self, browser_type: BrowswerType) -> Page:
        """
            Start the Playwright browser with the specified browser type.
        """

        self.playwright: Playwright = await async_playwright().start()

        if not BrowswerType.is_valid_browser(browser_type):
            raise ValueError(f"Invalid browser type: {browser_type}. Valid options are: {BrowswerType.get_all_browsers()}")

        self.browser: Browser = await self.playwright[browser_type].launch(headless=self.headless)
        self.context: BrowserContext = await self.browser.new_context()
        self.page: Page = await self.context.new_page()

        return self.page

    async def navigate_to(self, url: str):
        """
        Navigate to a specified URL using the Playwright page.

        Args:
            url (str): url to navigate to.

        Raises:
            BrowserClosedError: when the browser is closed.
            PageNotInitializedError: when the page is not initialized.
        Returns:
            _type_: The Playwright page object after navigation.
        """
        if not self.browser.is_connected:
            raise BrowserClosedError()

        if not self.page:
            raise PageNotInitializedError()

        await self.page.goto(url)

        return self.page

    async def close(self):
        """
            Close the Playwright browser and context.
        """
        if self.page:
            await self.page.close()
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()

        await self.playwright.stop()
