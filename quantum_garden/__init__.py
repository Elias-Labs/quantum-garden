"""
Quantum Garden - AI Agent Orchestration Platform

Build your own AI workforce. No GUI required.
"""

__version__ = "0.1.0"
__author__ = "Mychal Simka"
__email__ = "mychal@eliaslabs.com"

from .core.orchestrator import Orchestrator
from .core.agent import Agent

__all__ = ["Orchestrator", "Agent"]