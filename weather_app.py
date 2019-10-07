import tkinter as tk
from tkinter import font
import requests

root = tk.Tk()
root.title("Weather")

def format(weather):
    """Function to prepare response from request in proper format"""
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = round(weather['main']['temp'])
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        display_text = 'City: %s \nTemperature: %s°C \nConditions: %s \nPressure: %shPa \nHumidity: %s' % (name, temperature, description, pressure, humidity)
    except:
        display_text = 'Failed to find your City'

    return display_text

def get_weather(city):
    """Function to request weather details from website"""
    weather_key = '87ffbf755d5f6be60265a75403f51468'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,
              'q': city,
              'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format(weather)

def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry.get() == 'Enter your city':
       entry.delete(0, "end") # delete all the text in the entry
       entry.insert(0, '') #Insert blank for user input
       entry.config(fg = 'black')

canvas = tk.Canvas(root, height=600, width=600)
canvas.pack()

background_image = tk.PhotoImage(file='weather.png')
backgroud_label = tk.Label(root, image=background_image)
backgroud_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#f5b342", bd=5 ) # ramka na wpisanie miasta i przycisk
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') #rel = relative / positioning a frame in the window

top_label = tk.Label(root, bg="light blue", bd=5, font=("Arial", 13), text="Welcome to my Weather Application")
top_label.place(relx=0.25, y=12, relwidth=0.5, relheight=0.08,)

entry = tk.Entry(frame, font=("Courier", 15), bg='#e6f2ff', justify='center')
entry.place(relwidth=0.65, relheight=1)
entry.insert(0, 'Enter your city')
entry.bind('<FocusIn>', on_entry_click)

button = tk.Button(frame, text="Find city", font=("Courier",10), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#f5b342", bd=10) # krawedzie duzego pola na dole
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='#bcd4e6', font=("Courier", 18), anchor='center', justify='center', bd=4) #wypelnienie duzego pola
label.place(relwidth=1, relheight=1)

root.mainloop()
