# Display an X

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    # Note that vertical position for the text was computed manually
    canvas.draw_text("X",[20,60], 40, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("X", 96, 96)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()

