import gradio as gr
import google.generativeai as genai
import random

# Configure Gemini API
genai.configure(api_key="AIzaSyABjjtDkWlJTGYgy5mkagHlDAEhpPTm1JI")  # Replace with your actual key

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Tip + Habit + Mood bank
snack_tips = [
    "Roasted makhana is low in calories and high in protein — perfect for mindful munching.",
    "Greek yogurt with honey and fruit is a great dessert alternative.",
    "Avocados are rich in healthy fats — perfect on toast or with eggs.",
    "Air-popped popcorn with herbs is a great low-calorie crunchy fix.",
    "Cucumber slices with hummus are refreshing and filling."
]

healthy_habits = [
    "Stay hydrated — sometimes cravings are just thirst in disguise.",
    "Always keep 1-2 healthy snacks prepped and ready to grab.",
    "Avoid snacking straight from the packet — portion out instead.",
    "Combine protein + fiber to feel full longer.",
    "Don’t skip meals — it leads to worse cravings later!"
]

moods = [
    "I want something sweet",
    "I'm feeling bored",
    "I need energy",
    "I crave something salty",
    "I'm feeling low",
    "I'm trying to focus",
    "I want something crunchy",
    "I'm stressed out",
    "I'm studying late night",
    "I'm craving junk food",
    "I want something filling",
    "I'm on a break",
    "I want something refreshing",
    "I'm in a hurry",                        
    "I’m working out later",
    "I want a no-cook snack",
    "I just woke up",
    "I’m craving chocolate",
    "I want something warm",
    "I'm feeling snacky but not hungry"
]


# Gemini Prompt Functions
def snack_by_mood(mood):
    prompt = f"""
You are a friendly healthy snack assistant.

The user is feeling: "{mood}"

Based on that mood, suggest 3 healthy, simple snack ideas that can help improve the mood and control cravings.

For each snack, include:
- Snack Name
- Quick recipe or ingredients (1–2 lines)
- Make the suggestions casual, friendly, and motivating
"""
    try:
        response = model.generate_content(prompt)
        result = response.text.strip()
        if not result:
            return "Oops! I couldn't come up with snacks for that mood right now. Try another or click 'Surprise Me'."
        return result
    except Exception as e:
        return f"Something went wrong while fetching snack ideas. Try again or choose a different mood.\n\n(Error: {str(e)})"


def snack_of_the_day():
    mood = random.choice(moods)
    return snack_by_mood(mood)

def tip_of_the_day():
    return f"💡 Tip of the Day:\n{random.choice(snack_tips)}"

def healthy_habit():
    return f"🧠 Healthy Habit:\n{random.choice(healthy_habits)}"

# UI Layout
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    <h1 style='text-align: center; color: #43a047; font-size: 2.8em;'>SnackSmart</h1>
    <h3 style='text-align: center; color: #666;'>Crave Less. Snack Better.</h3>
    <p style='text-align: center; max-width: 700px; margin: auto; font-size: 1.1em;'>
    Your mood-based healthy snack buddy. Select a mood or explore snack ideas, tips, and habits to snack smart anytime.
    </p>
    <hr>
    """)

    with gr.Row():
        with gr.Column(scale=1):
            mood = gr.Dropdown(choices=moods, label="Choose Your Current Mood")
            mood_btn = gr.Button("Suggest Snacks for Mood")
            surprise_btn = gr.Button("Surprise Me (Random Mood)")
            snack_day_btn = gr.Button("Snack of the Day")
            tip_btn = gr.Button("Tip of the Day")
            habit_btn = gr.Button("Healthy Habit")
        with gr.Column(scale=2):
            output = gr.Textbox(label="SnackSmart Suggestions", lines=18, interactive=False)

    # Button Logic
    mood_btn.click(fn=snack_by_mood, inputs=mood, outputs=output)
    surprise_btn.click(fn=lambda: snack_by_mood(random.choice(moods)), inputs=None, outputs=output)
    snack_day_btn.click(fn=snack_of_the_day, inputs=None, outputs=output)
    tip_btn.click(fn=tip_of_the_day, inputs=None, outputs=output)
    habit_btn.click(fn=healthy_habit, inputs=None, outputs=output)

    gr.Markdown("<hr><p style='text-align: center; font-size: 0.9em; color: gray;'>Built using Gemini AI and Gradio • Project: SnackSmart – Crave Less. Snack Better.</p>")

demo.launch()
