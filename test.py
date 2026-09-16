from tools.tavily_tool import tavily_search

from tools.flight_tool import search_flights

# res= tavily_search("Best hotels in Paris")
# print(res)

res = search_flights("plan a 2 weeks slovenia trip from Lagos, Nigeria")
print(res)