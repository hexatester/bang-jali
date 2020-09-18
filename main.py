from jali import jali
from dotenv import load_dotenv
load_dotenv()

jali.start()
jali.run_until_disconnected()
