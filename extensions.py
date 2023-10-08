import observer
import os

from dotenv import load_dotenv

load_dotenv()

files = os.listdir(os.getenv('PATH'))
filename = files[0]

print(filename)