import requests
import bonobo
from bonobo.config import use_context_processor

FABLABS_API_URL = 'https://public-us.opendatasoft.com/api/records/1.0/search/?dataset=fablabs&rows=1000'

def extract_fablabs():
    yield from requests.get(FABLABS_API_URL).json().get('records')

def with_opened_file(self, context):
    with open('output.txt', 'w+') as f:
        yield f

@use_context_processor(with_opened_file)
def write_repr_to_file(f, *row):
    f.write(repr(row) + "\n")

def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(
        extract_fablabs,
        bonobo.Limit(10),
        write_repr_to_file,
    )
    return graph

# The __main__ block actually execute the graph.
if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),

        )
