"""
AI Chatbot - Interactive chatbot with OpenAI support and local fallback

This chatbot works in two modes:
1. OpenAI Mode - Uses GPT models if you have an API key
2. Local Mode - Simple rule-based responses (no API needed!)

Perfect for learning AI automation without requiring paid APIs.

Author: Python AI Automation Lab
"""

import os
from typing import List, Dict, Optional
from colorama import init, Fore, Style
from dotenv import load_dotenv

# Initialize colorama for colored output
init(autoreset=True)

# Load environment variables
load_dotenv()


class LocalChatbot:
    """Simple rule-based chatbot for when OpenAI API is not available."""
    
    def __init__(self):
        """Initialize the local chatbot with predefined responses."""
        self.conversation_history: List[Dict[str, str]] = []
        
        # Simple response patterns
        self.responses = {
            'hello': "Hi there! I'm running in local mode. How can I help you today?",
            'hi': "Hello! I'm a simple local chatbot. What's on your mind?",
            'how are you': "I'm doing great! I'm a local AI chatbot running without an API. How are you?",
            'bye': "Goodbye! Have a great day!",
            'thanks': "You're welcome! Happy to help!",
            'help': "I'm a simple local chatbot. Try asking me questions or just chat! For full AI power, add an OpenAI API key.",
            'weather': "I can't check the weather in local mode, but I hope it's nice where you are!",
            'name': "I'm a local chatbot - a simple AI without cloud APIs. I'm here to chat!",
        }
    
    def get_response(self, user_message: str) -> str:
        """
        Generate a response based on the user's message.
        
        Args:
            user_message: The user's input message
            
        Returns:
            A response string
        """
        # Store the conversation
        self.conversation_history.append({
            'role': 'user',
            'content': user_message
        })
        
        # Convert to lowercase for matching
        msg_lower = user_message.lower().strip()
        
        # Check for keyword matches
        for keyword, response in self.responses.items():
            if keyword in msg_lower:
                self.conversation_history.append({
                    'role': 'assistant',
                    'content': response
                })
                return response
        
        # Default responses for unknown inputs
        default_responses = [
            f"That's interesting! You said: '{user_message}'. I'm a simple local chatbot, so my responses are limited.",
            f"I heard you say '{user_message}'. In local mode, I can do basic chats. Want to add an OpenAI key for smarter responses?",
            f"Thanks for sharing! I'm running without an API key, so I'm pretty simple. But I'm happy to chat!",
        ]
        
        # Rotate through default responses
        response = default_responses[len(self.conversation_history) % len(default_responses)]
        
        self.conversation_history.append({
            'role': 'assistant',
            'content': response
        })
        
        return response


class OpenAIChatbot:
    """OpenAI-powered chatbot using GPT models."""
    
    def __init__(self, api_key: str):
        """
        Initialize the OpenAI chatbot.
        
        Args:
            api_key: OpenAI API key
        """
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=api_key)
            self.conversation_history: List[Dict[str, str]] = [
                {
                    "role": "system",
                    "content": "You are a helpful, friendly AI assistant. Keep responses concise and engaging."
                }
            ]
            self.available = True
        except ImportError:
            self.available = False
            print(f"{Fore.RED}OpenAI package not installed. Run: pip install openai")
        except Exception as e:
            self.available = False
            print(f"{Fore.RED}Error initializing OpenAI: {str(e)}")
    
    def get_response(self, user_message: str) -> Optional[str]:
        """
        Get a response from OpenAI's GPT model.
        
        Args:
            user_message: The user's input message
            
        Returns:
            AI-generated response or None if error occurs
        """
        if not self.available:
            return None
        
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                max_tokens=150,
                temperature=0.7
            )
            
            # Extract the assistant's message
            assistant_message = response.choices[0].message.content
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            print(f"{Fore.RED}Error getting response: {str(e)}")
            return None


def main():
    """Main function to run the chatbot."""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}🤖 AI Chatbot")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    # Check for OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    
    chatbot = None
    mode = "LOCAL"
    
    if api_key and api_key != "your_api_key_here":
        print(f"{Fore.GREEN}✓ OpenAI API key found! Using GPT-powered mode.\n")
        chatbot = OpenAIChatbot(api_key)
        if chatbot.available:
            mode = "OPENAI"
        else:
            print(f"{Fore.YELLOW}⚠️  Falling back to local mode...\n")
            chatbot = LocalChatbot()
    else:
        print(f"{Fore.YELLOW}ℹ️  No API key found - using local mode (no API needed!)")
        print(f"{Fore.CYAN}💡 Tip: Add OPENAI_API_KEY to .env for smarter responses\n")
        chatbot = LocalChatbot()
    
    # Display mode indicator
    if mode == "LOCAL":
        print(f"{Fore.MAGENTA}🏠 Running in LOCAL MODE - Simple rule-based responses")
    else:
        print(f"{Fore.GREEN}☁️  Running in OPENAI MODE - AI-powered responses")
    
    print(f"{Fore.CYAN}Type 'quit' or 'exit' to end the conversation\n")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    # Chat loop
    while True:
        try:
            # Get user input
            user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"\n{Fore.CYAN}👋 Thanks for chatting! Goodbye!\n")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Get response
            response = chatbot.get_response(user_input)
            
            if response:
                print(f"{Fore.BLUE}Bot: {Style.RESET_ALL}{response}\n")
            else:
                # Fallback to local mode if OpenAI fails
                if mode == "OPENAI":
                    print(f"{Fore.YELLOW}⚠️  OpenAI error, switching to local mode...\n")
                    chatbot = LocalChatbot()
                    mode = "LOCAL"
                    response = chatbot.get_response(user_input)
                    print(f"{Fore.BLUE}Bot: {Style.RESET_ALL}{response}\n")
        
        except KeyboardInterrupt:
            print(f"\n\n{Fore.CYAN}👋 Chat interrupted. Goodbye!\n")
            break
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()
