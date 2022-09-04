import PyPDF2
from art import tprint
from pathlib import Path
import pyttsx3


def convert_to_mp3(text: str, audio_file_name: str, lang='ru'):
    engine = pyttsx3.init("sapi5")
    engine.setProperty('voice', lang)
    engine.save_to_file(text, f'{audio_file_name}.mp3')
    engine.runAndWait()


def read_pdf_convert_pm3():
    done_flag = False
    while done_flag is False:
        file_direction = input('Hello, please enter direction to pdf file ')
        try:
            with open(file_direction, 'rb') as Pdf:

                pdf_reader = PyPDF2.PdfReader(Pdf)
                text = [pdf_reader.getPage(page_num).extractText() for page_num in range(pdf_reader.numPages)]
                text = ''.join(text).replace('\n', '')
                ''' Rear Pdf file and convert them to text '''
                language = input('Please enter pdf language\nFor example "en" or "ru"')
                language = language.lower()
                file_name = Path(file_direction).stem
                print('Hold on for a while we are in processing ')
                convert_to_mp3(text, file_name, language)
                done_flag = True
        except FileNotFoundError:
            print('File not found! Please try again')
        else:
            tprint('Success', 'random')
            print('File saved')


if __name__ == '__main__':
    read_pdf_convert_pm3
