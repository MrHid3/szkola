import  sys, os, time

def animgif_to_ASCII_animation(animated_gif_path):
    # map greyscale to characters
    chars = ('#', '#', '@', '%', '=', '+', '*', ':', '-', '.', ' ')
    clear_console = 'clear' if os.name == 'posix' else 'CLS'

    # load image
    anim = image.load_animation(animated_gif_path)

    # Step through forever, frame by frame
    while True:
        for frame in anim.frames:

            # Gets a list of luminance ('L') values of the current frame
            data = frame.image.get_data('L', frame.image.width)

            # Built up the string, by translating luminance values to characters
            outstr = ''
            for (i, pixel) in enumerate(data):
                outstr += chars[(ord(pixel) * (len(chars) - 1)) / 255] + \
                          ('\n' if (i + 1) % frame.image.width == 0 else '')

            # Clear the console
            os.system(clear_console)

            # Write the current frame on stdout and sleep
            sys.stdout.write(outstr)
            sys.stdout.flush()
            time.sleep(0.1)

# run the animation based on some animated gif
animgif_to_ASCII_animation(u'rickroll-roll.gif')