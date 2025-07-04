"""
Firefly Core - Base communication agent functionality
"""

import asyncio
from typing import Dict, List, Optional, Any
from datetime import datetime
import json
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich import print as rprint

console = Console()


class FireflyCore:
    """Core Firefly agent for all communication tasks"""
    
    def __init__(self):
        self.name = "✨ Firefly"
        self.version = "0.1.0"
        self.capabilities = [
            "Email management",
            "SMS/text messaging", 
            "Unified messaging",
            "Contact management",
            "Draft/Send distinction"
        ]
        self.draft_mode = True  # Safety first!
        
    def greeting(self):
        """Display Firefly greeting"""
        rprint(Panel(
            f"[yellow]✨ Firefly Communication Agent v{self.version}[/yellow]\n\n"
            "[green]I handle all your communication needs:[/green]\n"
            "• Email (all providers)\n"
            "• SMS/text messaging\n" 
            "• WhatsApp, Telegram, etc.\n"
            "• Contact management\n\n"
            "[red]Safety First:[/red] I always draft before sending!",
            title="✨ Firefly Activated",
            border_style="yellow"
        ))
        
    async def draft_message(self, 
                          recipient: str,
                          subject: str,
                          body: str,
                          msg_type: str = "email") -> Dict[str, Any]:
        """Draft a message for review"""
        
        draft = {
            "id": f"draft_{datetime.now().timestamp()}",
            "type": msg_type,
            "recipient": recipient,
            "subject": subject,
            "body": body,
            "created_at": datetime.now().isoformat(),
            "status": "draft"
        }
        
        # Display draft for review
        self._display_draft(draft)
        
        return draft
        
    def _display_draft(self, draft: Dict[str, Any]):
        """Display a draft message"""
        console.print("\n[yellow]📝 Draft Message[/yellow]")
        
        table = Table(show_header=False, box=None)
        table.add_column("Field", style="cyan")
        table.add_column("Value")
        
        table.add_row("To:", draft['recipient'])
        if draft['type'] == 'email':
            table.add_row("Subject:", draft['subject'])
        table.add_row("Type:", draft['type'].upper())
        table.add_row("Status:", f"[yellow]{draft['status'].upper()}[/yellow]")
        
        console.print(table)
        console.print("\n[bold]Message:[/bold]")
        console.print(Panel(draft['body'], border_style="blue"))
        
    async def send_message(self, draft: Dict[str, Any]) -> bool:
        """Send a drafted message with confirmation"""
        
        # Safety check - always confirm
        console.print(f"\n[red]⚠️  Ready to send this {draft['type']} to {draft['recipient']}?[/red]")
        
        if Confirm.ask("Do you want me to send this message?", default=False):
            # In a real implementation, this would integrate with email/SMS providers
            console.print(f"\n[green]✅ Message sent to {draft['recipient']}![/green]")
            draft['status'] = 'sent'
            draft['sent_at'] = datetime.now().isoformat()
            return True
        else:
            console.print("\n[yellow]📝 Message remains in draft mode[/yellow]")
            return False
            
    def list_capabilities(self):
        """List all Firefly capabilities"""
        table = Table(title="✨ Firefly Capabilities", show_header=True)
        table.add_column("Feature", style="cyan")
        table.add_column("Status", style="green")
        
        for capability in self.capabilities:
            table.add_row(capability, "✅ Available")
            
        console.print(table)