## Usar archivos .env en Python

Una manera de usar los archivos .env en Python es haciendo uso de la la librería python-dotenv.
```
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
```