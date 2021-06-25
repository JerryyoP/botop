from os import getenv
from dotenv import load_dotenv

load_dotenv()

STRING = getenv("STRING")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
STRING4 = getenv("STRING4")
STRING5 = getenv("STRING5")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BIO_MESSAGE = getenv("BIO")
SUDO = list(map(int, getenv("SUDO").split()))
