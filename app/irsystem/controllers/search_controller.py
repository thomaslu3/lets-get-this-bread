from . import *
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder
from app.irsystem.models.search import *


project_name = "Let's Get This Bread"
net_id = "Lindsey Luo: lgl47, Thomas Lu: tlu398, Michelle Loven: ml2359, Peter Munn: pcm82"


@irsystem.route('/', methods=['GET'])
def search():
    query = request.args.get('search')
    if not query:
        data = []
    else:
<<<<<<< HEAD
        data = top_k(query, 100)
        if data == "No results found":
            # TODO: insert operation for when we dont have any results found
            return render_template('search.html', name=project_name, netid=net_id, query=query, data="")
=======
        if top_k(query, 100) == "No results found":
            data = []
>>>>>>> 276013cad1e610da493463a8d8225d257491eff9
        else:
            data = top_k(query, 10)
    return render_template('search.html', name=project_name, netid=net_id, query=query, data=data)
