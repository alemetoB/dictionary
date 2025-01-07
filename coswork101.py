# Spanish to English dictionary
english_to_spanish = {
    "hello": "hola",
    "goodbye": "adios",
    "thank you": "gracias",
    "please": "por favor",
    "yes": "si",
    "no": "no",
    "good morning": "buenos dias",
    "good night": "buenas noches",
    "im sorry": "lo siento",
    "goodbye": "adios",
    'good evening': 'buenos tardes',
    'good afternoon' : "buenos tardes",
    "Familia": 'family',
    'amigo':'friendly',
    "luz" : 'light',
    'agua': 'water',
    'comida' : 'food',
    'casco' : 'helmet',
    'zapatos' : 'shoes'}
from tkinter import Tk, Entry, Button, Label,StringVar

window = Tk()
window.geometry('600x250')
window.title('spanish to english dictionary')

word = StringVar()
word_entry = Entry(window, textvariable=word, font=('ariel', 20))
word_entry.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

def search (word):
    if word in english_to_spanish:
        result.set(english_to_spanish[word])
        print(english_to_spanish[word])
    else:
        result.set('word not found')

search_btn = Button(window, text='search',command=lambda: search(word.get()))
search_btn.pack()


exit_btn = Button(window, text='exit', command=lambda: exit())
exit_btn.pack()

word_entry = Entry(window, textvariable=word, font=('ariel', 20))
window.mainloop()

