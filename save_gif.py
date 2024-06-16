from PIL import Image
import glob
import os
# Paths to the JPG images (assuming they are named sequentially)
folder_path = 'output'
image_paths = sorted(
    [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.startswith('frame_') and f.endswith('.jpg')],
    key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[1])
)

# List to hold the image frames
frames = []

# Load each image and append to the frames list
for image_path in image_paths:
    img = Image.open(image_path)
    frames.append(img)

# Save the frames as a GIF
output_path = 'output.gif'
frames[0].save(output_path, format='GIF', append_images=frames[1:], save_all=True, duration=500, loop=0)

print(f'GIF saved at: {output_path}')
