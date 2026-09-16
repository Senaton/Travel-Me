from tools.tavily_tool import tavily_search

from tools.flight_tool import search_flights
from backend import run_travel_agent

# res= tavily_search("Best hotels in Paris")
# print(res)

# res = search_flights("plan a 2 weeks slovenia trip from Lagos, Nigeria")
# print(res)

user_input=input("Enter your travel query: ")
response = run_travel_agent(user_input=user_input,thread_id="test_user")


print("\nFlight Results:\n")
print(response["answer"])