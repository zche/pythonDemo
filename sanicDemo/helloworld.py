from sanic import Sanic
from sanic.response import text


class RasaNLU(object):
    """Class representing Rasa NLU http server"""

    def __init__(self):
        super().__init__()

    app = Sanic()

    @app.route("/")
    async def test(self,request):
        return text('Hello World!')


    @app.route("/parse", methods=['GET', 'POST', 'OPTIONS'])
    async def test(request):
        return text(request.args)


if __name__ == "__main__":
    rasa = RasaNLU()
    rasa.app.run(host="0.0.0.0", port=8000)