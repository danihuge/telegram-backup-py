import os
import datetime
from pyrogram import Client, Filters

_session_name = "xxxxxxxxxx"
_api_id = 1234
_api_hash = "xxxxxxxx"
_backup_chat_id = "xxxxxxxxxx"

script_path = os.path.dirname(os.path.abspath( __file__ ))

app = Client(
    session_name=_session_name,
    api_id=_api_id,
    api_hash=_api_hash
)

@app.on_message(Filters.chat("origin_chat_channel"))
def from_pyrogramchat(client, message):

    app.send_message(_backup_chat_id, message.text)

    file_name = '{date:%Y%m%d-%H%M%S}.txt'.format( date=datetime.datetime.now() )
    file = open(script_path+'/files/'+file_name, "w")
    file.write(message.text)
    file.close()

app.start()
app.idle()