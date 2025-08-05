"""
    Custom exceptions for errors.
"""


class PlaywrightAutomationError(Exception):
    """Base class for Playwright automation-related errors."""
    pass


class PageNotInitializedError(PlaywrightAutomationError):
    """Raised when 'page' is not initialized or is None."""
    def __init__(self, message="Playwright page is not initialized?"):
        super().__init__(message)


class BrowserClosedError(PlaywrightAutomationError):
    """Raised when attempting to use the page after browser is closed."""
    def __init__(self, message="Browser has been closed."):
        super().__init__(message)


class PageNavigationError(PlaywrightAutomationError):
    """Raised when there is an error navigating to a page."""
    def __init__(self, message="Error navigating to the specified URL."):
        super().__init__(message)
