import urllib.request as f
from PIL import Image
import facerecognition as faceRec
from memoryhandel import MemoryHandel


def send_to_brain(ip, text):
        f.urlopen("http://" + str(ip) + ":8888?uid=" + text).read()
        print(str(ip))


def amazon(frame):
    m = MemoryHandel('memory')

    str_num, ip = m.get_saved_values()

    fa = faceRec.FaceRecognition()
    name_id = fa.compare_img(Image.fromarray(frame))
    if name_id is None:
        num = int(str_num) + 1
        m.save_values(num, ip)
        print("-----" + str_num + "-----")
        send_to_brain(ip, str_num)
    else:
        print("Found face, (id) " + name_id)
        send_to_brain(ip, name_id)
