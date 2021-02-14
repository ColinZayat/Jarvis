import wolframalpha

#############################
import sys
additional_paths = [r'C:\Users\colin\AppData\Local\Programs\Python\Python38\lib\site-packages\win32', r'C:\Users\colin\AppData\Local\Programs\Python\Python38\lib\site-packages\win32\lib', r'C:\Users\colin\AppData\Local\Programs\Python\Python38\lib\site-packages\Pythonwin']
sys.path = sys.path + additional_paths
#############################


app_id = 'JRWT5G-62X98LJXET'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client("JRWT5G-62X98LJXET")
res = client.query('temperature in Washington, DC on October 3, 2012')

import wikipedia

##import pyttsx3
##engine = pyttsx3.init()
##engine.say("I will speak this text")
##engine.runAndWait()

import PySimpleGUI as sg                        

sg.theme('Black')
# Define the window's contents
layout = [  [sg.Text("Enter a command")], 
            [sg.Input()],
            [sg.Button('Ok'), ] ]

# Create the window
window = sg.Window('Jarvis', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    try:
        wiki_res = wikipedia.summary(values[0])
    except:
        wiki_res = "Wikipedia No info \n"

    try:
        res = client.query(values[0])
        wolfram_res = next(res.results).text
    except:
        wolfram_res = "Wolfram No info \n"
    

    total_res = wolfram_res +"\n \n"+ wiki_res  
    sg.Popup(total_res, title = "Jarvis Answer")
    
    

# Finish up by removing from the screen
window.close()           


