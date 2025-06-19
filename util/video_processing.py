import time

def extract_audio(video_file,mocking = False):
    """
    Extracts audio from a video file.
    
    Args:
        video_file (str): Path to the video file.
        mocking (bool): If True, simulates the extraction process.
        
    Returns:
        str: Path to the extracted audio file.
    """
    if mocking:
        time.sleep(1)  # Simulate processing time
        fake_audio_path = "temp/fake_audio.mp3"
        print(f"sucessful, file location : {fake_audio_path}")
        return  fake_audio_path  
