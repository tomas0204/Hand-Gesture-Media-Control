# Hand Gesture Volume Control

This project uses a webcam to detect hand gestures and control the system volume and media playback based on the gestures.

## Requirements

- Python 3.6+
- A webcam

## Setup

1. **Clone the repository:**

    ```sh
    git clone <URL_of_your_repository>
    cd <repository_name>
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

1. **Ensure your webcam is connected.**

2. **Run the main script:**

    ```sh
    python main.py
    ```

## How it Works

- **Open Hand:** Increases the system volume.
- **Closed Hand:** Decreases the system volume.
- **Two Open Hands:** Pauses or resumes the music if both hands are detected open for more than 3 seconds.

## Files

- `main.py`: The main script to run the hand gesture detection and control.
- `functions.py`: Contains functions to manage volume control and hand gesture recognition.
- `requirements.txt`: Lists all the dependencies required to run this project.

## Troubleshooting

- If you encounter any issues with the webcam or dependencies, ensure all required packages are installed correctly and that your webcam is properly connected.
- Make sure to activate your virtual environment each time you start a new terminal session before running the script.

## License

This project is licensed under the MIT License.
