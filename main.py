from turtle import Screen, Turtle
import voice_handler

screen = Screen()
screen.setup(width=1500, height=780, startx=0, starty=0)
turtle = Turtle()

engine = voice_handler.init_engine()
voice = voice_handler.get_voice(engine)
voice_handler.speak('Dites stop pour arrêter', voice, engine)

while True:
    voice_handler.speak('Quel angle ?', voice, engine)
    command = voice_handler.get_audio()
    print(command)

    if 'stop' in command:
        break
    else:
        if command.isdigit():
            turtle.left(int(command))

        voice_handler.speak('Quel distance ?', voice, engine)
        command = voice_handler.get_audio()
        print(command)
        if command.isdigit():
            turtle.forward(int(command))

screen.mainloop()