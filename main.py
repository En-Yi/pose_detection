from ultralytics import YOLO
import cv2
from PIL import Image, ImageDraw, ImageFont

# Load a model
model = YOLO("yolov8n-pose.pt")  # load an official model
# Predict with the model
# results = model("5f508c4e783a1.jpg")  # predict on an image
for i in range(0,14):

    results = model.predict("gif_frames/frame_" + str(i) + ".png", conf=0.5)
    keypoints = results[0].keypoints
    if len(keypoints.xy) > 0:
        image = Image.open('runs/pose/predict4/frame_' + str(i) + ".png")
                
        for kpt in keypoints.xy:
            print(kpt)
            print(len(kpt))
            if len(kpt) > 0:
                if (kpt[11][1] - kpt[5][1])*2 > (kpt[15][1] - kpt[5][1]) or (kpt[9][1] - kpt[5][1])*2 > (kpt[15][1] - kpt[5][1]):
                    # Initialize ImageDraw
                    draw = ImageDraw.Draw(image)
                    text = "人員跌倒"  # Replace with your desired text
                    font_path = "kaiu.ttf"  # Path to a .ttf font file
                    font_size = 36  # Font size
                    font = ImageFont.truetype(font_path, font_size)

                    # Define the position for the text (top-left corner)
                    position = (10, 10)  # Adjust as needed
                    # Measure the size of the text to create a background rectangle
                    text_bbox = draw.textbbox(position, text, font=font)
                    background_rect = (text_bbox[0] - 5, text_bbox[1] - 5, text_bbox[2] + 5, text_bbox[3] + 5)

                    # Define colors
                    background_color = (0, 0, 0)  # Black background
                    text_color = (255, 255, 255)  # White text

                    # Draw the background rectangle
                    draw.rectangle(background_rect, fill=background_color)

                    # Add text to image
                    draw.text(position, text, font=font, fill=text_color)
                    # Save the modified image
                output_path = 'output/frame_' + str(i) + ".jpg"  # Replace with your desired output path
                image.save(output_path)
            else:
                output_path = 'output/frame_' + str(i) + ".jpg"  # Replace with your desired output path
                image.save(output_path)
            # x, y = int(kpt[0]), int(kpt[1])
        

# cv2.imshow("Keypoints without lines", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()