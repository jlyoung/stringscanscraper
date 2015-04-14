from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from stringscanscraper import contains_match

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


# Matches
#   shows which urls from the list contain the search term
class Matches(Resource):
    def post(self):
        parser.add_argument('searchterm', type=str, required=True,
                            help="Search term is required!")
        parser.add_argument('urls', type=str, action='append', required=True,
                            help="Atleast one url to scan is required!")
        args = parser.parse_args()
        matches = []
        searchterm = args['searchterm']
        for url in args['urls']:
            if contains_match(args['searchterm'], url):
                matches.append(url)
        result = {  'searchterm': searchterm,
                    'matches': matches }
        return result

##
## Actually setup the Api resource routing here
##
api.add_resource(Matches, '/matches')


if __name__ == '__main__':
    app.run(debug=True)