# graphql_spotify_d3f
Wrap Spotify API data (for "Drei Fragezeichen") with GraphQL.

# Overview
My project consists of the following components:

Backend
- Spotify API (Spotipy): <https://developer.spotify.com/documentation/web-api/reference-beta/>
- GraphQL (Graphene)
- Flask and FlaskGraphQL

I’ll show how to define schema and transform JSON into GraphQL models.

# Usage
To save Spotify API output as a json file:
```
python save_api_results.py
```

To run the whole application
```
python server.py
```

In the result we see the following GraphiQL interface. Works.
![https://github.com/M9T/D3F/blob/master/graphiql.jpg](https://github.com/M9T/D3F/blob/master/graphiql.jpg)
