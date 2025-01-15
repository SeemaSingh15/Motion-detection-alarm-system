# 🎥 Motion Detection Alarm System with Email Notification

This project is a Python-based motion detection system that uses your computer's webcam to detect movement and trigger an alarm with email notifications. When motion is detected, the system sounds an alarm and sends an email alert to the specified recipient.

## 📚 Libraries Used

This project utilizes several libraries to implement motion detection and notifications:

- **OpenCV** (`cv2`): For video capture and image processing capabilities.
- **Imutils** (`imutils`): Provides convenient functions for image processing.
- **Threading** (`threading`): For handling multiple operations simultaneously.
- **Winsound** (`winsound`): For generating alarm sounds on Windows systems.
- **SMTP** (`smtplib`): For sending email notifications.
- **Python Dotenv** (`python-dotenv`): To manage environment variables for email configuration.
- **Email** (`email.mime`): For creating and formatting email messages.

## 🎯 Project Overview

The main features of this motion detection system include:

- **Real-time Motion Detection**: Monitors the webcam feed for any movement.
- **Email Alerts**: Sends immediate notifications when motion is detected.
- **Alarm System**: Triggers an audible alarm on detection.
- **Low Resource Usage**: Optimized for performance with frame skipping.
- **Easy Configuration**: Uses environment variables for email settings.

## 🚀 How to Run the Application

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies

Make sure you have Python 3.6+ installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```

Alternatively, you can install the dependencies manually using pip:

```bash
pip install opencv-python
pip install imutils
pip install python-dotenv
```

### 3. Set Up Email Configuration

Create a `.env` file in the project root directory with the following variables:

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_specific_password
RECIPIENT_EMAIL=recipient_email@example.com
```

Note: For Gmail, you'll need to use an App-Specific Password. To generate one:
1. Enable 2-Step Verification in your Google Account
2. Go to Security > App Passwords
3. Generate a new app password and use it in the .env file

### 4. Run the Application

Run the script using Python:

```bash
python motion_detection.py
```

## 📖 How to Use the Application

1. **Start the System** 🚀
   - Run the script to start the webcam monitoring.

2. **Activate Alarm Mode** 🔐
   - Press 'a' to toggle alarm mode on/off.

3. **Motion Detection** 🔍
   - When motion is detected in alarm mode:
     - An audible alarm will sound
     - An email alert will be sent
     - The detection window will show the motion threshold

4. **Exit the Program** ❌
   - Press 'n' to exit the application

## 📁 Project Structure

```
motion_detection/
├── motion_detection.py    # Main application file
├── requirements.txt       # Project dependencies
├── .env                  # Environment variables
└── README.md             # Documentation
```

## ⚠️ Notes

- The system works best with good lighting conditions
- Adjust the `threshold` value in the code to fine-tune motion sensitivity
- Make sure to allow camera access when running the application
- Email notifications require an active internet connection
- The alarm sound feature is Windows-specific (uses winsound)

## 🔧 Customization

You can modify these parameters in the code:
- Frame width and height (default: 320x240)
- Frame skip rate (default: process every 5th frame)
- Motion detection threshold (default: 300)
- Alarm counter threshold (default: 20)
