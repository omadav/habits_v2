#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on August 08, 2018, at 15:05
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
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
expName = 'habits_2'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'01', u'interval': u'10', u'schedule': u'RI'}
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
    originPath=u'C:\\Users\\omada\\Dropbox\\Projects\\Caltech\\Humans\\Habits\\Caltech 2018-2 (Anastasia)\\Task\\habits_2_previous.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
    text=u'\nIn this experiment, you will be using your joystick to earn either gold or silver coins which correspond to credits that can be cashed in for real money at the end of the experiment. \n\nEach coin is worth exactly the same dollar amount of 0.25 dollars. Each of the coins you earn during the experiment will be deposited into one of two piggy banks: one for gold coins and the other for silver coins.\n\n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font=u'Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instr1_1"
instr1_1Clock = core.Clock()
instr1_1_txt = visual.TextStim(win=win, name='instr1_1_txt',
    text=u'During each trial, you will be allowed to perform one of four actions with the joystick: move left, move right, push and pull. Each allowed movement comes at a cost of 0.01 dollars.\n\nYou will know which action is the correct one by a stimulus that will appear on the screen. An incorrect action will have no effect. \n\nThe following screens will present the stimuli and the correct action you need to take when you see each stimulus.\n\n\n\n\n\n\n\n(Press any key to continue)',
    font=u'Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instr_stim1"
instr_stim1Clock = core.Clock()
instr_stim1_txt = visual.TextStim(win=win, name='instr_stim1_txt',
    text=u'Below is one of the stimuli you will see.\n\nThis stimuli is a cube that has a button on the left side, so the correct response is to push the button by moving the joystick to the right, as shown in the picture to the right of the cube. \n\nFeel free to try it! \n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font=u'Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
resp_right_img = visual.ImageStim(
    win=win, name='resp_right_img',
    image=u'stim/right_resp_img.png', mask=None,
    ori=0, pos=(-0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
joy_right_img = visual.ImageStim(
    win=win, name='joy_right_img',
    image=u'stim/joy_img_right.jpg', mask=None,
    ori=0, pos=(0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_stim2"
instr_stim2Clock = core.Clock()
instr_stim2_txt = visual.TextStim(win=win, name='instr_stim2_txt',
    text=u'Here is another one of the stimuli you will see.\n\nThis cube has a button on the top, so the correct response is to push the button by pulling the joystick towards you, as shown in the picture to the right of the cube. Feel free to try it!\n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font=u'Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
resp_down_img = visual.ImageStim(
    win=win, name='resp_down_img',
    image=u'stim/down_resp_img.png', mask=None,
    ori=0, pos=(-0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
joy_down_img = visual.ImageStim(
    win=win, name='joy_down_img',
    image=u'stim/joy_img_down.jpg', mask=None,
    ori=0, pos=(0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_stim3"
instr_stim3Clock = core.Clock()
instr_stim3_txt = visual.TextStim(win=win, name='instr_stim3_txt',
    text=u'\nHere is another one of the stimuli you will see.\n\nThis cube has a button on the front, so the correct response is to push the button by pushing the joystick away from you, as shown in the picture to the right of the cube. Feel free to try it!\n\n\n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font=u'Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
resp_up_img = visual.ImageStim(
    win=win, name='resp_up_img',
    image=u'stim/up_resp_img.png', mask=None,
    ori=0, pos=(-0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
joy_up_img = visual.ImageStim(
    win=win, name='joy_up_img',
    image=u'stim/joy_img_up.jpg', mask=None,
    ori=0, pos=(0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_stim4"
instr_stim4Clock = core.Clock()
instr_stim4_txt = visual.TextStim(win=win, name='instr_stim4_txt',
    text=u'Here is another one of the stimuli you will see.\n\nThis cube has a button on the right side, so the correct response is to push the button by moving the joystick to the left, as shown in the picture to the right of the cube. Feel free to try it!\n\n\n\n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font=u'Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
resp_left_image = visual.ImageStim(
    win=win, name='resp_left_image',
    image=u'stim/left_resp_img.png', mask=None,
    ori=0, pos=(-0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
joy_left_img = visual.ImageStim(
    win=win, name='joy_left_img',
    image=u'stim/joy_img_left.jpg', mask=None,
    ori=0, pos=(0.2, -0.2), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr2_3"
instr2_3Clock = core.Clock()
instr2_3_txt = visual.TextStim(win=win, name='instr2_3_txt',
    text=u'Every time you perform the action that corresponds to the stimulus shown on the screen, a triangle will appear at the center of the screen signalling that the relevant response has been made. \n\nYou may receive a reward for performing the action which corresponds to the stimulus shown on the screen. This will be in the form of either a gold or silver coin, which will appear at the top of the screen when the reward is earned. Your credits will increase proportionally, and the coin will be added to your respective piggy bank. \n\nTwo of the actions will give you gold coins when you are rewarded; the other two will give you silver coins. \n\n\n\n\n\n\n\n(Press any key to continue)\n',
    font=u'Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "training"
trainingClock = core.Clock()
circle_resp = visual.ShapeStim(
    win=win, name='circle_resp',
    vertices=[[-(0.2, 0.2)[0]/2.0,-(0.2, 0.2)[1]/2.0], [+(0.2, 0.2)[0]/2.0,-(0.2, 0.2)[1]/2.0], [0,(0.2, 0.2)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=2, lineColor=[1.000,0.004,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,0.004,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
stim = visual.ImageStim(
    win=win, name='stim',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stim_pressed = visual.ImageStim(
    win=win, name='stim_pressed',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

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
begin_trial = sound.Sound('sounds/begin_trial.wav')
exp_finished = sound.Sound('sounds/exp_finished.wav')

# Initialise some variables

# Should we show the debugging msgs on screen?
debugging = True

# Initialise credits
credits = 20.00

nReinforcers = 0

# create array to save last two frames for joystick position
joy_posx_array, joy_posy_array = [], []
window = 2 # maximum length of array (2 if you want 2 frames, for ex)

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
    ''' Once a response has been recorded,
    this function checks whether a response is reinforced
    and gives the reward '''
    global credits, shouldBeReinforced, nReinforcers # globals because these are used outside
    
    if shouldBeReinforced:
        nReinforcers += 1
        reward_sound.play()
        for frameN in range(30): # show for half a sec
            #reward_txt.draw()
            circle_resp.setOpacity(0)
            coin.setOpacity(1)
            credits += 0.25
            win.flip()
    trials.addData("wasRnf", shouldBeReinforced)
    thisExp.nextEntry()
    shouldBeReinforced = 0 # reset shouldBeReinforced flag


def resp_made():
    global credits
    ''' after a resp is made, save it in the csv file and show circle '''
    if phase == "training":
        if key_resp_2.keys in ["left", "right"]: # this updates the 2-element array with joy_x pos
            joy_posx_array.pop(0)
            joy_posx_array.append(joy_x)
            # save data in csv 
            trials.addData("response", key_resp_2.keys)
            trials.addData("t", str(globalClock.getTime()))

        elif key_resp_2.keys in ["up", "down"]: # this updates the 2-element array with joy_y pos
            joy_posx_array.pop(0)
            joy_posx_array.pop(0)
            joy_posx_array.append(joy_y)
            trials.addData("response", key_resp_2.keys)
            trials.addData("t", str(globalClock.getTime()))

    elif phase == "choice":
        if key_resp_4.keys in ["left", "right"]: # this updates the 2-element array with joy_x pos
            joy_posx_array.pop(0)
            joy_posx_array.append(joy_x)
            # save data in csv 
            trials.addData("response", key_resp_4.keys)
            trials.addData("t", str(globalClock.getTime()))

        elif key_resp_4.keys in ["up", "down"]: # this updates the 2-element array with joy_y pos
            joy_posx_array.pop(0)
            joy_posx_array.pop(0)
            joy_posx_array.append(joy_y)
            trials.addData("response", key_resp_4.keys)
            trials.addData("t", str(globalClock.getTime()))
        thisExp.nextEntry()
        
    
    if phase == "training":
        if key_resp_2.keys in [corrResp]:
            credits -= 0.01
            coin_sound.play()
            #print("correct resp")
            for nframes in range(3):
                circle_resp.setOpacity(1)

                #stim_pressed.setOpacity(1)
            checkRnf() # call checkRnf function to see whether it's reinforced
    elif phase == "choice":
        if key_resp_4.keys in [corrResp1, corrResp2]:
            credits -= 0.01
            coin_sound.play()
            #print("correct resp")
            for nframes in range(3):
                circle_resp_choice.setOpacity(1)
                #stim_pressed.setOpacity(1)
            #checkRnf()

#### END BEGIN EXPERIMENT SNIPPET ####

coin = visual.ImageStim(
    win=win, name='coin',
    image='sin', mask=None,
    ori=0, pos=(0, 0.85), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "instr_test"
instr_testClock = core.Clock()
instr_devaluation_txt = visual.TextStim(win=win, name='instr_devaluation_txt',
    text='One of the piggy banks is now full.\n\nPlease call the experimenter.',
    font='Comic Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

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
    image=u'stim/curtain.jpg', mask=None,
    ori=0, pos=(0, 0.85), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

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
instr2_3Components = [instr2_3_txt, key_resp_10]
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

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx', selection='0:4'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "training"-------
    t = 0
    trainingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()
    stim.setPos(position)
    stim.setImage(stimulus)
    stim_pressed.setPos(position)
    stim_pressed.setImage(stimulus_pressed)
    # Initialise parameters at the beginning of each block (routine)
    phase = "training"
    
    shouldBeReinforced = 0 # flag to set next reinforcer for RI schedule
    
    tickClock = core.CountdownTimer(1) # this is to tick every second for reward availability
    
    
    coin.setImage(coin_img)
    # keep track of which components have finished
    trainingComponents = [key_resp_2, circle_resp, stim, stim_pressed, coin]
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
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
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
                key_resp_2.keys.extend(theseKeys)  # storing all keys
                key_resp_2.rt.append(key_resp_2.clock.getTime())
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
        
        # *stim_pressed* updates
        if t >= 0.0 and stim_pressed.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_pressed.tStart = t
            stim_pressed.frameNStart = frameN  # exact frame index
            stim_pressed.setAutoDraw(True)
        frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if stim_pressed.status == STARTED and t >= frameRemains:
            stim_pressed.setAutoDraw(False)
        if stim_pressed.status == STARTED:  # only update if drawing
            stim_pressed.setOpacity(0, log=False)
        
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
                resp_made() 
            elif joy_y == 1:
                key_resp_2.keys = "down"
                resp_made()
            elif joy_x == -1:
                key_resp_2.keys = "left"
                resp_made()
            elif joy_x == 1:
                key_resp_2.keys = "right"
                resp_made()
        
        
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
            coin.setOpacity(0, log=False)
        
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
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    
    # the Routine "training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instr_test"-------
t = 0
instr_testClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
instr_testComponents = [instr_devaluation_txt, key_resp_5]
for thisComponent in instr_testComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_test"-------
while continueRoutine:
    # get current time
    t = instr_testClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_devaluation_txt* updates
    if t >= 0.0 and instr_devaluation_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_devaluation_txt.tStart = t
        instr_devaluation_txt.frameNStart = frameN  # exact frame index
        instr_devaluation_txt.setAutoDraw(True)
    
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
    for thisComponent in instr_testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_test"-------
for thisComponent in instr_testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "instr_test" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx', selection='4:6'),
    seed=None, name='test')
thisExp.addLoop(test)  # add the loop to the experiment
thisTest = test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
if thisTest != None:
    for paramName in thisTest.keys():
        exec(paramName + '= thisTest.' + paramName)

for thisTest in test:
    currentLoop = test
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest.keys():
            exec(paramName + '= thisTest.' + paramName)
    
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
        frameRemains = 0.0 + duration- win.monitorFramePeriod * 0.75  # most of one frame period left
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
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
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
                key_resp_4.keys.extend(theseKeys)  # storing all keys
                key_resp_4.rt.append(key_resp_4.clock.getTime())
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
                key_resp_4.keys = "up"
                resp_made() 
            elif joy_y == 1:
                key_resp_4.keys = "down"
                resp_made()
            elif joy_x == -1:
                key_resp_4.keys = "left"
                resp_made()
            elif joy_x == 1:
                key_resp_4.keys = "right"
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
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys=None
    test.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        test.addData('key_resp_4.rt', key_resp_4.rt)
    
    # the Routine "choice_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'test'

# get names of stimulus parameters
if test.trialList in ([], [None], None):
    params = []
else:
    params = test.trialList[0].keys()
# save data for this loop
test.saveAsExcel(filename + '.xlsx', sheetName='test',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
test.saveAsText(filename + 'test.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
