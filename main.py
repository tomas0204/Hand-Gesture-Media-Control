import cv2
from functions import *
import time

# Video capture
cap = cv2.VideoCapture(0)
paused = False

open_hands_start_time = None
open_hands_duration = 0

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    open_hands_count = 0
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if is_hand_open(hand_landmarks):
                open_hands_count += 1
                print("Open hand detected")
            else:
                print("Closed hand detected")

        
        if open_hands_count == 2:
            if open_hands_start_time is None:
                open_hands_start_time = time.time()
            else:
                open_hands_duration = time.time() - open_hands_start_time

            if open_hands_duration > 2:
                print("Two open hands detected for more than 3 seconds - Pausing/Resuming music")
                pyautogui.press('playpause')
                open_hands_start_time = None  # Reset timer after action
                open_hands_duration = 0
        else:
            open_hands_start_time = None
            open_hands_duration = 0

        if open_hands_count == 1:
            print("One open hand - Adjusting volume")
            increase_volume()
        elif open_hands_count == 0:
            print("No open hands - Lowering volume")
            decrease_volume()
    else:
        print("No hands detected")
        open_hands_start_time = None
        open_hands_duration = 0

    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
