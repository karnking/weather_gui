import tkinter as tk
import requests

root = tk.Tk()


def format_weather(weather):
    #try:
        city = weather['name']
        country = weather['sys']['country']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        img_code = 'img/'+weather['weather'][0]['icon']+'.png'
        weather_image['file'] = img_code
        final_string = 'City : %s (%s)\nConditions : %s \nTemperature(°C): %s' % (city, country, description, temp)

    #except:
    #    final_string = 'There was a problem retrieving the information'

        return final_string


def get_weather(city):
    weather_key = '758401b9a8564c2fa7d9182ee5221032'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params)
    weather = response.json()
    final_result = format_weather(weather)
    label['text'] = final_result


HEIGHT = 500
WIDTH = 600

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='Capture001.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="CLick Me", font=('Courier', 11), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 15), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

weather_image = tk.PhotoImage()
weather_label = tk.Label(lower_frame, image=weather_image)
weather_label.place(relx=0.83, rely=0)

root.mainloop()
