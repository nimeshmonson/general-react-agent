from tavily import TavilyClient
import os

class TavilySearchClient:
    def __init__(self, api_key):
        self.client = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))

    def search_internet(self, search_query):
        print("Searched Tavily: {}".format(search_query))
        return self.client.get_search_context(search_query)