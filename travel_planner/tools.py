# For google search agent tool
from google.adk.tools.google_search_tool import google_search  #convert the google_search function tool(normal function) converted into agent tool. 
from google.adk.agents import Agent  # It is help us to create agent.
from google.adk.tools.agent_tool import AgentTool  # It is help us to create agent tool.

LLM = "gemini-3.5-flash"

search_agent = Agent(
    name="google_search_wrapped_agent",
    model=LLM,
    description="An agent providing Google-search grounding capabilities. It can be used to retrieve relevant information from the web to support travel planning and recommendations.",    
    instruction="""
        * You are a Web Search Specialist that retrieves accurate and relevant information from the internet to support travel-related queries.
        * Search for destination information, attractions, accommodations, transportation options, local customs, weather, and travel requirements when needed.
        * Provide up-to-date and reliable information from trustworthy sources.
        * Use web search to verify facts and gather current details before responding.
        * Present findings clearly and concisely, focusing on information most relevant to the user's travel needs.
        * If information is unavailable or uncertain, clearly communicate the limitation rather than making assumptions
        Important:
        -Always return your response in bullet points
        -Specify what matter to the user.
        """,

    tools=[google_search],

)

google_search_grounding = AgentTool(agent=search_agent)

# -------------------------------

from google.adk.tools import FunctionTool
from geopy.geocoders import Nominatim
import requests

def find_near_by_places_open(query: str, location: str, radius: int=3000, limit: int=5
) -> str:
    """
    Find nearby places for any text quey using only free openStreetMap APIs (no API keys required).

    Args:
        query (str): Type of place to search for (e.g., restaurant, hotel, cafe).
        location (str): City, address, or coordinates.
        radius (float): Search radius in kilometers.
        limit (int): Maximum number of results to return.

    Returns:
        str: List of matching place names and addresses.
    """
    try:
        # Step 1: Geocode the location to get coordinates
        geolocator = Nominatim(user_agent="open_place_finder")
        loc = geolocator.geocode(location)
        if not loc:
            return f"Could not find location '{location}'."

        lat, lon = loc.latitude, loc.longitude

        # Step 2: Query Overpass API for matching places
        overpass_url = "https://overpass-api.de/api/interpreter"
        overpass_query = f"""
        [out:json][timeout:25];
        (
          node["name"~"{query}", i](around:{radius},{lat},{lon});
          node["amenity"~"{query}", i](around:{radius},{lat},{lon});
          node["shop"~"{query}", i](around:{radius},{lat},{lon});
        );
        out body {limit};
        """

        response = requests.get(overpass_url, params={"data": overpass_query})
        if response.status_code != 200:
            return f"Overpass API error: {response.status_code}"

        data = response.json()
        elements = data.get("elements", [])
        if not elements:
            return f"No results found for '{query}' near {location}."

        # Step 3: Format results
        output = [f"Top results for '{query}' near {location}:"]
        for el in elements[:limit]:
            name = el.get("tags", {}).get("name", "Unnamed place")
            street = el.get("tags", {}).get("addr:street", "")
            city = el.get("tags", {}).get("addr:city", "")
            full_addr = ", ".join(filter(None, [street, city]))
            output.append(f"- {name} | {full_addr if full_addr else 'Address not available'}")

        return "\n".join(output)

    except Exception as e:
        return f"Error searching for '{query}' near '{location}': {str(e)}"

location_search_tool = FunctionTool(find_near_by_places_open)   # Now they will create a location_searching_tool