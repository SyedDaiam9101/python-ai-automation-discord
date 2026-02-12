"""
Smart File Organizer - Automatically organize files by type

This script helps you clean up messy folders by automatically organizing
files into categorized folders based on their extensions.

Author: Python AI Automation Lab
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)


class FileOrganizer:
    """Organizes files into categorized folders based on file extensions."""
    
    # File type categories and their extensions
    CATEGORIES: Dict[str, List[str]] = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.odt'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h'],
        'Executables': ['.exe', '.msi', '.apk', '.app', '.deb', '.rpm'],
    }
    
    def __init__(self, source_dir: str = ".", dry_run: bool = True):
        """
        Initialize the File Organizer.
        
        Args:
            source_dir: Directory to organize (default: current directory)
            dry_run: If True, only show what would be done without moving files
        """
        self.source_dir = Path(source_dir).resolve()
        self.dry_run = dry_run
        self.stats = {'moved': 0, 'skipped': 0, 'errors': 0}
    
    def get_category(self, file_path: Path) -> str:
        """
        Determine the category for a file based on its extension.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Category name or 'Others' if no match found
        """
        extension = file_path.suffix.lower()
        
        for category, extensions in self.CATEGORIES.items():
            if extension in extensions:
                return category
        
        return 'Others'
    
    def organize(self) -> None:
        """
        Organize files in the source directory into categorized folders.
        """
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}📁 Smart File Organizer")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        if self.dry_run:
            print(f"{Fore.YELLOW}🔍 DRY RUN MODE - No files will be moved")
            print(f"{Fore.YELLOW}Set dry_run=False to actually move files\n")
        
        print(f"📂 Scanning: {Fore.GREEN}{self.source_dir}\n")
        
        # Get all files in the directory (not subdirectories)
        files = [f for f in self.source_dir.iterdir() if f.is_file()]
        
        if not files:
            print(f"{Fore.YELLOW}⚠️  No files found to organize!")
            return
        
        print(f"Found {Fore.GREEN}{len(files)}{Style.RESET_ALL} files to process\n")
        
        # Process each file
        for file_path in files:
            try:
                # Skip this script itself
                if file_path.name == Path(__file__).name:
                    continue
                
                category = self.get_category(file_path)
                category_dir = self.source_dir / category
                destination = category_dir / file_path.name
                
                # Show what will happen
                print(f"  {Fore.BLUE}📄 {file_path.name}")
                print(f"     → {Fore.GREEN}{category}/")
                
                if not self.dry_run:
                    # Create category folder if it doesn't exist
                    category_dir.mkdir(exist_ok=True)
                    
                    # Handle file name conflicts
                    if destination.exists():
                        base = destination.stem
                        ext = destination.suffix
                        counter = 1
                        while destination.exists():
                            destination = category_dir / f"{base}_{counter}{ext}"
                            counter += 1
                        print(f"     {Fore.YELLOW}⚠️  Renamed to: {destination.name}")
                    
                    # Move the file
                    shutil.move(str(file_path), str(destination))
                    self.stats['moved'] += 1
                else:
                    self.stats['moved'] += 1
                
            except Exception as e:
                print(f"     {Fore.RED}❌ Error: {str(e)}")
                self.stats['errors'] += 1
        
        # Print summary
        self._print_summary()
    
    def _print_summary(self) -> None:
        """Print organization summary statistics."""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}📊 Summary")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        if self.dry_run:
            print(f"{Fore.GREEN}✓ {self.stats['moved']} files would be organized")
        else:
            print(f"{Fore.GREEN}✓ {self.stats['moved']} files organized successfully")
        
        if self.stats['errors'] > 0:
            print(f"{Fore.RED}✗ {self.stats['errors']} errors occurred")
        
        print()


def main():
    """Main function to run the file organizer."""
    print(f"\n{Fore.MAGENTA}Welcome to Smart File Organizer! 🎯\n")
    
    # Get user input
    source = input(f"Enter folder path to organize (or press Enter for current folder): ").strip()
    if not source:
        source = "."
    
    # Confirm before proceeding
    print(f"\n{Fore.YELLOW}This will organize files in: {Fore.GREEN}{Path(source).resolve()}")
    
    # First, do a dry run
    print(f"\n{Fore.CYAN}Running preview mode first...\n")
    organizer = FileOrganizer(source_dir=source, dry_run=True)
    organizer.organize()
    
    # Ask if user wants to proceed
    proceed = input(f"\n{Fore.YELLOW}Proceed with organizing? (yes/no): ").strip().lower()
    
    if proceed in ['yes', 'y']:
        print(f"\n{Fore.GREEN}Organizing files...\n")
        organizer = FileOrganizer(source_dir=source, dry_run=False)
        organizer.organize()
        print(f"{Fore.GREEN}✨ Done! Your files are now organized.\n")
    else:
        print(f"\n{Fore.YELLOW}Operation cancelled. No files were moved.\n")


if __name__ == "__main__":
    main()
