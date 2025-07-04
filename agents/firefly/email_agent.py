"""
Firefly Email Agent - Specialized email management
Following Inbox Zero methodology with AI assistance
"""

import asyncio
from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
from collections import defaultdict
import json
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print as rprint
from .core import FireflyCore

console = Console()


class Email:
    """Email representation"""
    def __init__(self, id: str, sender: str, subject: str, 
                 date: datetime, body: str = "", read: bool = False):
        self.id = id
        self.sender = sender
        self.subject = subject
        self.date = date
        self.body = body
        self.read = read
        self.labels = []
        
    def age_days(self) -> int:
        """Get email age in days"""
        return (datetime.now() - self.date).days


class FireflyEmailAgent(FireflyCore):
    """Firefly's email management specialization"""
    
    def __init__(self):
        super().__init__()
        self.emails: List[Email] = []
        self.folders = {
            "inbox": [],
            "archive": [],
            "trash": [],
            "sent": []
        }
        self.processing_stats = {
            "reviewed": 0,
            "archived": 0,
            "deleted": 0,
            "responded": 0
        }
        
    async def demo_inbox_zero(self):
        """Interactive Inbox Zero demo"""
        console.clear()
        self.greeting()
        
        # Generate demo emails
        self._generate_demo_emails()
        
        rprint("\n[yellow]📧 Starting Inbox Zero Session[/yellow]")
        rprint(f"Found {len(self.emails)} emails to process\n")
        
        # Process emails oldest first
        self.emails.sort(key=lambda x: x.date)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True
        ) as progress:
            task = progress.add_task("[cyan]Processing emails...", total=len(self.emails))
            
            for idx, email in enumerate(self.emails):
                progress.update(task, advance=1)
                await self._process_email(email, idx + 1, len(self.emails))
                
                if idx < len(self.emails) - 1:
                    if not Confirm.ask("\n[cyan]Continue to next email?[/cyan]", default=True):
                        break
                        
        # Show summary
        self._show_processing_summary()
        
    def _generate_demo_emails(self):
        """Generate realistic demo emails"""
        demo_data = [
            {
                "sender": "newsletter@techcrunch.com",
                "subject": "This Week in AI: Latest breakthroughs",
                "days_ago": 14,
                "body": "Weekly roundup of AI news and developments..."
            },
            {
                "sender": "no-reply@github.com", 
                "subject": "Your repository has a new star ⭐",
                "days_ago": 2,
                "body": "quantum-garden received a star from user..."
            },
            {
                "sender": "team@openai.com",
                "subject": "Important: API usage update",
                "days_ago": 0,
                "body": "We're updating our API pricing model..."
            },
            {
                "sender": "support@aws.com",
                "subject": "Your AWS bill is ready",
                "days_ago": 5,
                "body": "Your monthly bill of $47.32 is available..."
            },
            {
                "sender": "phil.shackleton@apu.edu",
                "subject": "Re: Earwig progress update",
                "days_ago": 1,
                "body": "Hey Mychal, great progress on the MIDI integration!"
            }
        ]
        
        for data in demo_data:
            email = Email(
                id=f"email_{len(self.emails)}",
                sender=data["sender"],
                subject=data["subject"],
                date=datetime.now() - timedelta(days=data["days_ago"]),
                body=data["body"]
            )
            self.emails.append(email)
            self.folders["inbox"].append(email)
            
    async def _process_email(self, email: Email, current: int, total: int):
        """Process a single email with AI assistance"""
        console.clear()
        
        # Display email
        rprint(f"\n[cyan]Email {current}/{total}[/cyan]")
        table = Table(show_header=False, box=None)
        table.add_column("Field", style="cyan", width=10)
        table.add_column("Value")
        
        table.add_row("From:", email.sender)
        table.add_row("Subject:", email.subject)
        table.add_row("Date:", f"{email.date.strftime('%Y-%m-%d')} ({email.age_days()} days old)")
        
        console.print(table)
        console.print(f"\n[dim]{email.body[:100]}...[/dim]\n")
        
        # AI suggestion (simulated)
        suggestion = self._get_ai_suggestion(email)
        rprint(f"[yellow]🤖 AI Suggestion:[/yellow] {suggestion}\n")
        
        # Action menu
        actions = {
            "1": ("Archive", self._archive_email),
            "2": ("Delete", self._delete_email),
            "3": ("Reply", self._reply_to_email),
            "4": ("Skip", None),
            "5": ("Archive all older", self._archive_all_older)
        }
        
        for key, (label, _) in actions.items():
            rprint(f"[cyan]{key}[/cyan]. {label}")
            
        choice = Prompt.ask("\nAction", choices=list(actions.keys()), default="1")
        
        action_name, action_func = actions[choice]
        if action_func:
            await action_func(email)
            
        self.processing_stats["reviewed"] += 1
        
    def _get_ai_suggestion(self, email: Email) -> str:
        """Get AI suggestion for email (simulated)"""
        # In real implementation, this would use AI
        if "newsletter" in email.sender.lower():
            return "Archive - This is a newsletter, older than 7 days"
        elif email.age_days() > 30:
            return "Archive - Email is over 30 days old"
        elif "bill" in email.subject.lower():
            return "Keep - This is a bill/invoice"
        elif "important" in email.subject.lower():
            return "Review - Marked as important"
        else:
            return "Archive - Appears to be informational"
            
    async def _archive_email(self, email: Email):
        """Archive an email"""
        self.folders["inbox"].remove(email)
        self.folders["archive"].append(email)
        self.processing_stats["archived"] += 1
        rprint("[green]✅ Archived[/green]")
        await asyncio.sleep(0.5)
        
    async def _delete_email(self, email: Email):
        """Delete an email"""
        if Confirm.ask("[red]Are you sure you want to delete this email?[/red]", default=False):
            self.folders["inbox"].remove(email)
            self.folders["trash"].append(email)
            self.processing_stats["deleted"] += 1
            rprint("[red]🗑️  Deleted[/red]")
        await asyncio.sleep(0.5)
        
    async def _reply_to_email(self, email: Email):
        """Reply to an email"""
        rprint("\n[yellow]📝 Drafting reply...[/yellow]")
        
        # Simple reply draft
        reply_body = Prompt.ask("Reply message")
        
        draft = await self.draft_message(
            recipient=email.sender,
            subject=f"Re: {email.subject}",
            body=reply_body,
            msg_type="email"
        )
        
        if await self.send_message(draft):
            self.processing_stats["responded"] += 1
            await self._archive_email(email)
            
    async def _archive_all_older(self, email: Email):
        """Archive all emails older than this one"""
        older_emails = [e for e in self.folders["inbox"] 
                       if e.date < email.date and e != email]
        
        if older_emails:
            rprint(f"\n[yellow]Found {len(older_emails)} older emails[/yellow]")
            if Confirm.ask("Archive all older emails?", default=True):
                for old_email in older_emails:
                    await self._archive_email(old_email)
                rprint(f"[green]✅ Archived {len(older_emails)} emails[/green]")
        else:
            rprint("[dim]No older emails found[/dim]")
            
    def _show_processing_summary(self):
        """Show processing summary"""
        console.clear()
        rprint("\n[green]✨ Inbox Zero Session Complete![/green]\n")
        
        table = Table(title="Session Summary", show_header=True)
        table.add_column("Metric", style="cyan")
        table.add_column("Count", justify="right")
        
        table.add_row("Emails Reviewed", str(self.processing_stats["reviewed"]))
        table.add_row("Archived", str(self.processing_stats["archived"]))
        table.add_row("Deleted", str(self.processing_stats["deleted"]))
        table.add_row("Replied", str(self.processing_stats["responded"]))
        table.add_row("Remaining in Inbox", str(len(self.folders["inbox"])))
        
        console.print(table)
        
        if len(self.folders["inbox"]) == 0:
            rprint("\n[green]🎉 Inbox Zero achieved![/green]")
        else:
            rprint(f"\n[yellow]📧 {len(self.folders['inbox'])} emails remaining[/yellow]")