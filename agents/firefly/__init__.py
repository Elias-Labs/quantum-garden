"""
Firefly - The Communication Agent
Handles all email, SMS, and messaging tasks
"""

from .email_agent import FireflyEmailAgent
from .core import FireflyCore

__all__ = ['FireflyEmailAgent', 'FireflyCore']