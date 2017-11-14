from six.moves import urllib as f
from PIL import Image
import facerecognition as faceRec
from memoryhandel import MemoryHandel


def send_to_brain(ip, text):
    try:
        data = f.urlencode({"text": text}).encode()
        req = f.Request("http://" + str(ip) + ":8080/robologic/see", data=data)
        req.urlopen(req)
    except:
        print("Could not connect to brain.")


def amazon(frame):
    m = MemoryHandel('memory')

    str_num, ip = m.get_saved_values()

    f = faceRec.FaceRecognition()
    name_id = f.compare_img(Image.fromarray(frame))
    if name_id is None:
        num = int(str_num) + 1
        m.save_values(num, ip)
        print("-----" + str_num + "-----")
        f.upload_img(Image.fromarray(frame), str_num)
        send_to_brain(ip, str_num)
    else:
        print("Found face, (id) " + name_id)
        send_to_brain(ip, name_id)