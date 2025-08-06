"""
    This module defines an constants.
"""


class BrowserType:
    """
        Enum for Playwright browser types.
    """
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'
    WEBKIT = 'webkit'

    @classmethod
    def get_all_browsers(cls):
        """
        Returns a list of all available browser types.
        """
        return [cls.CHROMIUM, cls.FIREFOX, cls.WEBKIT]

    @classmethod
    def is_valid_browser(cls, browser_type):
        """
        Checks if the provided browser type is valid.

        Args:
            browser_type (str): The browser type to check.

        Returns:
            bool: True if valid, False otherwise.
        """
        return browser_type in cls.get_all_browsers()


class LoginMenu:
    """
    Constants for Ryuuchi Application.
    """
    # Login
    DIVISION_ONE: str = "一課"
    DIVISION_ONE_SV: str = "一課SV"
    DIVISION_TWO: str = "二課"
    DIVISION_TWO_1: str = "二課1"
    DIVISION_TWO_2: str = "二課2"
    KOUJI_MACHI: str = "麹町署"
    MARUNOUCHI: str = "丸の内署"
    CHUUOU: str = "中央署"
    TAMA_M: str = "多摩分室 男"
    TAMA_F: str = "多摩分室 女"
    WANGAN_M: str = "湾岸分室 男"
    WANGAN_F: str = "湾岸分室 女"
    NISHIGAOKA: str = "西が丘"
    HARAJUKU_M: str = "原宿男"
    HARAJUKU_F: str = "原宿女"
    MUSASHI_M: str = "武蔵男"
    MUSASHI_F: str = "武蔵女"
    MITA: str = "三田分室"

    @classmethod
    def get_all_login(cls):
        """
        Returns a list of all Ryuuchi menu constants.
        """
        return [
            cls.DIVISION_ONE,
            cls.DIVISION_ONE_SV,
            cls.DIVISION_TWO,
            cls.DIVISION_TWO_1,
            cls.DIVISION_TWO_2,
            cls.KOUJI_MACHI,
            cls.MARUNOUCHI,
            cls.CHUUOU,
            cls.TAMA_M,
            cls.TAMA_F,
            cls.WANGAN_M,
            cls.WANGAN_F,
            cls.NISHIGAOKA,
            cls.HARAJUKU_M,
            cls.HARAJUKU_F,
            cls.MUSASHI_M,
            cls.MUSASHI_F,
            cls.MITA
        ]

    @classmethod
    def is_valid_login(cls, menu_name):
        """
        Checks if the provided menu name is valid.

        Args:
            menu_name (str): The menu name to check.

        Returns:
            bool: True if valid, False otherwise.
        """
        return menu_name in cls.get_all_login()


class MainMenu:
    """
    Constants for Main Menu.
    """
    DATA_ENTRY: str = "入力業務"
    CONTRACT: str = "委託業務"
    SPECIAL_DETENTION: str = "特留業務"
    INQUIRY: str = "照会業務"
    DETENTION_FEE: str = "拘禁費用業務"
    REPORT_PRINT: str = "様式印字"

    @classmethod
    def get_all_main_menu(cls):
        """
        Returns a list of all main menu constants.
        """
        return [
            cls.DATA_ENTRY,
            cls.CONTRACT,
            cls.SPECIAL_DETENTION,
            cls.INQUIRY,
            cls.DETENTION_FEE,
            cls.REPORT_PRINT
        ]