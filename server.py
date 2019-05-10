from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
from schema import Query
# from local import Query
import os

view_func = GraphQLView.as_view('graphql',
                                schema=Schema(query=Query),
                                graphiql=True)

app = Flask(__name__)
app.add_url_rule('/', view_func=view_func)

if __name__ == '__main__':
    app.run()