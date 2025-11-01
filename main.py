import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(phrase: str):
    prompt = f"""
You are a Corsican language tutor specializing in Corsican (Corsu), English, and French.

For the input below:
1. Detect if it's in Corsican, English, or French.
2. Translate accordingly:
   - If Corsican, provide both English AND French translations
   - If English, translate to Corsican
   - If French, translate to Corsican
3. Provide example sentences in the relevant languages.
4. Give a short grammar tip or cultural note about Corsican.

Format your response as:
🌍 Language Detected:
🗣️ Translation(s):
💬 Example Sentences:
💡 Grammar/Cultural Note:
Input: {phrase}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are an expert in the Corsican language (Corsu), helping preserve and teach this endangered language. You're fluent in Corsican, English, and French."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        print("\n" + response.choices[0].message.content.strip() + "\n")
    
    except Exception as e:
        print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    print("🌐 Corsican Language Tutor powered by Groq\n")
    print("Supports: English <-> Corsican | French <-> Corsican\n")
    while True:
        phrase = input("Enter a word or phrase (or 'quit'): ").strip()
        if phrase.lower() in ["quit", "exit"]:
            print("Pace è salute! 👋")
            break
        if phrase:
            ask_ai(phrase)
        else:
            print("⚠️ Please enter a word or phrase.\n")