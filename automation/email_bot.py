"""
Email Automation Bot - Send automated emails safely

⚠️ CRITICAL SECURITY REQUIREMENTS:
1. Use APP PASSWORDS, not your main email password
2. Never commit your .env file to Git
3. Gmail users: Enable 2FA and create App Password at:
   https://myaccount.google.com/apppasswords

This script helps you send automated emails for notifications,
reminders, or batch communications.

Author: Python AI Automation Lab
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from typing import List, Optional
from colorama import init, Fore, Style
from dotenv import load_dotenv

# Initialize colorama
init(autoreset=True)

# Load environment variables (NEVER logged, NEVER committed)
load_dotenv()


class EmailBot:
    """
    Email automation bot with security best practices.
    
    Security features:
    - Uses environment variables for credentials
    - Never logs passwords or API keys
    - Validates inputs before sending
    - Uses app-specific passwords
    """
    
    # Common SMTP servers
    SMTP_SERVERS = {
        'gmail': ('smtp.gmail.com', 587),
        'outlook': ('smtp-mail.outlook.com', 587),
        'yahoo': ('smtp.mail.yahoo.com', 587),
    }
    
    def __init__(self, email_address: Optional[str] = None, 
                 email_password: Optional[str] = None):
        """
        Initialize the Email Bot.
        
        Args:
            email_address: Sender email (or set EMAIL_ADDRESS in .env)
            email_password: App password (or set EMAIL_PASSWORD in .env)
        """
        # Get credentials from environment or parameters
        self.email_address = email_address or os.getenv("EMAIL_ADDRESS")
        self.email_password = email_password or os.getenv("EMAIL_PASSWORD")
        
        # Validate credentials (WITHOUT logging them!)
        if not self.email_address:
            raise ValueError(
                "Email address not found! Set EMAIL_ADDRESS in .env file"
            )
        
        if not self.email_password or self.email_password == "your_app_password_here":
            raise ValueError(
                "Email password not found! Set EMAIL_PASSWORD in .env file\n"
                "⚠️  Use an APP PASSWORD, not your main password!\n"
                "Gmail: https://myaccount.google.com/apppasswords"
            )
        
        # Determine SMTP server based on email domain
        self.smtp_server, self.smtp_port = self._get_smtp_config()
    
    def _get_smtp_config(self) -> tuple:
        """
        Determine SMTP configuration based on email domain.
        
        Returns:
            Tuple of (smtp_server, port)
        """
        email_lower = self.email_address.lower()
        
        if 'gmail' in email_lower:
            return self.SMTP_SERVERS['gmail']
        elif 'outlook' in email_lower or 'hotmail' in email_lower:
            return self.SMTP_SERVERS['outlook']
        elif 'yahoo' in email_lower:
            return self.SMTP_SERVERS['yahoo']
        else:
            # Default to Gmail settings for unknown providers
            print(f"{Fore.YELLOW}⚠️  Unknown email provider, using Gmail SMTP")
            return self.SMTP_SERVERS['gmail']
    
    def send_email(self, 
                   to_email: str, 
                   subject: str, 
                   body: str,
                   attachments: Optional[List[str]] = None,
                   html: bool = False) -> bool:
        """
        Send an email with optional attachments.
        
        Args:
            to_email: Recipient email address
            subject: Email subject
            body: Email body content
            attachments: List of file paths to attach (optional)
            html: If True, send body as HTML instead of plain text
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Attach body
            mime_type = 'html' if html else 'plain'
            msg.attach(MIMEText(body, mime_type))
            
            # Attach files if provided
            if attachments:
                for file_path in attachments:
                    self._attach_file(msg, file_path)
            
            # Send email via SMTP
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                
                # Login (password is NEVER logged)
                server.login(self.email_address, self.email_password)
                
                # Send email
                server.send_message(msg)
            
            print(f"{Fore.GREEN}✓ Email sent successfully to {to_email}")
            return True
            
        except smtplib.SMTPAuthenticationError:
            print(f"{Fore.RED}❌ Authentication failed!")
            print(f"{Fore.YELLOW}⚠️  Make sure you're using an APP PASSWORD, not your main password")
            print(f"{Fore.CYAN}Gmail users: https://myaccount.google.com/apppasswords")
            return False
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error sending email: {str(e)}")
            return False
    
    def _attach_file(self, msg: MIMEMultipart, file_path: str) -> None:
        """
        Attach a file to the email message.
        
        Args:
            msg: Email message object
            file_path: Path to file to attach
        """
        try:
            path = Path(file_path)
            
            if not path.exists():
                print(f"{Fore.YELLOW}⚠️  File not found: {file_path}")
                return
            
            with open(path, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {path.name}'
            )
            
            msg.attach(part)
            print(f"{Fore.CYAN}📎 Attached: {path.name}")
            
        except Exception as e:
            print(f"{Fore.YELLOW}⚠️  Could not attach {file_path}: {str(e)}")


