import cv2
import os

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_name = f"{os.path.basename(video_path).split('.')[0]}_{count}.jpg"
        cv2.imwrite(os.path.join(output_folder, frame_name), frame)
        count += 1
    
    cap.release()