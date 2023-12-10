import PyPDF2
from gtts import gTTS

path = open('dummy.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(path)

text = ""

for page_num in range(len(pdfReader.pages)):
    page = pdfReader.pages[page_num].extract_text()
    text += page.strip().replace("\n", " ").replace(" ' ", "'")

print("Converting PDF to MP3...")
tts = gTTS(text=text, lang='en', slow=False)
tts.save("output.mp3")