def main():
    """Main function to run the email bot."""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}📧 Email Automation Bot")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    # Security warning
    print(f"{Fore.RED}⚠️  SECURITY REMINDER:")
    print(f"{Fore.YELLOW}   • Use APP PASSWORDS, not your main password")
    print(f"{Fore.YELLOW}   • Never share your .env file")
    print(f"{Fore.YELLOW}   • This script NEVER logs your credentials\n")
    
    try:
        # Initialize bot (credentials from .env)
        bot = EmailBot()
        
        print(f"{Fore.GREEN}✓ Email bot initialized successfully")
        print(f"{Fore.CYAN}Sending from: {Fore.GREEN}{bot.email_address}\n")
        
        # Get email details from user
        to_email = input(f"{Fore.CYAN}Recipient email: {Style.RESET_ALL}").strip()
        subject = input(f"{Fore.CYAN}Subject: {Style.RESET_ALL}").strip()
        
        print(f"\n{Fore.CYAN}Enter message body (press Enter twice when done):")
        body_lines = []
        while True:
            line = input()
            if line == "" and len(body_lines) > 0 and body_lines[-1] == "":
                body_lines.pop()  # Remove the last empty line
                break
            body_lines.append(line)
        
        body = "\n".join(body_lines)
        
        # Ask about attachments
        attach = input(f"\n{Fore.CYAN}Add attachments? (yes/no): {Style.RESET_ALL}").strip().lower()
        attachments = []
        
        if attach in ['yes', 'y']:
            print(f"{Fore.YELLOW}Enter file paths (one per line, empty line to finish):")
            while True:
                file_path = input(f"{Fore.CYAN}  File: {Style.RESET_ALL}").strip()
                if not file_path:
                    break
                attachments.append(file_path)
        
        # Confirm before sending
        print(f"\n{Fore.YELLOW}{'='*60}")
        print(f"{Fore.YELLOW}Ready to send!")
        print(f"{Fore.YELLOW}To: {to_email}")
        print(f"{Fore.YELLOW}Subject: {subject}")
        if attachments:
            print(f"{Fore.YELLOW}Attachments: {len(attachments)} file(s)")
        print(f"{Fore.YELLOW}{'='*60}\n")
        
        confirm = input(f"{Fore.CYAN}Send email? (yes/no): {Style.RESET_ALL}").strip().lower()
        
        if confirm in ['yes', 'y']:
            success = bot.send_email(
                to_email=to_email,
                subject=subject,
                body=body,
                attachments=attachments if attachments else None
            )
            
            if success:
                print(f"\n{Fore.GREEN}✨ Email sent successfully!\n")
            else:
                print(f"\n{Fore.RED}❌ Failed to send email\n")
        else:
            print(f"\n{Fore.YELLOW}Email cancelled. Nothing was sent.\n")
    
    except ValueError as e:
        print(f"\n{Fore.RED}❌ Configuration Error:")
        print(f"{Fore.YELLOW}{str(e)}\n")
        print(f"{Fore.CYAN}Setup Instructions:")
        print(f"1. Copy .env.example to .env")
        print(f"2. Add your email and APP PASSWORD to .env")
        print(f"3. Never commit .env to Git!\n")
    
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Operation cancelled.\n")
    
    except Exception as e:
        print(f"\n{Fore.RED}❌ Unexpected error: {str(e)}\n")


if __name__ == "__main__":
    main()
