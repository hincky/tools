from moviepy.editor import VideoFileClip
import sys
import os

def convert_mp4_to_mp3(mp4_path, mp3_path):
    try:
        video_clip = VideoFileClip(mp4_path)
        audio_clip = video_clip.audio
        
        # 简化版本，不使用进度条
        audio_clip.write_audiofile(mp3_path, logger=None, verbose=False, write_logfile=False)

        audio_clip.close()
        video_clip.close()
        print(f"转换成功: {mp3_path}")
    except Exception as e:
        print(f"转换失败: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python convert.py <输入文件.mp4> <输出文件.mp3>")
    else:
        mp4_path = sys.argv[1]
        mp3_path = sys.argv[2]
        convert_mp4_to_mp3(mp4_path, mp3_path) 