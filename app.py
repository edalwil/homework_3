from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route('/numeros_estudiante')
def index():
    url = "https://docs.google.com/spreadsheets/d/1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU/export?format=csv&id=1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU&gid=135007174"

    df = pd.read_csv(url)
    return {"numeros de estudiante": len(df)}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)
