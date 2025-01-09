from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Controller, Browser, BrowserConfig, SystemPrompt
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Verify telemetry is disabled
if os.getenv('ANONYMIZED_TELEMETRY', 'true').lower() != 'false':
    raise EnvironmentError('Telemetry must be disabled. Set ANONYMIZED_TELEMETRY=false in your .env file')

class MySystemPrompt(SystemPrompt):
    def important_rules(self) -> str:
        # Get existing rules from parent class
        existing_rules = super().important_rules()

        # Add your custom rules
        new_rules = """
9. Thinking Framework:
- Always create a logical plan and think really smart and efficiently before you execute any action
"""
        # Make sure to use this pattern otherwise the existing rules will be lost
        return f'{existing_rules}\n{new_rules}'

# Initialize Gemini 2.0 Flash
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp"
)

# Configure browser
config = BrowserConfig(
    headless=False  # Show the browser window
)

# Create custom controller and browser
custom_controller = Controller()
browser = Browser(config=config)

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

async def main():
    try:
        agent = Agent(
            task="@web - Please provide instructions for what you want me to do on the web",  # Default prompt for web tasks
            llm=llm,
            browser=browser,         # Reuse browser instance
            controller=custom_controller,  # Custom function registry
            use_vision=True,              # Enable vision capabilities
            save_conversation_path="logs/conversation.json",  # Save chat logs
            system_prompt_class=MySystemPrompt  # Use custom system prompt class
        )
        result = await agent.run(max_steps=200)
        print(result)
    finally:
        # Ensure browser is closed even if there's an error
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main()) 