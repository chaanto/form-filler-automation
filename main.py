import asyncio
from higisha_touroku_form import higisha_touroku_form
from constants import BrowserType


def main():
    """
        Main function to run the form automation.
    """
    browser_type = BrowserType.CHROMIUM
    login_url = "http://vm-ryuchiwin2019/ryuchisys/login_dummy/"
    # URL can be replace to local or domain URL
    asyncio.run(higisha_touroku_form(login_url, browser_type))


if __name__ == "__main__":
    main()