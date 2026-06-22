from google.adk.agents import Agent

from travel_planner.tools import google_search_grounding,location_search_tool
from google.adk.tools.agent_tool import AgentTool


LLM = "gemini-3.5-flash"

# after that 2 create this one (new_agent)
news_agent = Agent(
    name="news_agent",
    model=LLM,
    description= "Provides up-to-date travel news, updates, events, and advisories.",
    instruction="""
        * You are a Travel News Specialist responsible for providing up-to-date travel news, advisories, events, visa updates, transportation disruptions, weather impacts, and other travel-related information relevant to the user's destination or travel plans.
        * Always use the `google_search_grounding` agent/tool to search, verify, and retrieve the latest information before responding, and present the findings clearly, accurately, and concisely.
""",
    tools=[google_search_grounding],
)


# after that 3 create this one (new_agent)
place_agent = Agent(
    name="place_agent",
    model=LLM,
    description= "Suggests locations based on user preferences.",
    instruction="""
You are responsible for providing accurate and relevant location information based on user queries. Use the `location_search_tool` to retrieve specific location details when needed, and ensure that your responses are clear, concise, and directly address the user's request for location information.Limit the choices to 10 results.
Each place must have a name, location, and address.
You can use the places_tool to find the latitude and longitude of the place and address.
""",
    tools=[location_search_tool],
)


#This is create 1st
travel_inspiration_agent = Agent(
    name="travel_inspiration_agent",
    model=LLM,
    description= "Creates travel inspiration, destination ideas, trip themes, and fun travel suggestions. "
                 "Every response from this agent ends with a short witty travel joke or travel pun.",
    instruction="""
        You are a travel inspiration specialist. Help users discover appealing destinations,
        trip themes, memorable experiences, and creative travel ideas.

        IMPORTANT:
            * You are a Travel Inspiration Specialist who helps users discover destinations, travel experiences, trip themes, and itinerary ideas.
            * Ask follow-up questions when important travel details are missing.
            * Consult `place_agent` for destination-specific information, attractions, accommodations, transportation, and local culture.
            * Consult `news_agent` for recent travel updates, events, festivals, advisories, and current travel conditions.
            * Provide engaging, personalized, and practical travel recommendations tailored to the user's interests.
            * Every response must end with a short witty travel joke or travel pun, and the joke must be the final sentence of the response.

        """,
    tools=[AgentTool(agent=news_agent),AgentTool(agent=place_agent)], # we will provide travel_inspiration_agent provided a sub-agent.
)


