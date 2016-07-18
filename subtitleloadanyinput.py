import pycaption
from pycaption import detect_format
from pycaption import SRTWriter
from pycaption import WebVTTReader
import io


# Convert from WebVTT to SRT
# Pass the input file location as the argument to the function
def Subtitleload(inputfile):
    wttcaps=io.open(inputfile,"r",encoding='utf-8').read()
    converter = pycaption.CaptionConverter()
    #Captionset object as intermediary
    reader = pycaption.detect_format(wttcaps)
    converter.read(wttcaps,reader())
    srtcaps = io.open('youroutputfiledirectorygoeshere.srt', "w", encoding='utf-8')
    #Write converter object into srtcaps file
    srtcaps.write(converter.write(SRTWriter()))




