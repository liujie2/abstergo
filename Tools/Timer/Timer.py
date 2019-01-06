import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
'''
    Function:
        timer convert
'''
def Convert(t):
    D = t % 10
    B = (t // 100) % 6
    C = (t // 10) % 10
    A = t // 600
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)

'''
    Function:
        Start method
'''
def Start():
    global timer, color
    color = 'white'
    if not timer.is_running():
        timer.start()

'''
    Function
        Stop method
'''
def Stop():
    global timer, color
    timer.stop()
    color = 'red'

'''
    Function
        Clear method
'''
def Clear():
    global t, timer, color
    timer.stop()
    t = 0
    color = 'red'

'''
    Function:
        drawhandler method
'''
def drawHandler(canvas):
    t_convert = Convert(t)
    canvas.draw_text(t_convert, (25, 120), 60, color, 'serif')

'''
    Function:
        timerHandle method
'''
def timerHandler():
    global t
    t += 1

'''
    Function:
        main method
'''
def main():
    global t, color
    t = 0
    color = 'white'
    frame = simplegui.create_frame('Timer', 200, 200, 150)
    # 1000/100 = 10, t increase 10 times as 1 second
    global timer
    timer = simplegui.create_timer(100, timerHandler)
    frame.set_draw_handler(drawHandler)
    button_start = frame.add_button('Start', Start, 150)
    button_stop = frame.add_button('Stop', Stop, 150)
    button_clear = frame.add_button('Clear', Clear, 150)
    frame.start()

if __name__ == '__main__':
    main()