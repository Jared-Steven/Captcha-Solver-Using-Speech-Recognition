# Capthca-Solver-Using-Speech-Recognition

This Python program automatically generates a CAPTCHA and verifies user input via speech recognition.

## Features
- Generates a random CAPTCHA using lowercase letters.
- Captures user input via microphone and recognizes speech.
- Compares the spoken CAPTCHA with the generated CAPTCHA for verification.

## Requirements
- Python 3.x
- `speech_recognition` library
- `pyttsx3` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Jared-Steven/Capthca-Solver-Using-Speech-Recognition.git
    ```
2. Install the required libraries:
    ```sh
    pip install speechrecognition pyttsx3
    ```

## Usage
1. Run the program:
    ```sh
    python captcha solver.py
    ```
2. The program will generate a random CAPTCHA and print it.
3. Speak the CAPTCHA into the microphone when prompted.
4. The program will check if the spoken CAPTCHA matches the generated CAPTCHA and provide feedback.

