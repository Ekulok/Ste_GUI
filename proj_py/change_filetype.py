from PIL import Image
from pydub import AudioSegment
import os


#completed
def change(filename):
    filetype = os.path.splitext(filename)[-1].split('.')[-1]

    if filetype == "flac":
        song = AudioSegment.from_file(filename, format=filetype)
        changed_filename = os.path.splitext(filename)[0] + ".wav"
        song.export(changed_filename, format="wav")

    elif filetype == "wav":
        song = AudioSegment.from_file(filename, format=filetype)
        changed_filename = os.path.splitext(filename)[0] + ".flac"
        song.export(changed_filename, format="flac")
    elif filetype == "bmp":
        im = Image.open(filename)
        changed_filename = os.path.splitext(filename)[0] + ".png"
        im.save(changed_filename, "PNG")
    elif filetype == "png":
        im = Image.open(filename)
        changed_filename = os.path.splitext(filename)[0] + ".bmp"
        im.save(changed_filename, "BMP")