import sentry_sdk

from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration
#SENTRY_URL ='https://f9b1070564e247e58554d7a7406e0ecd@o485365.ingest.sentry.io/5540631'
sentry_sdk.init(
    dsn=os.envior.get("https://f9b1070564e247e58554d7a7406e0ecd@o485365.ingest.sentry.io/5540631"),
    integrations=[BottleIntegration()]
)
app = Bottle()
@app.route('/success')
def succes():
    return

@app.route('/fail')
def fail():
    raise RuntimeError('There are error!')
    return

app.run(host='localhost', port=8080)