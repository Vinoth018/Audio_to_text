
#3dates (From , To, Others)

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
#             # Sort the dates by the timestamp
#             sorted_dates = sorted(dates, key=lambda x: x[1])
#             # Set the first date as the 'From:' date
#             print("From:", sorted_dates[0][1].strftime('%d/%m/%Y'))
#             # Set the last date as the 'To:' date
#             print("To:", sorted_dates[-1][1].strftime('%d/%m/%Y'))
            
#             # If there are more than two dates, show the third date as 'Others:'
#             if len(sorted_dates) > 2:
#                 print("Others:", sorted_dates[1][1].strftime('%d/%m/%Y'))

#     except sr.UnknownValueError:
#         print("Could not understand the audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Specify the path to your audio file
# audio_file_path = r"C:\Users\ASUS\OneDrive\Desktop\Audio-To-Text\Audio\output03.wav"

# # Call the function to extract dates from the audio
# extract_dates_from_audio(audio_file_path)
