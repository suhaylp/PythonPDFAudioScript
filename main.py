import pypdf
from gtts import gTTS


def read_pdf(addr2pdf):
    pdffileobject = open(addr2pdf, 'rb')
    pdfreader = pypdf.PdfReader(pdffileobject)
    num_pages = len(pdfreader.pages)
    all_pages = ' '

    for p in range(num_pages):
        page_obj = pdfreader.pages[p]
        text = page_obj.extract_text()
        all_pages += text

    pdffileobject.close()
    return all_pages

def conv_text2speech(text2cov):
    audio = gTTS(text=text2cov,lang="en", slow=False)
    audio.save("output.mp3")

if __name__ == '__main__':
    pdf_content = read_pdf("dummy.pdf")
    conv_text2speech(pdf_content)

    # influenced by https://www.youtube.com/watch?v=cardL-Ydy34&ab_channel=TheCodingBuddiesGuild