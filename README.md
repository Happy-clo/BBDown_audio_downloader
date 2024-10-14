# Bilibili Video Downloader

## Overview

This application allows you to download audio from Bilibili videos. You can input multiple video links, specify audio quality preferences, and set a download path for the files. The tool uses **BBDown** for downloading and **ffmpeg** for processing.

## Features

- Download audio from multiple Bilibili video links at once.
- Specify audio quality preferences.
- Set a custom download path.
- Real-time output during the download process.

## Requirements

1. **Python 3.x** - Make sure you have Python installed.
2. **Gradio** - For the web interface.
3. **BBDown** - A command-line tool for downloading Bilibili videos. Ensure it's installed and available in your system's PATH.
4. **FFmpeg** - A multimedia framework for handling audio and video files. Make sure you have the correct path specified in the script.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Happy-clo/BBDown_audio_downloader.git <repository-directory>
   cd <repository-directory>
   ```
2. Install the required Python packages:

   ```bash
   pip install gradio
   ```

3. Ensure **BBDown** and **ffmpeg** are installed. Update the `download_audio` function in the `app.py` file with the correct paths if necessary.

## Usage

1. Fill in your own ffmpeg address into the code then run the application:

   ```bash
   python app.py
   ```

2. Open the provided link in your web browser.

3. Fill in the following fields:

   - **Bilibili 视频链接**: Input video links (one per line).
   - **音频质量优先级**: Specify your preferred quality for the audio (e.g., `1080P 高码率, 720P 高码率`).
   - **下载路径**: Specify where you want the audio files to be saved (e.g., `E:\AudioDownloads`).

4. Click "Submit" to start downloading. You will see real-time output and status messages during the process.

## Output

- The application will provide success or error messages for each video link processed.
- All downloaded audio files will be saved to the specified download path.

## Troubleshooting

- If you see "找不到 BBDown 或 ffmpeg 工具," ensure that both tools are properly installed and their paths are correctly configured in the script.
- If you encounter any unknown errors, the application will display an appropriate error message.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements!

## Contact

For inquiries, please contact [your email or contact information here].