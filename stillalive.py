import os
import time

from pygame import mixer # Load the required library

mixer.init()
mixer.music.load('audio.mp3')
mixer.music.play()

def draw_board(on_line, text, text_position, icon): # draws still image of the board
    current_line = text[on_line][:text_position] + '_'
    print()
    print()
    print('  ' + '-' * 55 + ' ' + '-' * 55 + ' ')
    line = 0
    text_line = 0
    image_index = 0
    while line < 57: # loops trough and draws parts of board that repeat
        if line % 2 == 0:  # prints even lines
            if line < 29:
                print('  ' + ' ' * 55 + '  ' + ' ' * 57)
            else:
                try:
                    print('  ' + ' ' * 55 + icon[image_index])
                except:
                    print('  ' + ' ' * 55)
                image_index += 1
        else: # print odd lings
            if on_line > text_line: # if we've passed this line
                if line < 29: # for line pluss credits
                    print('  ' + '|' + ' ' + text[text_line] + ' ' * (52-len(text[text_line])) + '|' + '|' + ' ' * 55 + '|')
                    text_line += 1
                elif line == 29: # for bottom of credits
                    print('  ' + '|' + ' ' + text[text_line] + ' ' * (52-len(text[text_line])) + '|' + '|' + '-' * 55 + '|')
                    text_line += 1
                else: # for after credits
                    try:
                        print('  ' + '|' + ' ' + text[text_line] + ' ' * (52-len(text[text_line])) + '|')
                    except:
                        print('  ' + '|' + ' ' + text[text_line] + ' ' * (52-len(text[text_line])) + '|' + icon[image_index])
                    image_index += 1
                    text_line += 1
            elif on_line == text_line: # if were on this line
                if line < 29: # for line pluss credits
                    print('  ' + '|' + ' ' + current_line + ' ' * (52 - len(current_line))+ '|' + '|' + ' ' * 55 + '|')
                    text_line += 1
                elif line == 29: # for bottom of credits
                    print('  ' + '|' + ' ' + current_line + ' ' * (52 - len(current_line))+ '|' + '|' + '-' * 55 + '|')
                    text_line += 1
                else: # for after credits
                    try:
                        print('  ' + '|' + ' ' + current_line + ' ' * (52 - len(current_line))+ '|' + icon[image_index])
                    except:
                        print('  ' + '|' + ' ' + current_line + ' ' * (52 - len(current_line))+ '|')
                    image_index += 1
                    text_line += 1
            else: #below this line
                if line < 29:# for line pluss credits
                    print('  ' + '|' + ' ' * 53 + '|' + '|' + ' ' * 55 + '|')
                    text_line += 1
                elif line == 29: # for bottom of credits
                    print('  ' + '|' + ' ' * 53 + '|' + '|' + '-' * 55 + '|')
                    text_line += 1
                else: # for after credits
                    try:
                        print('  ' + '|' + ' ' * 53 + '|' + icon[image_index])
                    except:
                        print('  ' + '|' + ' ' * 53 + '|')
                    image_index += 1
                    text_line += 1
        line += 1
    print('  ' + '-' * 55)

text = open('page1.txt','r').readlines()
for i in range(len(text)):
    text[i] = text[i].strip('\n')
times = open('times2.txt','r').readlines()
for i in range(len(times)):
    times[i] = times[i].strip('\n')
    times[i] = times[i].split(' ')
    times[i][0] = int(times[i][0])
timer = 0
line = 0
character = 0
time_index = 0
page = 1
pic = ' '
while True:
    time.sleep(.02)

    if timer  == times[time_index][0]:
        character += 1
        if character == len(text[line]):
            character = 0
            line += 1

        time_index += 1
        timer = 0
        if line == len(text):
            page += 1
            text = open('page' + str(page) + '.txt','r').readlines()
            for i in range(len(text)):
                text[i] = text[i].strip('\n')
            timer = 0
            line = 0
            character = 0
        try:
                pic = open(times[time_index][1] + '.txt','r').readlines()
                for i in range(len(pic)):
                    pic[i] = pic[i].strip('\n')
        except:
            pic = ' '
    os.system('clear')
    draw_board(line, text, character, pic)
    timer += 1
