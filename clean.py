import os 
import shutil
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

main_dir = "/Users/YOUR_USERNAME/Downloads"
pic_dir = "/Users/YOUR_USERNAME/Desktop/Downloaded Images"
video_dir = "/Users/YOUR_USERNAME/Desktop/Downloaded Videos"
doc_dir = "/Users/YOUR_USERNAME/Desktop/Downloaded Documents"
unknown_dir = "/Users/YOUR_USERNAME/Desktop/Unknown Download"

image_formats = [".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff", ".tif", ".svg", ".ico", ".heic"]
video_formats = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".3gp"]
document_formats = [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".txt", ".csv", ".rtf", ".odt"]

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        with os.scandir(main_dir) as entries:
            for i in entries:
                if i.name == ".DS_Store":
                    continue
                elif i.name.lower().endswith(tuple(image_formats)):
                   shutil.move(i, pic_dir)
                elif i.name.lower().endswith(tuple(video_formats)):
                    shutil.move(i, video_dir)
                elif i.name.lower().endswith(tuple(document_formats)):
                    shutil.move(i, doc_dir)
                else:
                    shutil.move(i, unknown_dir)
                
if __name__ == "__main__":
    path = main_dir
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
