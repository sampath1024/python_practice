from pypdf import PdfReader
from gtts import gTTS
reader=PdfReader("D:\PDF\Akash.Chawla.Resume.pdf") # takes the pdf input
page=reader.pages[0]   # it will print take the first page 0 means first page
print(page.extract_text()) # it will extract only text,ignores images etc
text=page.extract_text()
tts=gTTS(text,lang="en")
tts.save("page1.mp3")




