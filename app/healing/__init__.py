"""
Healing package for linux-server-diagnostics.
Exposes base healing classes for easy import.
"""

from .actions import HealingActions
from .base import BaseHealer

__all__ = ["BaseHealer", "HealingActions"]
