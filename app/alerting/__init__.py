"""
Alerting package for linux-server-diagnostics.
Exposes key classes for easy import.
"""

from .base import BaseAlertSender
from .email import EmailAlertSender
from .slack import SlackAlertSender
from .telegram import TelegramAlertSender

__all__ = [
    "BaseAlertSender",
    "TelegramAlertSender",
    "SlackAlertSender",
    "EmailAlertSender",
]
