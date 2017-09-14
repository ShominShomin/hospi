import uuid
import datetime

def callNum():
   str1 = datetime.datetime.now().strftime ("%Y%m%d")
   str2 = initial=uuid.uuid4().hex[:3].upper()
   return str1 + str2