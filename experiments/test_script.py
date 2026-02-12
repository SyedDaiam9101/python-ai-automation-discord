"""
Test Script - Experimentation Playground

This is your space to test ideas, prototype features, and learn Python!

Feel free to modify this file and experiment with:
- New automation ideas
- API integrations
- Data processing
- Whatever you want to build!

Author: Python AI Automation Lab
"""

from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)


def hello_automation():
    """A simple example function to get you started."""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}🧪 Welcome to the Experiments Lab!")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    print(f"{Fore.GREEN}✨ This is your playground for testing Python automation!\n")
    
    print(f"{Fore.YELLOW}Quick tips:")
    print(f"  • Modify this file to test new ideas")
    print(f"  • Import modules from the automation/ folder")
    print(f"  • Try integrating with APIs")
    print(f"  • Experiment with file processing\n")
    
    print(f"{Fore.MAGENTA}Example - Import an automation module:")
    print(f"{Fore.CYAN}  from automation.file_organizer import FileOrganizer")
    print(f"{Fore.CYAN}  organizer = FileOrganizer()")
    print(f"{Fore.CYAN}  organizer.organize()\n")


def demo_file_operations():
    """
    Demo function showing basic file operations.
    
    This is just an example - modify it to learn!
    """
    print(f"{Fore.BLUE}📁 File Operations Demo\n")
    
    # Get current directory
    current_dir = Path.cwd()
    print(f"Current directory: {Fore.GREEN}{current_dir}")
    
    # List files in current directory
    files = list(current_dir.glob("*.py"))
    print(f"\nPython files found: {Fore.GREEN}{len(files)}")
    
    for file in files[:5]:  # Show first 5
        print(f"  • {file.name}")
    
    print()


def demo_text_processing():
    """Demo function showing text processing."""
    print(f"{Fore.BLUE}📝 Text Processing Demo\n")
    
    sample_text = "Hello, World! Welcome to Python automation."
    
    print(f"Original: {sample_text}")
    print(f"Uppercase: {sample_text.upper()}")
    print(f"Word count: {len(sample_text.split())}")
    print(f"Character count: {len(sample_text)}\n")


def main():
    """Main function - run your experiments here!"""
    
    # Run demo functions
    hello_automation()
    demo_file_operations()
    demo_text_processing()
    
    # Your code here!
    print(f"{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.MAGENTA}✏️  Add your own experiments below!")
    print(f"{Fore.MAGENTA}{'='*60}\n")
    
    # Example: Test file organizer
    # from automation.file_organizer import FileOrganizer
    # organizer = FileOrganizer(dry_run=True)
    # organizer.organize()
    
    # Example: Test chatbot locally
    # from automation.chatbotbasics import LocalChatbot
    # bot = LocalChatbot()
    # response = bot.get_response("Hello!")
    # print(f"Bot says: {response}")
    
    print(f"{Fore.GREEN}✨ Happy experimenting!\n")


if __name__ == "__main__":
    main()
