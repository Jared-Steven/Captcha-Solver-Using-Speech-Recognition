# Python program to automatically generate CAPTCHA and
# verify user
import random
import speech_recognition as sr
import pyttsx3 

# Returns true if given two strings are the same
def checkCaptcha(captcha, user_captcha):
    return captcha == user_captcha

# Generates a lowercase CAPTCHA of given length
def generateCaptcha(n):
    # Characters to be included (only lowercase letters)
    chrs = "abcdefghijklmnopqrstuvwxyz"
    
    # Generate n characters from the above set and
    # add these characters to captcha.
    captcha = ""
    while n:
        captcha += chrs[random.randint(0, 25)]
        n -= 1
    return captcha

# Driver code

# Generate a random lowercase CAPTCHA
captcha = generateCaptcha(5)
print("Generated CAPTCHA:", captcha)

# Ask the user to enter a lowercase CAPTCHA
#print("Speak the above CAPTCHA:")
 
#import speech_recognition as sr

def capture_spelling(duration=3):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak the above CAPTCHA:")
        print("Adjusting for ambient noise. Please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=duration)
        audio = recognizer.listen(source)

    try:
        spelling = recognizer.recognize_google(audio)
        print("Spelling: {}".format(spelling))
        return spelling
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    # You can adjust the duration value as needed
    spelling_result = capture_spelling(duration=3)
    if spelling_result:
        usr_captcha = spelling_result.strip(" ")
        if checkCaptcha(str(captcha), str(usr_captcha)):
            print("CAPTCHA Matched")
        else:
            print("CAPTCHA Not Matched")
