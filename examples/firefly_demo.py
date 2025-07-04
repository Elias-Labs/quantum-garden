#!/usr/bin/env python3
"""
Firefly Email Agent Demo
Shows the power of AI-assisted email management
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.firefly import FireflyEmailAgent
from rich import print as rprint
from rich.panel import Panel


async def main():
    """Run the Firefly email demo"""
    
    # Welcome message
    rprint(Panel(
        "[bold cyan]Welcome to Quantum Garden![/bold cyan]\n\n"
        "This demo shows Firefly, our AI-powered email agent,\n"
        "helping you achieve Inbox Zero with intelligent assistance.\n\n"
        "[yellow]Features demonstrated:[/yellow]\n"
        "• AI suggestions for each email\n"
        "• Draft/Send safety distinction\n" 
        "• Bulk operations (archive all older)\n"
        "• Interactive email processing\n"
        "• Processing statistics\n\n"
        "[green]Let's see Firefly in action![/green]",
        title="🌟 Quantum Garden Demo",
        border_style="blue"
    ))
    
    input("\nPress Enter to start the demo...")
    
    # Initialize and run Firefly
    firefly = FireflyEmailAgent()
    await firefly.demo_inbox_zero()
    
    # Closing message
    rprint("\n[cyan]Thank you for trying Quantum Garden![/cyan]")
    rprint("Visit [blue]https://github.com/Elias-Labs/quantum-garden[/blue] to learn more\n")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        rprint("\n[yellow]Demo interrupted by user[/yellow]")
    except Exception as e:
        rprint(f"\n[red]Error: {e}[/red]")
        sys.exit(1)