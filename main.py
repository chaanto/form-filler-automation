import asyncio
from higisha_touroku_form import higisha_touroku_form
from constants import BrowswerType


def main():
    """
        Main function to run the form automation.
    """
    browser_type = BrowswerType.CHROMIUM
    asyncio.run(higisha_touroku_form(browser_type))


if __name__ == "__main__":
    main()