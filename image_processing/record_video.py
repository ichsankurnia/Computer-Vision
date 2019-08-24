import cv2
import datetime
from image_processing.utils import CFEVideoConf, image_resize

cap = cv2.VideoCapture(0)
save_path = 'video/video.mp4'
frames_per_seconds = 8 # 480p = 26.5  720p = 21.10  1080p = 20  4k = (GATAU) Camera logitech 720p
                           # 480p = 18.5  720p = 12  1080p =   4k = (GATAU) Camera Laptop
config = CFEVideoConf(cap, filepath=save_path, res='720p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)
finis_time = datetime.datetime.now() + datetime.timedelta(seconds=6)

while datetime.datetime.now() <= finis_time: # Record just for 6 second
# while(True):  # record untill break
    # Capture frame-by-frame
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 27: # press ESC to end record
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()