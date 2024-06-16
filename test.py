from PIL import Image
import os

# Open the GIF file
gif_path = '20170410090643735.gif'
gif = Image.open(gif_path)

# Create a directory to save the frames
frames_dir = 'gif_frames'
os.makedirs(frames_dir, exist_ok=True)

# Loop through each frame in the GIF and save it as a separate image
frame_number = 0
while True:
    # Save the current frame
    frame_path = os.path.join(frames_dir, f'frame_{frame_number}.png')
    gif.save(frame_path, 'PNG')
    
    # Move to the next frame
    frame_number += 1
    try:
        gif.seek(frame_number)
    except EOFError:
        break  # End of GIF

print(f'Frames saved in directory: {frames_dir}')
