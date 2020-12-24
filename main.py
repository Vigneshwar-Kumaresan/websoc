import websocket, json
import base64
import zlib
import pandas as pd
from io import StringIO
from tabulate import tabulate

def on_open(ws):
    print("opened")
    auth_data = {
        "acctid": "10099",
        "channel": "",
        "task": "cn",
        "token": "2639744535",
        "user": "10099"
    }
    ws.send(json.dumps(auth_data))

    os_data = {
        "acctid": "10099",
        "channel": "nse_cm|3045",
        "task": "os",
        "token": "2639744535",
        "user": "10099"
    }

    ws.send(json.dumps(os_data))
    #print(type(ws))
    #dfs = df.append(ws, ignore_index=True)
    #print(dfs)

def on_message(ws, message):
    print("received a message")
    encoded = message.replace(" ", "")
    data = base64.b64decode(encoded)
    decompress = zlib.decompressobj()
    decompressed_data = decompress.decompress(data)
    decompressed_data += decompress.flush()
    print(decompressed_data)
    #s = str(decompressed_data, 'utf-8')

    #data = StringIO(s)

    #df = pd.read_csv(data)
    #dataf= pd.DataFrame(df)
    #print(tabulate(dataf,headers='keys', tablefmt='grid'))
    #dfs = pd.DataFrame(decompressed_data)
    #print(dfs)

def on_close(ws):
    print("closed connection")

socket="wss://input.zebuetrade.com/NestHtml5MobileIBT/socket/stream"

ws =websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()



