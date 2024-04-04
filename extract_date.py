# import speech_recognition as sr
# from dateutil import parser

# def extract_date_from_audio(audio_file):
#     # Initialize the recognizer
#     recognizer = sr.Recognizer()

#     # Load audio file
#     with sr.AudioFile(audio_file) as source:
#         audio_data = recognizer.record(source)

#     # Recognize speech
#     try:
#         text = recognizer.recognize_google(audio_data)
#         print("Recognized speech:", text)
        
#         # Parse date from recognized speech
#         date = parser.parse(text, fuzzy=True).date()
#         return date

#     except sr.UnknownValueError:
#         print("Speech recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))
#     except Exception as e:
#         print("An error occurred: {0}".format(e))

# # Replace 'your_audio_file.wav' with the path to your audio file
# audio_file = 'output01.wav'
# date = extract_date_from_audio(audio_file)
# if date:
#     formatted_date = date.strftime("%d/%m/%Y")
#     print("The date is:", formatted_date)






# import speech_recognition as sr
# import re
# from dateparser.search import search_dates

# def extract_dates_from_audio(audio_file):
#     # Initialize the recognizer
#     recognizer = sr.Recognizer()

#     # Load the audio file
#     with sr.AudioFile(audio_file) as source:
#         audio_data = recognizer.record(source)

#     try:
#         # Convert audio to text
#         text = recognizer.recognize_google(audio_data)
#         print("Audio converted to text:", text)

#         # Extract dates from the text using dateparser.search
#         dates = search_dates(text)

#         # Print the extracted dates
#         if dates:
#             print("Extracted dates:")
#             for date_tuple in dates:
#                 # Format the date as dd/mm/yyyy
#                 date_str = date_tuple[1].strftime('%d/%m/%Y')
#                 print(date_str)

#     except sr.UnknownValueError:
#         print("Could not understand the audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Specify the path to your audio file
# audio_file_path = r"C:\Users\ASUS\OneDrive\Desktop\Audio-To-Text\2dates.wav"

# # Call the function to extract dates from the audio
# extract_dates_from_audio(audio_file_path)





#from and to date

import speech_recognition as sr
import re
from dateparser.search import search_dates

def extract_dates_from_audio(audio_file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        # Convert audio to text
        text = recognizer.recognize_google(audio_data)
        print("Audio converted to text:", text)

        # Extract dates from the text using dateparser.search
        dates = search_dates(text)

        # Print the extracted dates
        if dates:
            print("Extracted dates:")
            # Sort the dates by the timestamp
            sorted_dates = sorted(dates, key=lambda x: x[1])
            # Set the first date as the 'From:' date
            print("From Date:", sorted_dates[0][1].strftime('%d/%m/%Y'))
            # Set the last date as the 'To:' date
            print("To Date:", sorted_dates[-1][1].strftime('%d/%m/%Y'))

    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Specify the path to your audio file
audio_file_path = r"C:\Users\ASUS\OneDrive\Desktop\Audio-To-Text\2dates.wav"

# Call the function to extract dates from the audio
extract_dates_from_audio(audio_file_path)