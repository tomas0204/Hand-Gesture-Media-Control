from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui
import mediapipe as mp

# Features to control volume
def set_volume(volume):
    """
    Sets the system volume to a specified scalar value.

    Args:
        volume (float): The volume level to set (between 0.0 and 1.0).

    Returns:
        None
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_control = cast(interface, POINTER(IAudioEndpointVolume))
    volume_control.SetMasterVolumeLevelScalar(volume, None)

def increase_volume():
    """
    Increases the system volume by 0.1 if the current volume is less than 1.0.

    Returns:
        None
    """
    current_volume = get_volume()
    if current_volume < 1.0:
        set_volume(min(current_volume + 0.1, 1.0))

def decrease_volume():
    """
    Decreases the system volume by 0.1 if the current volume is greater than 0.0.

    Returns:
        None
    """
    current_volume = get_volume()
    if current_volume > 0.0:
        set_volume(max(current_volume - 0.1, 0.0))

def get_volume():
    """
    Retrieves the current system volume level as a scalar value between 0.0 and 1.0.

    Returns:
        float: The current system volume level.
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_control = cast(interface, POINTER(IAudioEndpointVolume))
    return volume_control.GetMasterVolumeLevelScalar()


# Initialize MediaPipe Hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def is_hand_open(hand_landmarks):
    """
    Determines if a hand is considered open based on landmark positions.

    Args:
        hand_landmarks (mediapipe.HandLandmark): A mediapipe HandLandmark object containing hand landmarks.

    Returns:
        bool: True if the hand is open (all fingertip landmarks are above their respective pip landmarks), False otherwise.
    """
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    if (index_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
        middle_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
        ring_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and
        pinky_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y):
        return True
    return False
