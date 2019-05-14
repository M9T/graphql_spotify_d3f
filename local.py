'''
Mini test scenario: This local.py file shows the idea behind graphql.
'''

import graphene
import json


class Artist(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(graphene.ObjectType):

    artist = graphene.List(Artist, first=graphene.Int())

    def resolve_artist(self, info, first):
        return [
            Artist(123, 'Mark'),
            Artist(234, 'Mark2'),
            Artist(345, 'Mark3')
        ][:first]


schema = graphene.Schema(query=Query)
query = """
    {
      artist(first: 1){
        id
        name
      }
    }
"""

if __name__ == "__main__":
    result = schema.execute(query)
    items = dict(result.data.items())
    print(json.dumps(items, indent=4))