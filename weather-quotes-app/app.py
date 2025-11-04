import random
import sys
from datetime import datetime

quotes = {
    "sunny": [
        "Today is a perfect day to shinee! ☀️",
        "Let the sunshine in your soul! 🌞",
        "Bright days bring bright opportunities! ✨"
    ],
    "rainy": [
        "Every storm runs out of rain 🌧️",
        "Rain is just confetti from the sky! 🌈",
        "Let the rain wash away yesterday's worries 💙"
    ],
    "cloudy": [
        "Behind every cloud is a silver lining ☁️",
        "Cloudy days are perfect for reflection 🤔",
        "Sometimes you need clouds to appreciate the sun 🌤️"
    ]
}

def display_banner():
    print("\n" + "="*50)
    print("🌦️  WEATHER QUOTES APP  🌦️")
    print("="*50)
    print(f"📅 {datetime.now().strftime('%A, %B %d, %Y - %H:%M')}")
    print("="*50 + "\n")

def get_quote(weather):
    if weather.lower() not in quotes:
        return "❓ Please choose: sunny, rainy, or cloudy"
    return random.choice(quotes[weather.lower()])

def main():
    display_banner()
    
    if len(sys.argv) > 1:
        weather = sys.argv[1]
    else:
        print("🌤️  How's the weather today?")
        print("   Choose: sunny, rainy, cloudy\n")
        weather = input("Your choice: ")
    
    print("\n💭 Your quote for today:")
    print(f"   {get_quote(weather)}\n")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()