import threading
import winsound
import cv2
import imutils
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the email details from environment variables
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Set up the video capture with lower resolution
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Lower width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # Lower height

# Initialize the starting frame for motion detection
_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=320)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

# Initialize variables
alarm = False
alarm_mode = False
alarm_counter = 0

# Email function
def send_email():
    subject = "ALERT: Motion Detected!"
    body = "Motion was detected, and the alarm has been triggered!"

    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)  # Use the new App Password here
            server.sendmail(EMAIL_USER, RECIPIENT_EMAIL, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Beep alarm function
def beep_alarm():
    global alarm
    while alarm_mode:  # Keep beeping as long as alarm mode is active
        print("ALARM")
        winsound.Beep(2500, 1000)
    alarm = False

# Video capture function running in a separate thread
def capture_video():
    global frame
    while True:
        _, frame = cap.read()

# Run video capture in a separate thread
thread = threading.Thread(target=capture_video)
thread.daemon = True  # Make sure the thread exits when the main program exits
thread.start()

frame_count = 0
frame_skip = 5  # Process every 5th frame

# Main loop
while True:
    frame_count += 1
    if frame_count % frame_skip == 0:
        frame_resized = imutils.resize(frame, width=320)

        if alarm_mode:
            frame_bw = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
            frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)
            difference = cv2.absdiff(frame_bw, start_frame)
            threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
            start_frame = frame_bw

            if threshold.sum() > 300:  # Adjust threshold value as needed
                alarm_counter += 1
            else:
                if alarm_counter > 0:
                    alarm_counter -= 1

            cv2.imshow("CAM", threshold)
        else:
            cv2.imshow("CAM", frame_resized)

        if alarm_counter > 20:
            if not alarm:
                alarm = True
                threading.Thread(target=beep_alarm).start()
                send_email()  # Send the email when the alarm is triggered

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("a"):
        alarm_mode = not alarm_mode
    if key_pressed == ord("n"):
        alarm_mode = False
        break

cap.release()
cv2.destroyAllWindows()
