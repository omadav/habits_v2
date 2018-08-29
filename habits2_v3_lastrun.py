#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on August 28, 2018, at 13:32
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'habits_2'  # from the Builder filename that created this script
expInfo = {u'participant': u'01', u'credits_per_rnf': u'20', u'schedule': u'RI', u'interval': u'10', u'session': u'1', u'experimenter': u'o', u'cost_response': u'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\omadav\\Dropbox\\Projects\\Caltech\\Humans\\Habits\\Caltech 2018-2 (Anastasia)\\Task\\habits2_v3.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instr_test_txt = visual.TextStim(win=win, name='instr_test_txt',
    text='\nWelcome. In this experiment you will have the chance to earn some extra money.\n\nUsing your joystick, you will take actions to win coins that will be cashed out for real money. Therefore, the more coins you collect, the more cash we will pay you when you are finished.\n\nCoins can be silver or gold and are worth 0.25 dollars, regardless of color.\n\n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instr1_1"
instr1_1Clock = core.Clock()
instr1_1_txt = visual.TextStim(win=win, name='instr1_1_txt',
    text='During each trial, you will be allowed to perform one of four actions with the joystick: move left, move right, push and pull. \n\nEach allowed movement comes at a cost of 0.01 dollars.\n\nYou will know which action is the correct one by a stimulus that will appear on the screen. An incorrect action will have no effect. \n\nThe following screens will present the stimuli and the correct action you need to take when you see each stimulus.\n\n\n\n\n\n\n\n\n\n(Press any key to continue)',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instr_stim1"
instr_stim1Clock = core.Clock()
instr_stim1_txt = visual.TextStim(win=win, name='instr_stim1_txt',
    text='Below is one of the stimuli you will see.\n\nThis stimuli is a cube that has a button on the left side, so the correct response is to push the button by moving the joystick to the right, as shown in the picture to the right of the cube. \n\nFeel free to try it! \n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
resp_right_img = visual.ImageStim(
    win=win, name='resp_right_img',
    image='stim/right_resp_img.png', mask=None,
    ori=0, pos=(-0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
joy_right_img = visual.ImageStim(
    win=win, name='joy_right_img',
    image='stim/joy_img_right.jpg', mask=None,
    ori=0, pos=(0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_stim2"
instr_stim2Clock = core.Clock()
instr_stim2_txt = visual.TextStim(win=win, name='instr_stim2_txt',
    text='Here is another one of the stimuli you will see.\n\nThis cube has a button on the top, so the correct response is to push the button by pulling the joystick towards you, as shown in the picture to the right of the cube. Feel free to try it!\n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
resp_down_img = visual.ImageStim(
    win=win, name='resp_down_img',
    image='stim/down_resp_img.png', mask=None,
    ori=0, pos=(-0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
joy_down_img = visual.ImageStim(
    win=win, name='joy_down_img',
    image='stim/joy_img_down.jpg', mask=None,
    ori=0, pos=(0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_stim3"
instr_stim3Clock = core.Clock()
instr_stim3_txt = visual.TextStim(win=win, name='instr_stim3_txt',
    text='\nHere is another one of the stimuli you will see.\n\nThis cube has a button on the front, so the correct response is to push the button by pushing the joystick away from you, as shown in the picture to the right of the cube. Feel free to try it!\n\n\n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
resp_up_img = visual.ImageStim(
    win=win, name='resp_up_img',
    image='stim/up_resp_img.png', mask=None,
    ori=0, pos=(-0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
joy_up_img = visual.ImageStim(
    win=win, name='joy_up_img',
    image='stim/joy_img_up.jpg', mask=None,
    ori=0, pos=(0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_stim4"
instr_stim4Clock = core.Clock()
instr_stim4_txt = visual.TextStim(win=win, name='instr_stim4_txt',
    text='Here is another one of the stimuli you will see.\n\nThis cube has a button on the right side, so the correct response is to push the button by moving the joystick to the left, as shown in the picture to the right of the cube. Feel free to try it!\n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
resp_left_image = visual.ImageStim(
    win=win, name='resp_left_image',
    image='stim/left_resp_img.png', mask=None,
    ori=0, pos=(-0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
joy_left_img = visual.ImageStim(
    win=win, name='joy_left_img',
    image='stim/joy_img_left.jpg', mask=None,
    ori=0, pos=(0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr2_3"
instr2_3Clock = core.Clock()
instr2_3_txt = visual.TextStim(win=win, name='instr2_3_txt',
    text='\n\nEvery time you perform the action that corresponds to the stimulus shown on the screen, a triangle will appear at the top of the screen signalling that the relevant response has been made. \n\n\n\n\n\n\nTwo of the actions (for ex., left and right) will give you gold coins when you are rewarded; the other two (for ex., up and down) will give you silver coins when you are rewarded. \n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
trian_img = visual.ImageStim(
    win=win, name='trian_img',
    image='stim/triangle_img.png', mask=None,
    ori=0, pos=(0, 0.3), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
coin1_img = visual.ImageStim(
    win=win, name='coin1_img',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(-0.2, -0.4), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
coin2_img = visual.ImageStim(
    win=win, name='coin2_img',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0.2, -0.4), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "instr_2_3_1"
instr_2_3_1Clock = core.Clock()
instr_2_3_1_txt = visual.TextStim(win=win, name='instr_2_3_1_txt',
    text='During each trial, the coin (either silver or gold) will flash at the center of the screen when you are rewarded. \n\nWe will be collecting these coins in two different piggy banks outside the room, one for the silver coins and one for the gold coins, provided they are not full. \n\nRemember: both gold and silver coins are worth the same.\n\n\n(Press any key to continue)',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instr_2_4"
instr_2_4Clock = core.Clock()
instr_2_4_txt = visual.TextStim(win=win, name='instr_2_4_txt',
    text='Given the nature of the task, not every correct joystick action you make during each trial will give you a coin. \n\nGiven that 0.01 dollars will be subtracted from your earnings every time you perform a correct action, it is to your advantage not to perform the action too many times. This applies to all actions, since they only differ in whether they give you silver or gold coins. \n\nGood luck!\n\n\n\n\n\n\n\n(Please call the experimenter now to start the experiment)',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "training"
trainingClock = core.Clock()
circle_resp = visual.ShapeStim(
    win=win, name='circle_resp',
    vertices=[[-(0.2, 0.2)[0]/2.0,-(0.2, 0.2)[1]/2.0], [+(0.2, 0.2)[0]/2.0,-(0.2, 0.2)[1]/2.0], [0,(0.2, 0.2)[1]/2.0]],
    ori=0, pos=(0, 0.85),
    lineWidth=2, lineColor=[1.000,0.004,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
stim = visual.ImageStim(
    win=win, name='stim',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

#### BEGIN EXPERIMENT SNIPPET ####

# Import joystick libraries
from psychopy.hardware import joystick
from psychopy import visual

joystick.backend='pyglet'  # must match the Window created

nJoys = joystick.getNumJoysticks()  # to check if we have any joysticks connected
id = 0
joy = joystick.Joystick(id)  # id must be <= nJoys - 1

# Load sounds
coin_sound = sound.Sound('sounds/coin.wav')
reward_sound = sound.Sound('sounds/reward2.wav')

# Create a csv file to save response times etc. Previous one is the native Psychopy file.
#file_name = 'data/S%s_session%s_%s_dev%s' %(expInfo['participant'], expInfo['session'], expInfo['date'], expInfo['devalued'])
#csv_file = open(file_name+'.csv', 'wb')
#writer_object = csv.writer(csv_file, delimiter=",") # create object to write in

#writer_object.writerow(['resp', 't', 'participant', 'trial', 'session'])

# Initialise some variables

# Should we show the debugging msgs on screen?
# In the present experiment, this means showing the credits on the screen
debugging = True

# Initialise credits
credits = 0.0

nReinforcers = 0
nResp = 0

# create array to save last two frames for joystick position
joy_posx_array, joy_posy_array = [], []
window = 2 # maximum length of array (2 if you want the joy pos for 2 frames, for ex)

# Create some text box objects for debugging purposes
num_credits_txt = visual.TextBox(window=win, text=' ', font_size=50,
                         font_color=[-1, -1, 1], size=(1.9, .3), pos=(0.7, -0.95), 
                         grid_horz_justification='center', units='norm')

joy_pos_array_txt = visual.TextBox(window=win, text='', font_size=20,
                         font_color=[1, 1, 1], size=(1.9, .3), pos=(-0.7, 0.5), 
                         grid_horz_justification='center', units='norm')

credits_title_txt = visual.TextBox(window=win, text='Credits', font_size=80,
                         font_color=[1,1,1], size=(1.9, .3), pos=(0.7, -0.8), 
                         grid_horz_justification='center', units='norm')

def show_debugging_stuff():
    ''' set text for stims to show every frame '''
    #shouldBeReinforced_txt.setText('Reinforce?: %d' %shouldBeReinforced)
    #joy_pos_array_txt.setText("joy_resp_array: \n" + str(joy_pos_array))
    num_credits_txt.setText(str(credits))
    # Draw stim on screen
    #shouldBeReinforced_txt.draw()
    #joy_pos_array_txt.draw()
    credits_title_txt.draw()
    num_credits_txt.draw()

def checkRnf():
    ''' Once a response has been recorded -resp_made()-,
    this function checks whether it is reinforced
    and gives the reward if shouldBeReinforced flag is True 
    After recording in a csv, goes to the next line '''
    global credits, shouldBeReinforced, nReinforcers # globals because these are used outside
    
    if shouldBeReinforced:
        nReinforcers += 1
        credits += float(expInfo['credits_per_rnf'])
        reward_sound.play()
        for frameN in range(40): # show for bit more than half a sec (60 frames = 1 sec)
            #reward_txt.draw()
            circle_resp.setOpacity(0)
            coin.setOpacity(1)
            win.flip()
    trials.addData("wasRnf", shouldBeReinforced)
    thisExp.nextEntry()

    shouldBeReinforced = 0 # reset shouldBeReinforced flag

def resp_made():
    global credits, nResp # credits var updates troughout the experiment
    ''' after a resp is made, save it in the csv file and show circle '''
    if phase == "training":
        if key_resp_2.keys in ["left", "right"]: # this updates the 2-element array with joy_x pos
            joy_posx_array.pop(0)
            joy_posx_array.append(joy_x)
            # save data in csv 
            trials.addData("key_resp_2.keys", key_resp_2.keys)
            trials.addData("key_resp_2.rt", str(globalClock.getTime()))
            #trials.addData("t", str(globalClock.getTime()))
            #trials.addData("devalued", expInfo['devalued'])

        elif key_resp_2.keys in ["up", "down"]: # this updates the 2-element array with joy_y pos
            joy_posy_array.pop(0)
            joy_posy_array.append(joy_y)
            #save data in csv
            trials.addData("key_resp_2.keys", key_resp_2.keys)
            trials.addData("key_resp_2.rt", str(globalClock.getTime()))
        #thisExp.nextEntry()

    elif phase == "choice":
        if key_resp_4.keys in ["left", "right"]: # this updates the 2-element array with joy_x pos
            joy_posx_array.pop(0)
            joy_posx_array.append(joy_x)
            # save data in csv 
            trials.addData("key_resp_4.keys", key_resp_4.keys)
            trials.addData("key_resp_4.rt", str(globalClock.getTime()))
            #trials.addData("devalued", expInfo['devalued'])

        elif key_resp_4.keys in ["up", "down"]: # this updates the 2-element array with joy_y pos
            joy_posy_array.pop(0)
            joy_posy_array.append(joy_y)
            trials.addData("key_resp_4.keys", key_resp_4.keys)
            trials.addData("key_resp_4.rt", str(globalClock.getTime()))
            #trials.addData("devalued", expInfo['devalued'])
        thisExp.nextEntry() # it does not call giveRnf(), so needs to go to next line in csv here

    if phase == "training":
        if key_resp_2.keys in [corrResp]:
            nResp += 1
            credits -= float(expInfo['cost_response'])
            coin_sound.play()
            #print("correct resp")
            for nframes in range(3):
                circle_resp.setOpacity(1)
                #stim_pressed.setOpacity(1)
            #'resp', 't', 'participant', 'session', 'trial', 
            #writer_object.writerow([key_resp_2.keys, str(globalClock.getTime()), expInfo['participant'], expInfo['session'], str(trials.thisN)])
            checkRnf() # call checkRnf function to see whether it's reinforced
    elif phase == "choice":
        if key_resp_4.keys in [corrResp1, corrResp2]:
            #credits -= 1
            #coin_sound.play() # no sound for choice stage
            #print("correct resp")
            for nframes in range(3):
                circle_resp_choice.setOpacity(1)
                #stim_pressed.setOpacity(1)
            #checkRnf()

#### END BEGIN EXPERIMENT SNIPPET ####

coin = visual.ImageStim(
    win=win, name='coin',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "shouldRun"
shouldRunClock = core.Clock()


# Initialize components for Routine "piggy_bank_partially_full"
piggy_bank_partially_fullClock = core.Clock()
piggy_bank_text = visual.TextStim(win=win, name='piggy_bank_text',
    text='default text',
    font='Comic Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
press_to_continue_txt = visual.TextStim(win=win, name='press_to_continue_txt',
    text='\n\n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)',
    font='Comic Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instr_before_consumption_test"
instr_before_consumption_testClock = core.Clock()
instr_devaluation_txt_3 = visual.TextStim(win=win, name='instr_devaluation_txt_3',
    text='Free Coin Collection!\n\nFor a limited amount of time you will have the chance to collect gold and silver coins by clicking on them with the mouse. \n\nWe will deposit the coins you collect in their respective piggy banks, if they are not already full.\n\nYou will have 7 seconds to collect as many coins as you like. Get ready!\n\n\n(Press any key to continue)  ',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "consumption_test1"
consumption_test1Clock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
gold1 = visual.ImageStim(
    win=win, name='gold1',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0.1, 0.1), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
gold2 = visual.ImageStim(
    win=win, name='gold2',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0, 0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
gold3 = visual.ImageStim(
    win=win, name='gold3',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0.5, 0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
gold4 = visual.ImageStim(
    win=win, name='gold4',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.8, 0.1), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
gold5 = visual.ImageStim(
    win=win, name='gold5',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.3, -0.9), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
gold6 = visual.ImageStim(
    win=win, name='gold6',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.26, 0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
gold7 = visual.ImageStim(
    win=win, name='gold7',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0.3, 0.86), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
gold8 = visual.ImageStim(
    win=win, name='gold8',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0.4, -0.75), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
gold9 = visual.ImageStim(
    win=win, name='gold9',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.35, -0.8), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
gold10 = visual.ImageStim(
    win=win, name='gold10',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.9, 0.9), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
silver1 = visual.ImageStim(
    win=win, name='silver1',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.12, 0), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
silver2 = visual.ImageStim(
    win=win, name='silver2',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.2, 0.28), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
silver3 = visual.ImageStim(
    win=win, name='silver3',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.26, -0.2), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
silver4 = visual.ImageStim(
    win=win, name='silver4',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(-0.2, -0.6), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
silver5 = visual.ImageStim(
    win=win, name='silver5',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(-0.7, -0.8), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
silver6 = visual.ImageStim(
    win=win, name='silver6',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(-0.1, -0.9), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
silver7 = visual.ImageStim(
    win=win, name='silver7',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.28, 0.7), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
silver8 = visual.ImageStim(
    win=win, name='silver8',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.1, -0.7), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
silver9 = visual.ImageStim(
    win=win, name='silver9',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.7, -0.85), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
silver10 = visual.ImageStim(
    win=win, name='silver10',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.6, 0.75), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)


# Initialize components for Routine "instr_after_consumption_test"
instr_after_consumption_testClock = core.Clock()
time_is_up_txt = visual.TextStim(win=win, name='time_is_up_txt',
    text='Time is up!\n\nNow press any key to continue.',
    font='Comic Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "shouldRun_2"
shouldRun_2Clock = core.Clock()


# Initialize components for Routine "piggy_bank_full"
piggy_bank_fullClock = core.Clock()
instr_devaluation_txt = visual.TextStim(win=win, name='instr_devaluation_txt',
    text='The following piggy bank:\n\n\n\n\n\nis now full. \n\nNo further coins can be deposited in this piggy bank.\n\n\n\n\n',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
devalued_piggy_bank_txt = visual.TextStim(win=win, name='devalued_piggy_bank_txt',
    text='default text',
    font='Comic Sans',
    pos=(0, 0.2), height=0.25, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instr_before_consumption_test"
instr_before_consumption_testClock = core.Clock()
instr_devaluation_txt_3 = visual.TextStim(win=win, name='instr_devaluation_txt_3',
    text='Free Coin Collection!\n\nFor a limited amount of time you will have the chance to collect gold and silver coins by clicking on them with the mouse. \n\nWe will deposit the coins you collect in their respective piggy banks, if they are not already full.\n\nYou will have 7 seconds to collect as many coins as you like. Get ready!\n\n\n(Press any key to continue)  ',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "consumption_test1"
consumption_test1Clock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
gold1 = visual.ImageStim(
    win=win, name='gold1',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0.1, 0.1), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
gold2 = visual.ImageStim(
    win=win, name='gold2',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0, 0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
gold3 = visual.ImageStim(
    win=win, name='gold3',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0.5, 0.2), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
gold4 = visual.ImageStim(
    win=win, name='gold4',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.8, 0.1), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
gold5 = visual.ImageStim(
    win=win, name='gold5',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.3, -0.9), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
gold6 = visual.ImageStim(
    win=win, name='gold6',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.26, 0.6), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
gold7 = visual.ImageStim(
    win=win, name='gold7',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0.3, 0.86), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
gold8 = visual.ImageStim(
    win=win, name='gold8',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(0.4, -0.75), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
gold9 = visual.ImageStim(
    win=win, name='gold9',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.35, -0.8), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
gold10 = visual.ImageStim(
    win=win, name='gold10',
    image='stim/gold_coin.png', mask=None,
    ori=0, pos=(-0.9, 0.9), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
silver1 = visual.ImageStim(
    win=win, name='silver1',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.12, 0), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
silver2 = visual.ImageStim(
    win=win, name='silver2',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.2, 0.28), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
silver3 = visual.ImageStim(
    win=win, name='silver3',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.26, -0.2), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
silver4 = visual.ImageStim(
    win=win, name='silver4',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(-0.2, -0.6), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
silver5 = visual.ImageStim(
    win=win, name='silver5',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(-0.7, -0.8), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
silver6 = visual.ImageStim(
    win=win, name='silver6',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(-0.1, -0.9), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
silver7 = visual.ImageStim(
    win=win, name='silver7',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.28, 0.7), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
silver8 = visual.ImageStim(
    win=win, name='silver8',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.1, -0.7), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
silver9 = visual.ImageStim(
    win=win, name='silver9',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.7, -0.85), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
silver10 = visual.ImageStim(
    win=win, name='silver10',
    image='stim/silver_coin.png', mask=None,
    ori=0, pos=(0.6, 0.75), size=(0.22,0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)


# Initialize components for Routine "instr_after_consumption_test"
instr_after_consumption_testClock = core.Clock()
time_is_up_txt = visual.TextStim(win=win, name='time_is_up_txt',
    text='Time is up!\n\nNow press any key to continue.',
    font='Comic Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instr_choice_test"
instr_choice_testClock = core.Clock()
instr_devaluation_txt_2 = visual.TextStim(win=win, name='instr_devaluation_txt_2',
    text='In this last part of the experiment you will have the opportunity to perform two actions during a trial.\n\nThe allowed actions will be signalled by their respective stimuli. For example, if you see the stimuli below you will be allowed to make left and up responses at the same time.\n\n\n\n\n\n\n\n\n\n\nThis time we will not show you the coins you are earning, the flashing triangle, nor the earnings you have so far. However, we will keep inserting the coins you win in their respective piggy banks. Apart from that, nothing about the game has changed, and you should \ncontinue playing as before. \n\n\n \n(Press any key to continue)',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
resp1_img_example = visual.ImageStim(
    win=win, name='resp1_img_example',
    image='stim/left_resp_img.png', mask=None,
    ori=0, pos=(-0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
resp2_img_example = visual.ImageStim(
    win=win, name='resp2_img_example',
    image='stim/up_resp_img.png', mask=None,
    ori=0, pos=(0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "choice_test"
choice_testClock = core.Clock()
circle_resp_choice = visual.ShapeStim(
    win=win, name='circle_resp_choice',
    vertices=[[-(0.2, 0.2)[0]/2.0,-(0.2, 0.2)[1]/2.0], [+(0.2, 0.2)[0]/2.0,-(0.2, 0.2)[1]/2.0], [0,(0.2, 0.2)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=2, lineColor=[1.000,0.004,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,0.004,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)
stim_choice1 = visual.ImageStim(
    win=win, name='stim_choice1',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stim_choice_2 = visual.ImageStim(
    win=win, name='stim_choice_2',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

curtain_img = visual.ImageStim(
    win=win, name='curtain_img',
    image='stim/curtain.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "contingency_test"
contingency_testClock = core.Clock()
contingency_test_instr = visual.TextStim(win=win, name='contingency_test_instr',
    text='Please indicate which coin was associated with the stimuli below.\n\nPress "g" for gold or "s" for silver.\n\n',
    font='Comic Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
stim_contingency_test = visual.ImageStim(
    win=win, name='stim_contingency_test',
    image='sin', mask=None,
    ori=0, pos=(0, -0.6), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "goodbye"
goodbyeClock = core.Clock()
final_txt_1 = visual.TextStim(win=win, name='final_txt_1',
    text='End of the experiment. Thanks for participating!\n\nPlease call the experimenter.\n\n',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
credits_txt = visual.TextStim(win=win, name='credits_txt',
    text='default text',
    font='Comic Sans',
    pos=(0, -0.35), height=0.25, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=-1.0);


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_instr1 = event.BuilderKeyResponse()
# keep track of which components have finished
instr1Components = [instr_test_txt, key_resp_instr1]
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_test_txt* updates
    if t >= 0.0 and instr_test_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_test_txt.tStart = t
        instr_test_txt.frameNStart = frameN  # exact frame index
        instr_test_txt.setAutoDraw(True)
    
    # *key_resp_instr1* updates
    if t >= 0.0 and key_resp_instr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instr1.tStart = t
        key_resp_instr1.frameNStart = frameN  # exact frame index
        key_resp_instr1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_instr1.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr1_1"-------
t = 0
instr1_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()
# keep track of which components have finished
instr1_1Components = [instr1_1_txt, key_resp_11]
for thisComponent in instr1_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr1_1"-------
while continueRoutine:
    # get current time
    t = instr1_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1_1_txt* updates
    if t >= 0.0 and instr1_1_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1_1_txt.tStart = t
        instr1_1_txt.frameNStart = frameN  # exact frame index
        instr1_1_txt.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1_1"-------
for thisComponent in instr1_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr1_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_stim1"-------
t = 0
instr_stim1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
instr_stim1Components = [instr_stim1_txt, key_resp_6, resp_right_img, joy_right_img]
for thisComponent in instr_stim1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_stim1"-------
while continueRoutine:
    # get current time
    t = instr_stim1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_stim1_txt* updates
    if t >= 0.0 and instr_stim1_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_stim1_txt.tStart = t
        instr_stim1_txt.frameNStart = frameN  # exact frame index
        instr_stim1_txt.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *resp_right_img* updates
    if t >= 0.0 and resp_right_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_right_img.tStart = t
        resp_right_img.frameNStart = frameN  # exact frame index
        resp_right_img.setAutoDraw(True)
    
    # *joy_right_img* updates
    if t >= 0.0 and joy_right_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        joy_right_img.tStart = t
        joy_right_img.frameNStart = frameN  # exact frame index
        joy_right_img.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_stim1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_stim1"-------
for thisComponent in instr_stim1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_stim1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_stim2"-------
t = 0
instr_stim2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
instr_stim2Components = [instr_stim2_txt, key_resp_7, resp_down_img, joy_down_img]
for thisComponent in instr_stim2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_stim2"-------
while continueRoutine:
    # get current time
    t = instr_stim2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_stim2_txt* updates
    if t >= 0.0 and instr_stim2_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_stim2_txt.tStart = t
        instr_stim2_txt.frameNStart = frameN  # exact frame index
        instr_stim2_txt.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *resp_down_img* updates
    if t >= 0.0 and resp_down_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_down_img.tStart = t
        resp_down_img.frameNStart = frameN  # exact frame index
        resp_down_img.setAutoDraw(True)
    
    # *joy_down_img* updates
    if t >= 0.0 and joy_down_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        joy_down_img.tStart = t
        joy_down_img.frameNStart = frameN  # exact frame index
        joy_down_img.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_stim2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_stim2"-------
for thisComponent in instr_stim2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_stim2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_stim3"-------
t = 0
instr_stim3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
instr_stim3Components = [instr_stim3_txt, key_resp_8, resp_up_img, joy_up_img]
for thisComponent in instr_stim3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_stim3"-------
while continueRoutine:
    # get current time
    t = instr_stim3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_stim3_txt* updates
    if t >= 0.0 and instr_stim3_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_stim3_txt.tStart = t
        instr_stim3_txt.frameNStart = frameN  # exact frame index
        instr_stim3_txt.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *resp_up_img* updates
    if t >= 0.0 and resp_up_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_up_img.tStart = t
        resp_up_img.frameNStart = frameN  # exact frame index
        resp_up_img.setAutoDraw(True)
    
    # *joy_up_img* updates
    if t >= 0.0 and joy_up_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        joy_up_img.tStart = t
        joy_up_img.frameNStart = frameN  # exact frame index
        joy_up_img.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_stim3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_stim3"-------
for thisComponent in instr_stim3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_stim3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_stim4"-------
t = 0
instr_stim4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
instr_stim4Components = [instr_stim4_txt, key_resp_9, resp_left_image, joy_left_img]
for thisComponent in instr_stim4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_stim4"-------
while continueRoutine:
    # get current time
    t = instr_stim4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_stim4_txt* updates
    if t >= 0.0 and instr_stim4_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_stim4_txt.tStart = t
        instr_stim4_txt.frameNStart = frameN  # exact frame index
        instr_stim4_txt.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *resp_left_image* updates
    if t >= 0.0 and resp_left_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_left_image.tStart = t
        resp_left_image.frameNStart = frameN  # exact frame index
        resp_left_image.setAutoDraw(True)
    
    # *joy_left_img* updates
    if t >= 0.0 and joy_left_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        joy_left_img.tStart = t
        joy_left_img.frameNStart = frameN  # exact frame index
        joy_left_img.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_stim4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_stim4"-------
for thisComponent in instr_stim4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_stim4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr2_3"-------
t = 0
instr2_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
instr2_3Components = [instr2_3_txt, key_resp_10, trian_img, coin1_img, coin2_img]
for thisComponent in instr2_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr2_3"-------
while continueRoutine:
    # get current time
    t = instr2_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2_3_txt* updates
    if t >= 0.0 and instr2_3_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2_3_txt.tStart = t
        instr2_3_txt.frameNStart = frameN  # exact frame index
        instr2_3_txt.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *trian_img* updates
    if t >= 0.0 and trian_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        trian_img.tStart = t
        trian_img.frameNStart = frameN  # exact frame index
        trian_img.setAutoDraw(True)
    
    # *coin1_img* updates
    if t >= 0.0 and coin1_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        coin1_img.tStart = t
        coin1_img.frameNStart = frameN  # exact frame index
        coin1_img.setAutoDraw(True)
    
    # *coin2_img* updates
    if t >= 0.0 and coin2_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        coin2_img.tStart = t
        coin2_img.frameNStart = frameN  # exact frame index
        coin2_img.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2_3"-------
for thisComponent in instr2_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr2_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_2_3_1"-------
t = 0
instr_2_3_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_18 = event.BuilderKeyResponse()
# keep track of which components have finished
instr_2_3_1Components = [instr_2_3_1_txt, key_resp_18]
for thisComponent in instr_2_3_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_2_3_1"-------
while continueRoutine:
    # get current time
    t = instr_2_3_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2_3_1_txt* updates
    if t >= 0.0 and instr_2_3_1_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_2_3_1_txt.tStart = t
        instr_2_3_1_txt.frameNStart = frameN  # exact frame index
        instr_2_3_1_txt.setAutoDraw(True)
    
    # *key_resp_18* updates
    if t >= 0.0 and key_resp_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_18.tStart = t
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_18.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_2_3_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_2_3_1"-------
for thisComponent in instr_2_3_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_2_3_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_2_4"-------
t = 0
instr_2_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()
# keep track of which components have finished
instr_2_4Components = [instr_2_4_txt, key_resp_13]
for thisComponent in instr_2_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_2_4"-------
while continueRoutine:
    # get current time
    t = instr_2_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2_4_txt* updates
    if t >= 0.0 and instr_2_4_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_2_4_txt.tStart = t
        instr_2_4_txt.frameNStart = frameN  # exact frame index
        instr_2_4_txt.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['c'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_2_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_2_4"-------
for thisComponent in instr_2_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_2_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_piggy_bank_'+expInfo['session']+'.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions3.xlsx', selection='0:6'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "training"-------
        t = 0
        trainingClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_2 = event.BuilderKeyResponse()
        stim.setPos(position)
        stim.setImage(stimulus)
        
        #### BEGIN ROUTINE SNIPPET FOR TRAINING ROUTINE ####
        
        # Initialise parameters at the beginning of each block (routine)
        phase = "training"
        
        shouldBeReinforced = 0 # flag to set next reinforcer for RI schedule
        
        tickClock = core.CountdownTimer(1) # this is to tick every second for reward availability in the RI schedule
        
        #print(expInfo['session'])
        
        #### FINISH BEGIN ROUTINE SNIPPET FOR TRAINING ROUTINE ####
        
        coin.setImage(coin_img)
        # keep track of which components have finished
        trainingComponents = [key_resp_2, circle_resp, stim, coin]
        for thisComponent in trainingComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "training"-------
        while continueRoutine:
            # get current time
            t = trainingClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_2* updates
            if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_2.status == STARTED and t >= frameRemains:
                key_resp_2.status = STOPPED
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['up', 'down', 'left', 'right', 'escape'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # *circle_resp* updates
            if t >= 0.0 and circle_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                circle_resp.tStart = t
                circle_resp.frameNStart = frameN  # exact frame index
                circle_resp.setAutoDraw(True)
            frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if circle_resp.status == STARTED and t >= frameRemains:
                circle_resp.setAutoDraw(False)
            if circle_resp.status == STARTED:  # only update if drawing
                circle_resp.setOpacity(0, log=False)
            
            # *stim* updates
            if t >= 0.0 and stim.status == NOT_STARTED:
                # keep track of start time/frame for later
                stim.tStart = t
                stim.frameNStart = frameN  # exact frame index
                stim.setAutoDraw(True)
            frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if stim.status == STARTED and t >= frameRemains:
                stim.setAutoDraw(False)
            
            #### EACH FRAME SNIPPET ####
            
            # show debugging stuff?
            if debugging:
                show_debugging_stuff()
            
            # Get position of x and y in joystick
            joy_x, joy_y = joy.getX(), joy.getY()
            
            joy_posx_array.append(joy_x)
            joy_posy_array.append(joy_y)
            
            if len(joy_posx_array) > 2:
                joy_posx_array.pop(0)
            
            if len(joy_posy_array) > 2:
                joy_posy_array.pop(0)
            
            # check whether reward is available to collect
            # this runs only if a response is not currently being made
            # this avoids rewarding maintaining the joystick in a position
            
            if joy_posx_array not in [[1, 1], [-1,-1]] and joy_posy_array not in [[1, 1], [-1,-1]]: # pos_array not in [["left","left"], ["right","right"], ["up", "up"],["down","down"]]:
            
                if not shouldBeReinforced and tickClock.getTime() <= 0:
                    shouldBeReinforced = np.random.binomial(1, 1/int(expInfo["interval"]))
                    tickClock.reset()
            
                # assign key_resp to "up", "down", etc.
                if joy_y == -1:
                    key_resp_2.keys = "up"
                    key_resp_2.rt = str(globalClock.getTime())
                    resp_made() 
                elif joy_y == 1:
                    key_resp_2.keys = "down"
                    key_resp_2.rt = str(globalClock.getTime())
                    resp_made()
                elif joy_x == -1:
                    key_resp_2.keys = "left"
                    key_resp_2.rt = str(globalClock.getTime())
                    resp_made()
                elif joy_x == 1:
                    key_resp_2.keys = "right"
                    key_resp_2.rt = str(globalClock.getTime())
                    resp_made()
                #resp_made() # a response has been recorded; run the functions associated with a response 
            
            #### END EACH FRAME SNIPPET ####
            
            
            # *coin* updates
            if t >= 0.0 and coin.status == NOT_STARTED:
                # keep track of start time/frame for later
                coin.tStart = t
                coin.frameNStart = frameN  # exact frame index
                coin.setAutoDraw(True)
            frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if coin.status == STARTED and t >= frameRemains:
                coin.setAutoDraw(False)
            if coin.status == STARTED:  # only update if drawing
                coin.setOpacity(0.15, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trainingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "training"-------
        for thisComponent in trainingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #### END ROUTINE SNIPPET FOR TRAINING ROUTINE ####
        
        
        
        #### FINISH END ROUTINE SNIPPET FOR TRAINING ROUTINE ####
        # the Routine "training" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "shouldRun"-------
    t = 0
    shouldRunClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if trials_3.thisRepN == 0:
        print("first rep; run the consump test")
        nRepsConsumptionTest = 1
    elif trials_3.thisRepN == 1:    
        print("Last rep; don't run the consump test")
        nRepsConsumptionTest = 1
        nRepsConsumptionTest = 0
    # keep track of which components have finished
    shouldRunComponents = []
    for thisComponent in shouldRunComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "shouldRun"-------
    while continueRoutine:
        # get current time
        t = shouldRunClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in shouldRunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "shouldRun"-------
    for thisComponent in shouldRunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "shouldRun" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_consumption_test = data.TrialHandler(nReps=nRepsConsumptionTest, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('runConsumptionTest.xlsx'),
        seed=None, name='trials_consumption_test')
    thisExp.addLoop(trials_consumption_test)  # add the loop to the experiment
    thisTrials_consumption_test = trials_consumption_test.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_consumption_test.rgb)
    if thisTrials_consumption_test != None:
        for paramName in thisTrials_consumption_test:
            exec('{} = thisTrials_consumption_test[paramName]'.format(paramName))
    
    for thisTrials_consumption_test in trials_consumption_test:
        currentLoop = trials_consumption_test
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_consumption_test.rgb)
        if thisTrials_consumption_test != None:
            for paramName in thisTrials_consumption_test:
                exec('{} = thisTrials_consumption_test[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "piggy_bank_partially_full"-------
        t = 0
        piggy_bank_partially_fullClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        piggy_bank_text.setText(piggy_message)
        key_resp_16 = event.BuilderKeyResponse()
        # keep track of which components have finished
        piggy_bank_partially_fullComponents = [piggy_bank_text, press_to_continue_txt, key_resp_16]
        for thisComponent in piggy_bank_partially_fullComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "piggy_bank_partially_full"-------
        while continueRoutine:
            # get current time
            t = piggy_bank_partially_fullClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *piggy_bank_text* updates
            if t >= 0.0 and piggy_bank_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                piggy_bank_text.tStart = t
                piggy_bank_text.frameNStart = frameN  # exact frame index
                piggy_bank_text.setAutoDraw(True)
            
            # *press_to_continue_txt* updates
            if t >= 0.0 and press_to_continue_txt.status == NOT_STARTED:
                # keep track of start time/frame for later
                press_to_continue_txt.tStart = t
                press_to_continue_txt.frameNStart = frameN  # exact frame index
                press_to_continue_txt.setAutoDraw(True)
            
            # *key_resp_16* updates
            if t >= 0.0 and key_resp_16.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_16.tStart = t
                key_resp_16.frameNStart = frameN  # exact frame index
                key_resp_16.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_resp_16.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in piggy_bank_partially_fullComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "piggy_bank_partially_full"-------
        for thisComponent in piggy_bank_partially_fullComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "piggy_bank_partially_full" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "instr_before_consumption_test"-------
        t = 0
        instr_before_consumption_testClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_15 = event.BuilderKeyResponse()
        # keep track of which components have finished
        instr_before_consumption_testComponents = [instr_devaluation_txt_3, key_resp_15]
        for thisComponent in instr_before_consumption_testComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instr_before_consumption_test"-------
        while continueRoutine:
            # get current time
            t = instr_before_consumption_testClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instr_devaluation_txt_3* updates
            if t >= 0.0 and instr_devaluation_txt_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                instr_devaluation_txt_3.tStart = t
                instr_devaluation_txt_3.frameNStart = frameN  # exact frame index
                instr_devaluation_txt_3.setAutoDraw(True)
            
            # *key_resp_15* updates
            if t >= 0.0 and key_resp_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_15.tStart = t
                key_resp_15.frameNStart = frameN  # exact frame index
                key_resp_15.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_resp_15.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instr_before_consumption_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instr_before_consumption_test"-------
        for thisComponent in instr_before_consumption_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "instr_before_consumption_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "consumption_test1"-------
        t = 0
        consumption_test1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(7.000000)
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        gotValidClick = False  # until a click is received
        # initialise whether coins have been collected or not
        
        # initialise "collected" flag for gold coins
        gold1_collected = 0
        gold2_collected = 0
        gold3_collected = 0
        gold4_collected = 0
        gold5_collected = 0
        gold6_collected = 0
        gold7_collected = 0
        gold8_collected = 0
        gold9_collected = 0
        gold10_collected = 0
        
        # initialise "collected" flag for silver coins
        silver1_collected = 0
        silver2_collected = 0
        silver3_collected = 0
        silver4_collected = 0
        silver5_collected = 0
        silver6_collected = 0
        silver7_collected = 0
        silver8_collected = 0
        silver9_collected = 0
        silver10_collected = 0
        
        # initialise number of collected coins of each type
        nGold, nSilver = 0, 0
        # keep track of which components have finished
        consumption_test1Components = [mouse, gold1, gold2, gold3, gold4, gold5, gold6, gold7, gold8, gold9, gold10, silver1, silver2, silver3, silver4, silver5, silver6, silver7, silver8, silver9, silver10]
        for thisComponent in consumption_test1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "consumption_test1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = consumption_test1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *gold1* updates
            if t >= 0.0 and gold1.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold1.tStart = t
                gold1.frameNStart = frameN  # exact frame index
                gold1.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold1.status == STARTED and t >= frameRemains:
                gold1.setAutoDraw(False)
            if gold1.status == STARTED:  # only update if drawing
                gold1.setOpacity(1, log=False)
            
            # *gold2* updates
            if t >= 0.0 and gold2.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold2.tStart = t
                gold2.frameNStart = frameN  # exact frame index
                gold2.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold2.status == STARTED and t >= frameRemains:
                gold2.setAutoDraw(False)
            if gold2.status == STARTED:  # only update if drawing
                gold2.setOpacity(1, log=False)
            
            # *gold3* updates
            if t >= 0.0 and gold3.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold3.tStart = t
                gold3.frameNStart = frameN  # exact frame index
                gold3.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold3.status == STARTED and t >= frameRemains:
                gold3.setAutoDraw(False)
            if gold3.status == STARTED:  # only update if drawing
                gold3.setOpacity(1, log=False)
            
            # *gold4* updates
            if t >= 0.0 and gold4.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold4.tStart = t
                gold4.frameNStart = frameN  # exact frame index
                gold4.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold4.status == STARTED and t >= frameRemains:
                gold4.setAutoDraw(False)
            if gold4.status == STARTED:  # only update if drawing
                gold4.setOpacity(1, log=False)
            
            # *gold5* updates
            if t >= 0.0 and gold5.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold5.tStart = t
                gold5.frameNStart = frameN  # exact frame index
                gold5.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold5.status == STARTED and t >= frameRemains:
                gold5.setAutoDraw(False)
            if gold5.status == STARTED:  # only update if drawing
                gold5.setOpacity(1, log=False)
            
            # *gold6* updates
            if t >= 0.0 and gold6.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold6.tStart = t
                gold6.frameNStart = frameN  # exact frame index
                gold6.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold6.status == STARTED and t >= frameRemains:
                gold6.setAutoDraw(False)
            if gold6.status == STARTED:  # only update if drawing
                gold6.setOpacity(1, log=False)
            
            # *gold7* updates
            if t >= 0.0 and gold7.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold7.tStart = t
                gold7.frameNStart = frameN  # exact frame index
                gold7.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold7.status == STARTED and t >= frameRemains:
                gold7.setAutoDraw(False)
            if gold7.status == STARTED:  # only update if drawing
                gold7.setOpacity(1, log=False)
            
            # *gold8* updates
            if t >= 0.0 and gold8.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold8.tStart = t
                gold8.frameNStart = frameN  # exact frame index
                gold8.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold8.status == STARTED and t >= frameRemains:
                gold8.setAutoDraw(False)
            if gold8.status == STARTED:  # only update if drawing
                gold8.setOpacity(1, log=False)
            
            # *gold9* updates
            if t >= 0.0 and gold9.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold9.tStart = t
                gold9.frameNStart = frameN  # exact frame index
                gold9.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold9.status == STARTED and t >= frameRemains:
                gold9.setAutoDraw(False)
            if gold9.status == STARTED:  # only update if drawing
                gold9.setOpacity(1, log=False)
            
            # *gold10* updates
            if t >= 0.0 and gold10.status == NOT_STARTED:
                # keep track of start time/frame for later
                gold10.tStart = t
                gold10.frameNStart = frameN  # exact frame index
                gold10.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if gold10.status == STARTED and t >= frameRemains:
                gold10.setAutoDraw(False)
            if gold10.status == STARTED:  # only update if drawing
                gold10.setOpacity(1, log=False)
            
            # *silver1* updates
            if t >= 0.0 and silver1.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver1.tStart = t
                silver1.frameNStart = frameN  # exact frame index
                silver1.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver1.status == STARTED and t >= frameRemains:
                silver1.setAutoDraw(False)
            if silver1.status == STARTED:  # only update if drawing
                silver1.setOpacity(1, log=False)
            
            # *silver2* updates
            if t >= 0.0 and silver2.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver2.tStart = t
                silver2.frameNStart = frameN  # exact frame index
                silver2.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver2.status == STARTED and t >= frameRemains:
                silver2.setAutoDraw(False)
            if silver2.status == STARTED:  # only update if drawing
                silver2.setOpacity(1, log=False)
            
            # *silver3* updates
            if t >= 0.0 and silver3.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver3.tStart = t
                silver3.frameNStart = frameN  # exact frame index
                silver3.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver3.status == STARTED and t >= frameRemains:
                silver3.setAutoDraw(False)
            if silver3.status == STARTED:  # only update if drawing
                silver3.setOpacity(1, log=False)
            
            # *silver4* updates
            if t >= 0.0 and silver4.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver4.tStart = t
                silver4.frameNStart = frameN  # exact frame index
                silver4.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver4.status == STARTED and t >= frameRemains:
                silver4.setAutoDraw(False)
            if silver4.status == STARTED:  # only update if drawing
                silver4.setOpacity(1, log=False)
            
            # *silver5* updates
            if t >= 0.0 and silver5.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver5.tStart = t
                silver5.frameNStart = frameN  # exact frame index
                silver5.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver5.status == STARTED and t >= frameRemains:
                silver5.setAutoDraw(False)
            if silver5.status == STARTED:  # only update if drawing
                silver5.setOpacity(1, log=False)
            
            # *silver6* updates
            if t >= 0.0 and silver6.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver6.tStart = t
                silver6.frameNStart = frameN  # exact frame index
                silver6.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver6.status == STARTED and t >= frameRemains:
                silver6.setAutoDraw(False)
            if silver6.status == STARTED:  # only update if drawing
                silver6.setOpacity(1, log=False)
            
            # *silver7* updates
            if t >= 0.0 and silver7.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver7.tStart = t
                silver7.frameNStart = frameN  # exact frame index
                silver7.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver7.status == STARTED and t >= frameRemains:
                silver7.setAutoDraw(False)
            if silver7.status == STARTED:  # only update if drawing
                silver7.setOpacity(1, log=False)
            
            # *silver8* updates
            if t >= 0.0 and silver8.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver8.tStart = t
                silver8.frameNStart = frameN  # exact frame index
                silver8.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver8.status == STARTED and t >= frameRemains:
                silver8.setAutoDraw(False)
            if silver8.status == STARTED:  # only update if drawing
                silver8.setOpacity(1, log=False)
            
            # *silver9* updates
            if t >= 0.0 and silver9.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver9.tStart = t
                silver9.frameNStart = frameN  # exact frame index
                silver9.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver9.status == STARTED and t >= frameRemains:
                silver9.setAutoDraw(False)
            if silver9.status == STARTED:  # only update if drawing
                silver9.setOpacity(1, log=False)
            
            # *silver10* updates
            if t >= 0.0 and silver10.status == NOT_STARTED:
                # keep track of start time/frame for later
                silver10.tStart = t
                silver10.frameNStart = frameN  # exact frame index
                silver10.setAutoDraw(True)
            frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if silver10.status == STARTED and t >= frameRemains:
                silver10.setAutoDraw(False)
            if silver10.status == STARTED:  # only update if drawing
                silver10.setOpacity(1, log=False)
            
            # if mouse is pressed in one coin, make it disappear and increase nGold or nSilver
            
            # gold
            
            if not gold1_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold1):
                    gold1_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold1_collected:
                gold1.setOpacity(0) # hide the stim
            
            if not gold2_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold2):
                    gold2_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold2_collected:
                gold2.setOpacity(0) # hide the stim
            
            if not gold3_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold3):
                    gold3_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold3_collected:
                gold3.setOpacity(0) # hide the stim
            
            if not gold4_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold4):
                    gold4_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold4_collected:
                gold4.setOpacity(0) # hide the stim
            
            if not gold5_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold5):
                    gold5_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold5_collected:
                gold5.setOpacity(0) # hide the stim
            
            if not gold6_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold6):
                    gold6_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold6_collected:
                gold6.setOpacity(0) # hide the stim
            
            if not gold7_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold7):
                    gold7_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold7_collected:
                gold7.setOpacity(0) # hide the stim
            
            if not gold8_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold8):
                    gold8_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold8_collected:
                gold8.setOpacity(0) # hide the stim
            
            if not gold9_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold9):
                    gold9_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold9_collected:
                gold9.setOpacity(0) # hide the stim
            
            if not gold10_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(gold10):
                    gold10_collected = 1
                    nGold += 1 # increase number of coins collected for this type of coin
            elif gold10_collected:
                gold10.setOpacity(0) # hide the stim
            
            # silver coins
            
            if not silver1_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver1):
                    silver1_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver1_collected:
                silver1.setOpacity(0) # hide the stim
            
            if not silver2_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver2):
                    silver2_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver2_collected:
                silver2.setOpacity(0) # hide the stim
            
            if not silver3_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver3):
                    silver3_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver3_collected:
                silver3.setOpacity(0) # hide the stim
            
            if not silver4_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver4):
                    silver4_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver4_collected:
                silver4.setOpacity(0) # hide the stim
            
            if not silver5_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver5):
                    silver5_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver5_collected:
                silver5.setOpacity(0) # hide the stim
            
            if not silver6_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver6):
                    silver6_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver6_collected:
                silver6.setOpacity(0) # hide the stim
            
            if not silver7_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver7):
                    silver7_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver7_collected:
                silver7.setOpacity(0) # hide the stim
            
            if not silver8_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver8):
                    silver8_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver8_collected:
                silver8.setOpacity(0) # hide the stim
            
            if not silver9_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver9):
                    silver9_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver9_collected:
                silver9.setOpacity(0) # hide the stim
            
            if not silver10_collected: # while coin has not yet been clicked on
                if mouse.isPressedIn(silver10):
                    silver10_collected = 1
                    nSilver += 1 # increase number of coins collected for this type of coin
            elif silver10_collected:
                silver10.setOpacity(0) # hide the stim
            
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in consumption_test1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "consumption_test1"-------
        for thisComponent in consumption_test1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_consumption_test (TrialHandler)
        thisExp.addData('nGold', nGold)
        thisExp.addData('nSilver', nSilver)
        thisExp.nextEntry()
        
        # ------Prepare to start Routine "instr_after_consumption_test"-------
        t = 0
        instr_after_consumption_testClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_17 = event.BuilderKeyResponse()
        # keep track of which components have finished
        instr_after_consumption_testComponents = [time_is_up_txt, key_resp_17]
        for thisComponent in instr_after_consumption_testComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instr_after_consumption_test"-------
        while continueRoutine:
            # get current time
            t = instr_after_consumption_testClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *time_is_up_txt* updates
            if t >= 0.0 and time_is_up_txt.status == NOT_STARTED:
                # keep track of start time/frame for later
                time_is_up_txt.tStart = t
                time_is_up_txt.frameNStart = frameN  # exact frame index
                time_is_up_txt.setAutoDraw(True)
            
            # *key_resp_17* updates
            if t >= 0.0 and key_resp_17.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_17.tStart = t
                key_resp_17.frameNStart = frameN  # exact frame index
                key_resp_17.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_resp_17.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instr_after_consumption_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instr_after_consumption_test"-------
        for thisComponent in instr_after_consumption_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "instr_after_consumption_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed nRepsConsumptionTest repeats of 'trials_consumption_test'
    
# completed 2 repeats of 'trials_3'


# ------Prepare to start Routine "shouldRun_2"-------
t = 0
shouldRun_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# This snippet checks whether session number is 1 or 2
# If it is 1, it does not present the devaluation phase
# (the devaluation is done only at the end of the 2nd session)

if expInfo['session'] == '2':
    print("session 2")
    nRepsChoice = 1
elif expInfo['session'] == '1':
    nRepsChoice = 0
    print("session 1")
else:
    print("something diff from 1 or 2 for session number; weird!")
# keep track of which components have finished
shouldRun_2Components = []
for thisComponent in shouldRun_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "shouldRun_2"-------
while continueRoutine:
    # get current time
    t = shouldRun_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in shouldRun_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "shouldRun_2"-------
for thisComponent in shouldRun_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "shouldRun_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
choice_block = data.TrialHandler(nReps=nRepsChoice, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('runBlock.xlsx'),
    seed=None, name='choice_block')
thisExp.addLoop(choice_block)  # add the loop to the experiment
thisChoice_block = choice_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisChoice_block.rgb)
if thisChoice_block != None:
    for paramName in thisChoice_block:
        exec('{} = thisChoice_block[paramName]'.format(paramName))

for thisChoice_block in choice_block:
    currentLoop = choice_block
    # abbreviate parameter names if possible (e.g. rgb = thisChoice_block.rgb)
    if thisChoice_block != None:
        for paramName in thisChoice_block:
            exec('{} = thisChoice_block[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "piggy_bank_full"-------
    t = 0
    piggy_bank_fullClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    devalued_piggy_bank_txt.setText(devalued_coin)
    key_resp_5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    piggy_bank_fullComponents = [instr_devaluation_txt, devalued_piggy_bank_txt, key_resp_5]
    for thisComponent in piggy_bank_fullComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "piggy_bank_full"-------
    while continueRoutine:
        # get current time
        t = piggy_bank_fullClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_devaluation_txt* updates
        if t >= 0.0 and instr_devaluation_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr_devaluation_txt.tStart = t
            instr_devaluation_txt.frameNStart = frameN  # exact frame index
            instr_devaluation_txt.setAutoDraw(True)
        
        # *devalued_piggy_bank_txt* updates
        if t >= 0.0 and devalued_piggy_bank_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            devalued_piggy_bank_txt.tStart = t
            devalued_piggy_bank_txt.frameNStart = frameN  # exact frame index
            devalued_piggy_bank_txt.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['c'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in piggy_bank_fullComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "piggy_bank_full"-------
    for thisComponent in piggy_bank_fullComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    choice_block.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        choice_block.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "piggy_bank_full" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instr_before_consumption_test"-------
    t = 0
    instr_before_consumption_testClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_15 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instr_before_consumption_testComponents = [instr_devaluation_txt_3, key_resp_15]
    for thisComponent in instr_before_consumption_testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr_before_consumption_test"-------
    while continueRoutine:
        # get current time
        t = instr_before_consumption_testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_devaluation_txt_3* updates
        if t >= 0.0 and instr_devaluation_txt_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr_devaluation_txt_3.tStart = t
            instr_devaluation_txt_3.frameNStart = frameN  # exact frame index
            instr_devaluation_txt_3.setAutoDraw(True)
        
        # *key_resp_15* updates
        if t >= 0.0 and key_resp_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_15.tStart = t
            key_resp_15.frameNStart = frameN  # exact frame index
            key_resp_15.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_15.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_before_consumption_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_before_consumption_test"-------
    for thisComponent in instr_before_consumption_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instr_before_consumption_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "consumption_test1"-------
    t = 0
    consumption_test1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    # initialise whether coins have been collected or not
    
    # initialise "collected" flag for gold coins
    gold1_collected = 0
    gold2_collected = 0
    gold3_collected = 0
    gold4_collected = 0
    gold5_collected = 0
    gold6_collected = 0
    gold7_collected = 0
    gold8_collected = 0
    gold9_collected = 0
    gold10_collected = 0
    
    # initialise "collected" flag for silver coins
    silver1_collected = 0
    silver2_collected = 0
    silver3_collected = 0
    silver4_collected = 0
    silver5_collected = 0
    silver6_collected = 0
    silver7_collected = 0
    silver8_collected = 0
    silver9_collected = 0
    silver10_collected = 0
    
    # initialise number of collected coins of each type
    nGold, nSilver = 0, 0
    # keep track of which components have finished
    consumption_test1Components = [mouse, gold1, gold2, gold3, gold4, gold5, gold6, gold7, gold8, gold9, gold10, silver1, silver2, silver3, silver4, silver5, silver6, silver7, silver8, silver9, silver10]
    for thisComponent in consumption_test1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "consumption_test1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = consumption_test1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *gold1* updates
        if t >= 0.0 and gold1.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold1.tStart = t
            gold1.frameNStart = frameN  # exact frame index
            gold1.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold1.status == STARTED and t >= frameRemains:
            gold1.setAutoDraw(False)
        if gold1.status == STARTED:  # only update if drawing
            gold1.setOpacity(1, log=False)
        
        # *gold2* updates
        if t >= 0.0 and gold2.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold2.tStart = t
            gold2.frameNStart = frameN  # exact frame index
            gold2.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold2.status == STARTED and t >= frameRemains:
            gold2.setAutoDraw(False)
        if gold2.status == STARTED:  # only update if drawing
            gold2.setOpacity(1, log=False)
        
        # *gold3* updates
        if t >= 0.0 and gold3.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold3.tStart = t
            gold3.frameNStart = frameN  # exact frame index
            gold3.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold3.status == STARTED and t >= frameRemains:
            gold3.setAutoDraw(False)
        if gold3.status == STARTED:  # only update if drawing
            gold3.setOpacity(1, log=False)
        
        # *gold4* updates
        if t >= 0.0 and gold4.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold4.tStart = t
            gold4.frameNStart = frameN  # exact frame index
            gold4.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold4.status == STARTED and t >= frameRemains:
            gold4.setAutoDraw(False)
        if gold4.status == STARTED:  # only update if drawing
            gold4.setOpacity(1, log=False)
        
        # *gold5* updates
        if t >= 0.0 and gold5.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold5.tStart = t
            gold5.frameNStart = frameN  # exact frame index
            gold5.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold5.status == STARTED and t >= frameRemains:
            gold5.setAutoDraw(False)
        if gold5.status == STARTED:  # only update if drawing
            gold5.setOpacity(1, log=False)
        
        # *gold6* updates
        if t >= 0.0 and gold6.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold6.tStart = t
            gold6.frameNStart = frameN  # exact frame index
            gold6.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold6.status == STARTED and t >= frameRemains:
            gold6.setAutoDraw(False)
        if gold6.status == STARTED:  # only update if drawing
            gold6.setOpacity(1, log=False)
        
        # *gold7* updates
        if t >= 0.0 and gold7.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold7.tStart = t
            gold7.frameNStart = frameN  # exact frame index
            gold7.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold7.status == STARTED and t >= frameRemains:
            gold7.setAutoDraw(False)
        if gold7.status == STARTED:  # only update if drawing
            gold7.setOpacity(1, log=False)
        
        # *gold8* updates
        if t >= 0.0 and gold8.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold8.tStart = t
            gold8.frameNStart = frameN  # exact frame index
            gold8.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold8.status == STARTED and t >= frameRemains:
            gold8.setAutoDraw(False)
        if gold8.status == STARTED:  # only update if drawing
            gold8.setOpacity(1, log=False)
        
        # *gold9* updates
        if t >= 0.0 and gold9.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold9.tStart = t
            gold9.frameNStart = frameN  # exact frame index
            gold9.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold9.status == STARTED and t >= frameRemains:
            gold9.setAutoDraw(False)
        if gold9.status == STARTED:  # only update if drawing
            gold9.setOpacity(1, log=False)
        
        # *gold10* updates
        if t >= 0.0 and gold10.status == NOT_STARTED:
            # keep track of start time/frame for later
            gold10.tStart = t
            gold10.frameNStart = frameN  # exact frame index
            gold10.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gold10.status == STARTED and t >= frameRemains:
            gold10.setAutoDraw(False)
        if gold10.status == STARTED:  # only update if drawing
            gold10.setOpacity(1, log=False)
        
        # *silver1* updates
        if t >= 0.0 and silver1.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver1.tStart = t
            silver1.frameNStart = frameN  # exact frame index
            silver1.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver1.status == STARTED and t >= frameRemains:
            silver1.setAutoDraw(False)
        if silver1.status == STARTED:  # only update if drawing
            silver1.setOpacity(1, log=False)
        
        # *silver2* updates
        if t >= 0.0 and silver2.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver2.tStart = t
            silver2.frameNStart = frameN  # exact frame index
            silver2.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver2.status == STARTED and t >= frameRemains:
            silver2.setAutoDraw(False)
        if silver2.status == STARTED:  # only update if drawing
            silver2.setOpacity(1, log=False)
        
        # *silver3* updates
        if t >= 0.0 and silver3.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver3.tStart = t
            silver3.frameNStart = frameN  # exact frame index
            silver3.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver3.status == STARTED and t >= frameRemains:
            silver3.setAutoDraw(False)
        if silver3.status == STARTED:  # only update if drawing
            silver3.setOpacity(1, log=False)
        
        # *silver4* updates
        if t >= 0.0 and silver4.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver4.tStart = t
            silver4.frameNStart = frameN  # exact frame index
            silver4.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver4.status == STARTED and t >= frameRemains:
            silver4.setAutoDraw(False)
        if silver4.status == STARTED:  # only update if drawing
            silver4.setOpacity(1, log=False)
        
        # *silver5* updates
        if t >= 0.0 and silver5.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver5.tStart = t
            silver5.frameNStart = frameN  # exact frame index
            silver5.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver5.status == STARTED and t >= frameRemains:
            silver5.setAutoDraw(False)
        if silver5.status == STARTED:  # only update if drawing
            silver5.setOpacity(1, log=False)
        
        # *silver6* updates
        if t >= 0.0 and silver6.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver6.tStart = t
            silver6.frameNStart = frameN  # exact frame index
            silver6.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver6.status == STARTED and t >= frameRemains:
            silver6.setAutoDraw(False)
        if silver6.status == STARTED:  # only update if drawing
            silver6.setOpacity(1, log=False)
        
        # *silver7* updates
        if t >= 0.0 and silver7.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver7.tStart = t
            silver7.frameNStart = frameN  # exact frame index
            silver7.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver7.status == STARTED and t >= frameRemains:
            silver7.setAutoDraw(False)
        if silver7.status == STARTED:  # only update if drawing
            silver7.setOpacity(1, log=False)
        
        # *silver8* updates
        if t >= 0.0 and silver8.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver8.tStart = t
            silver8.frameNStart = frameN  # exact frame index
            silver8.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver8.status == STARTED and t >= frameRemains:
            silver8.setAutoDraw(False)
        if silver8.status == STARTED:  # only update if drawing
            silver8.setOpacity(1, log=False)
        
        # *silver9* updates
        if t >= 0.0 and silver9.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver9.tStart = t
            silver9.frameNStart = frameN  # exact frame index
            silver9.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver9.status == STARTED and t >= frameRemains:
            silver9.setAutoDraw(False)
        if silver9.status == STARTED:  # only update if drawing
            silver9.setOpacity(1, log=False)
        
        # *silver10* updates
        if t >= 0.0 and silver10.status == NOT_STARTED:
            # keep track of start time/frame for later
            silver10.tStart = t
            silver10.frameNStart = frameN  # exact frame index
            silver10.setAutoDraw(True)
        frameRemains = 0.0 + 7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if silver10.status == STARTED and t >= frameRemains:
            silver10.setAutoDraw(False)
        if silver10.status == STARTED:  # only update if drawing
            silver10.setOpacity(1, log=False)
        
        # if mouse is pressed in one coin, make it disappear and increase nGold or nSilver
        
        # gold
        
        if not gold1_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold1):
                gold1_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold1_collected:
            gold1.setOpacity(0) # hide the stim
        
        if not gold2_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold2):
                gold2_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold2_collected:
            gold2.setOpacity(0) # hide the stim
        
        if not gold3_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold3):
                gold3_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold3_collected:
            gold3.setOpacity(0) # hide the stim
        
        if not gold4_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold4):
                gold4_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold4_collected:
            gold4.setOpacity(0) # hide the stim
        
        if not gold5_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold5):
                gold5_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold5_collected:
            gold5.setOpacity(0) # hide the stim
        
        if not gold6_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold6):
                gold6_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold6_collected:
            gold6.setOpacity(0) # hide the stim
        
        if not gold7_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold7):
                gold7_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold7_collected:
            gold7.setOpacity(0) # hide the stim
        
        if not gold8_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold8):
                gold8_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold8_collected:
            gold8.setOpacity(0) # hide the stim
        
        if not gold9_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold9):
                gold9_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold9_collected:
            gold9.setOpacity(0) # hide the stim
        
        if not gold10_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(gold10):
                gold10_collected = 1
                nGold += 1 # increase number of coins collected for this type of coin
        elif gold10_collected:
            gold10.setOpacity(0) # hide the stim
        
        # silver coins
        
        if not silver1_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver1):
                silver1_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver1_collected:
            silver1.setOpacity(0) # hide the stim
        
        if not silver2_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver2):
                silver2_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver2_collected:
            silver2.setOpacity(0) # hide the stim
        
        if not silver3_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver3):
                silver3_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver3_collected:
            silver3.setOpacity(0) # hide the stim
        
        if not silver4_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver4):
                silver4_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver4_collected:
            silver4.setOpacity(0) # hide the stim
        
        if not silver5_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver5):
                silver5_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver5_collected:
            silver5.setOpacity(0) # hide the stim
        
        if not silver6_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver6):
                silver6_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver6_collected:
            silver6.setOpacity(0) # hide the stim
        
        if not silver7_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver7):
                silver7_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver7_collected:
            silver7.setOpacity(0) # hide the stim
        
        if not silver8_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver8):
                silver8_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver8_collected:
            silver8.setOpacity(0) # hide the stim
        
        if not silver9_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver9):
                silver9_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver9_collected:
            silver9.setOpacity(0) # hide the stim
        
        if not silver10_collected: # while coin has not yet been clicked on
            if mouse.isPressedIn(silver10):
                silver10_collected = 1
                nSilver += 1 # increase number of coins collected for this type of coin
        elif silver10_collected:
            silver10.setOpacity(0) # hide the stim
        
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consumption_test1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "consumption_test1"-------
    for thisComponent in consumption_test1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for choice_block (TrialHandler)
    thisExp.addData('nGold', nGold)
    thisExp.addData('nSilver', nSilver)
    thisExp.nextEntry()
    
    # ------Prepare to start Routine "instr_after_consumption_test"-------
    t = 0
    instr_after_consumption_testClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_17 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instr_after_consumption_testComponents = [time_is_up_txt, key_resp_17]
    for thisComponent in instr_after_consumption_testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr_after_consumption_test"-------
    while continueRoutine:
        # get current time
        t = instr_after_consumption_testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *time_is_up_txt* updates
        if t >= 0.0 and time_is_up_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            time_is_up_txt.tStart = t
            time_is_up_txt.frameNStart = frameN  # exact frame index
            time_is_up_txt.setAutoDraw(True)
        
        # *key_resp_17* updates
        if t >= 0.0 and key_resp_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_17.tStart = t
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_17.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_after_consumption_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_after_consumption_test"-------
    for thisComponent in instr_after_consumption_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instr_after_consumption_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instr_choice_test"-------
    t = 0
    instr_choice_testClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_14 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instr_choice_testComponents = [instr_devaluation_txt_2, key_resp_14, resp1_img_example, resp2_img_example]
    for thisComponent in instr_choice_testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr_choice_test"-------
    while continueRoutine:
        # get current time
        t = instr_choice_testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_devaluation_txt_2* updates
        if t >= 0.0 and instr_devaluation_txt_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr_devaluation_txt_2.tStart = t
            instr_devaluation_txt_2.frameNStart = frameN  # exact frame index
            instr_devaluation_txt_2.setAutoDraw(True)
        
        # *key_resp_14* updates
        if t >= 0.0 and key_resp_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_14.tStart = t
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_14.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *resp1_img_example* updates
        if t >= 0.0 and resp1_img_example.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp1_img_example.tStart = t
            resp1_img_example.frameNStart = frameN  # exact frame index
            resp1_img_example.setAutoDraw(True)
        
        # *resp2_img_example* updates
        if t >= 0.0 and resp2_img_example.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp2_img_example.tStart = t
            resp2_img_example.frameNStart = frameN  # exact frame index
            resp2_img_example.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_choice_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_choice_test"-------
    for thisComponent in instr_choice_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instr_choice_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions3.xlsx', selection='6:8'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "choice_test"-------
        t = 0
        choice_testClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4 = event.BuilderKeyResponse()
        stim_choice1.setPos(position1)
        stim_choice1.setImage(stimulus_choice1)
        stim_choice_2.setPos(position2)
        stim_choice_2.setImage(stimulus_choice2)
        
        #### BEGIN ROUTINE SNIPPET FOR CHOICE TEST ####
        phase = "choice" 
        
        shouldBeReinforced = 0 # just in case not running the training stage for debugging purposes
        tickClock = core.CountdownTimer(1) # same reason as line above
        
        if expInfo['session'] == 1: # set rep of choice trial to zero if in first session (no devaluation yet)
            trials_2.nReps = 0
        
        shouldBeReinforced_1, shouldBeReinforced_2 = 0, 0 # set rnf flag for two options
        
        tickClock1, tickClock2 = core.CountdownTimer(1), core.CountdownTimer(1) # this is to tick every second for reward availability
        
        #### END BEGIN ROUTINE SNIPPET FOR CHOICE TEST ####
        
        # keep track of which components have finished
        choice_testComponents = [circle_resp_choice, key_resp_4, stim_choice1, stim_choice_2, curtain_img]
        for thisComponent in choice_testComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "choice_test"-------
        while continueRoutine:
            # get current time
            t = choice_testClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *circle_resp_choice* updates
            if t >= 0.0 and circle_resp_choice.status == NOT_STARTED:
                # keep track of start time/frame for later
                circle_resp_choice.tStart = t
                circle_resp_choice.frameNStart = frameN  # exact frame index
                circle_resp_choice.setAutoDraw(True)
            frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if circle_resp_choice.status == STARTED and t >= frameRemains:
                circle_resp_choice.setAutoDraw(False)
            if circle_resp_choice.status == STARTED:  # only update if drawing
                circle_resp_choice.setOpacity(0, log=False)
            
            # *key_resp_4* updates
            if t >= 0.0 and key_resp_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_4.tStart = t
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_4.status == STARTED and t >= frameRemains:
                key_resp_4.status = STOPPED
            if key_resp_4.status == STARTED:
                theseKeys = event.getKeys(keyList=['up', 'down', 'left', 'right', 'escape'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # *stim_choice1* updates
            if t >= 0.0 and stim_choice1.status == NOT_STARTED:
                # keep track of start time/frame for later
                stim_choice1.tStart = t
                stim_choice1.frameNStart = frameN  # exact frame index
                stim_choice1.setAutoDraw(True)
            frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if stim_choice1.status == STARTED and t >= frameRemains:
                stim_choice1.setAutoDraw(False)
            
            # *stim_choice_2* updates
            if t >= 0.0 and stim_choice_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                stim_choice_2.tStart = t
                stim_choice_2.frameNStart = frameN  # exact frame index
                stim_choice_2.setAutoDraw(True)
            frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if stim_choice_2.status == STARTED and t >= frameRemains:
                stim_choice_2.setAutoDraw(False)
            
            #### EACH FRAME SNIPPET ####
            
            # show debugging stuff?
            #if debugging:
            #    show_debugging_stuff()
            
            # Get position of x and y in joystick
            joy_x, joy_y = joy.getX(), joy.getY()
            
            joy_posx_array.append(joy_x)
            joy_posy_array.append(joy_y)
            
            if len(joy_posx_array) > 2:
                joy_posx_array.pop(0)
            
            if len(joy_posy_array) > 2:
                joy_posy_array.pop(0)
            
            # check whether reward is available to collect
            # this runs only if a response is not currently being made
            # this avoids rewarding maintaining the joystick in a position
            
            if joy_posx_array not in [[1, 1], [-1,-1]] and joy_posy_array not in [[1, 1], [-1,-1]]: # pos_array not in [["left","left"], ["right","right"], ["up", "up"],["down","down"]]:
            
                if not shouldBeReinforced and tickClock.getTime() <= 0:
                    shouldBeReinforced = np.random.binomial(1, 1/int(expInfo["interval"]))
                    tickClock.reset()
            
                # assign key_resp to "up", "down", etc.
                if joy_y == -1:
                    key_resp_4.keys = "up"
                    #key_resp_4.rt = str(globalClock.getTime())
                    resp_made() 
                elif joy_y == 1:
                    key_resp_4.keys = "down"
                    #key_resp_4.rt = str(globalClock.getTime())
                    resp_made()
                elif joy_x == -1:
                    key_resp_4.keys = "left"
                    #key_resp_4.rt = str(globalClock.getTime())
                    resp_made()
                elif joy_x == 1:
                    key_resp_4.keys = "right"
                    #key_resp_4.rt = str(globalClock.getTime())
                    resp_made()
            
            
            #### END EACH FRAME SNIPPET ####
            
            
            # *curtain_img* updates
            if t >= 0.0 and curtain_img.status == NOT_STARTED:
                # keep track of start time/frame for later
                curtain_img.tStart = t
                curtain_img.frameNStart = frameN  # exact frame index
                curtain_img.setAutoDraw(True)
            frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if curtain_img.status == STARTED and t >= frameRemains:
                curtain_img.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in choice_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "choice_test"-------
        for thisComponent in choice_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "choice_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed nRepsChoice repeats of 'choice_block'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions2.xlsx', selection='0:4'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "contingency_test"-------
    t = 0
    contingency_testClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_ct = event.BuilderKeyResponse()
    stim_contingency_test.setImage(stimulus)
    # keep track of which components have finished
    contingency_testComponents = [contingency_test_instr, key_resp_ct, stim_contingency_test]
    for thisComponent in contingency_testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "contingency_test"-------
    while continueRoutine:
        # get current time
        t = contingency_testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *contingency_test_instr* updates
        if t >= 0.0 and contingency_test_instr.status == NOT_STARTED:
            # keep track of start time/frame for later
            contingency_test_instr.tStart = t
            contingency_test_instr.frameNStart = frameN  # exact frame index
            contingency_test_instr.setAutoDraw(True)
        
        # *key_resp_ct* updates
        if t >= 0.0 and key_resp_ct.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_ct.tStart = t
            key_resp_ct.frameNStart = frameN  # exact frame index
            key_resp_ct.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_ct.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_ct.status == STARTED:
            theseKeys = event.getKeys(keyList=['g', 's'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_ct.keys == []:  # then this was the first keypress
                    key_resp_ct.keys = theseKeys[0]  # just the first key pressed
                    key_resp_ct.rt = key_resp_ct.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_ct.keys == str(corrResp_ct)) or (key_resp_ct.keys == corrResp_ct):
                        key_resp_ct.corr = 1
                    else:
                        key_resp_ct.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *stim_contingency_test* updates
        if t >= 0.0 and stim_contingency_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_contingency_test.tStart = t
            stim_contingency_test.frameNStart = frameN  # exact frame index
            stim_contingency_test.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in contingency_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "contingency_test"-------
    for thisComponent in contingency_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_ct.keys in ['', [], None]:  # No response was made
        key_resp_ct.keys=None
        # was no response the correct answer?!
        if str(corrResp_ct).lower() == 'none':
           key_resp_ct.corr = 1  # correct non-response
        else:
           key_resp_ct.corr = 0  # failed to respond (incorrectly)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('key_resp_ct.keys',key_resp_ct.keys)
    trials_4.addData('key_resp_ct.corr', key_resp_ct.corr)
    if key_resp_ct.keys != None:  # we had a response
        trials_4.addData('key_resp_ct.rt', key_resp_ct.rt)
    # the Routine "contingency_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# ------Prepare to start Routine "goodbye"-------
t = 0
goodbyeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
credits_txt.setText(str((credits/100)) + ' dollars')
key_resp_12 = event.BuilderKeyResponse()

# keep track of which components have finished
goodbyeComponents = [final_txt_1, credits_txt, key_resp_12]
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "goodbye"-------
while continueRoutine:
    # get current time
    t = goodbyeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *final_txt_1* updates
    if t >= 0.0 and final_txt_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        final_txt_1.tStart = t
        final_txt_1.frameNStart = frameN  # exact frame index
        final_txt_1.setAutoDraw(True)
    
    # *credits_txt* updates
    if t >= 0.0 and credits_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        credits_txt.tStart = t
        credits_txt.frameNStart = frameN  # exact frame index
        credits_txt.setAutoDraw(True)
    frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if credits_txt.status == STARTED and t >= frameRemains:
        credits_txt.setAutoDraw(False)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['c'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye"-------
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()






payout_this_session = (nReinforcers*float(expInfo['credits_per_rnf']) - nResp*float(expInfo['cost_response']))/100.0

print("credits: %.2f")%credits

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
