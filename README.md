# SnackSmart: Your Mood-Based Healthy Snack Buddy 🍎🥦

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

SnackSmart is a web application built with Gradio and the Gemini AI model to help you make healthier snacking choices based on your current mood. Feeling stressed? Craving something sweet? Just woke up? Tell SnackSmart how you're feeling, and it will suggest three simple and healthy snack ideas to improve your mood and control cravings.

## Features

* **Mood-Based Snack Suggestions:** Select your current mood from a dropdown, and Gemini AI will provide tailored healthy snack recommendations.
* **Surprise Me:** Get a random mood selected for you and discover new snack ideas.
* **Snack of the Day:** Receive a daily healthy snack suggestion based on a randomly chosen mood.
* **Tip of the Day:** Get a daily insightful tip related to healthy snacking.
* **Healthy Habit:** Learn a new healthy habit to incorporate into your daily routine.
* **Simple and Friendly Interface:** Built with Gradio for an easy and intuitive user experience.

## How to Use

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd SnackSmart
    ```
    *(Replace `[YOUR_REPOSITORY_URL]` with the actual URL of your GitHub repository)*

2.  **Install Dependencies:**
    ```bash
    pip install gradio google-generativeai
    ```

3.  **Set up Gemini API Key:**
    * Obtain an API key from the [Google Cloud AI Platform](https://console.cloud.google.com/vertex-ai/generative/language).
    * **Important:** Replace `"AIzaSyABjjtDkWlJTGYgy5mkagHlDAEhpPTm1JI"` in the `app.py` file with your actual Gemini API key. **Ensure you keep your API key secure and do not share it publicly.**

4.  **Run the Application:**
    ```bash
    python app.py
    ```

5.  **Access in Your Browser:** The Gradio application will launch, and you'll see a local URL (usually `http://localhost:7860`) in your terminal. Open this URL in your web browser to start using SnackSmart.

## Technologies Used

* **Gradio:** For creating the interactive web interface.
* **Google Gemini AI:** For generating mood-based snack suggestions.
* **Python:** The primary programming language.

## Contributing

Contributions to SnackSmart are welcome! If you have ideas for new features, snack tips, healthy habits, or improvements to the code, feel free to:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

* Powered by the amazing Gemini AI model from Google.
* Built with the user-friendly Gradio library.
* Inspired by the desire to make healthy snacking easier and more enjoyable.

## Project Status

This project is currently under development and may receive updates and new features in the future.

---

**Project: SnackSmart – Crave Less. Snack Better.**
