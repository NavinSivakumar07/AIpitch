#!/usr/bin/env python3
"""
Check API key configuration for the RAG system
"""

import os
from dotenv import load_dotenv

def check_api_keys():
    """Check if required API keys are configured."""
    
    print("🔑 Checking API Key Configuration")
    print("=" * 40)
    
    # Load environment variables
    load_dotenv()
    
    # Check required API keys
    api_keys = {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'SERPER_API_KEY': os.getenv('SERPER_API_KEY')
    }
    
    all_configured = True
    
    for key_name, key_value in api_keys.items():
        if key_value:
            # Show first 8 and last 4 characters for security
            masked_key = f"{key_value[:8]}...{key_value[-4:]}" if len(key_value) > 12 else "***"
            print(f"✅ {key_name}: {masked_key}")
        else:
            print(f"❌ {key_name}: Not configured")
            all_configured = False
    
    print("\n" + "=" * 40)
    
    if all_configured:
        print("✅ All API keys are configured!")
        print("🚀 The system should be able to:")
        print("   • Perform web research using Serper API")
        print("   • Generate content using OpenAI API")
        print("   • Extract and display research source URLs")
    else:
        print("❌ Some API keys are missing!")
        print("📝 To fix this:")
        print("   1. Create a .env file in the project directory")
        print("   2. Add the missing API keys:")
        for key_name, key_value in api_keys.items():
            if not key_value:
                print(f"      {key_name}=your_api_key_here")
        print("   3. Restart the Streamlit app")
    
    return all_configured

if __name__ == "__main__":
    check_api_keys()
