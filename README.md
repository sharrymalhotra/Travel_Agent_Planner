# Travel Planner Agent

An AI-powered travel planning system built with Google ADK that helps users discover destinations, create personalized itineraries, retrieve current travel updates, and find nearby places of interest.

## Architecture

                         Travel Planner
                           (agent.py)
                                │
                                ▼
                  Travel Inspiration Agent
                    (supporting_agents.py)
                         /             \
                        /               \
                       ▼                 ▼
                News Agent         Place Agent
           (supporting_agents.py) (supporting_agents.py)
                    │                    │
                    ▼                    ▼
      Google Search Grounding      Nearby Places Tool
              (tools.py)              (tools.py)
                    │                      │
                    ▼                      (Function tool)
            Google Search API             


## Project Structure


Travel_planner_post
│
├── pyproject.toml
│
└── travel_planner
    │
    ├── __init__.py (for root)
    ├── agent.py
    ├── supporting_agents.py
    └── tools.py


## Components

### Travel Planner Agent

**File:** `agent.py`

Responsibilities:

* Acts as the main orchestrator(managing and coordinating multiple component).
* Collects travel requirements.
* Creates personalized travel plans.
* Delegates destination discovery tasks to the Travel Inspiration Agent.

---

### Travel Inspiration Agent

**File:** `supporting_agents.py`

Responsibilities:

* Suggests destinations and travel experiences.
* Recommends trip themes and itinerary ideas.
* Requests additional information when necessary.
* Consults specialized agents when needed.
* Ends every response with a witty travel joke.

---

### News Agent

**File:** `supporting_agents.py`

Responsibilities:

* Provides current travel news and updates.
* Retrieves visa updates and travel advisories.
* Checks transportation disruptions and weather impacts.
* Uses the Google Search Grounding tool to obtain the latest information.

---

### Place Agent

**File:** `supporting_agents.py`

Responsibilities:

* Provides destination-specific recommendations.
* Suggests attractions, accommodations, and transportation.
* Retrieves nearby places using the Nearby Places Tool.
* Shares local culture and travel insights.

---

### Google Search Grounding Tool

**File:** `tools.py`

Responsibilities:

* Performs web searches.
* Verifies current travel information.
* Supports the News Agent with up-to-date information.

---

### Nearby Places Tool

**File:** `tools.py`

Responsibilities:

* Finds nearby attractions, restaurants, hotels, and other points of interest.
* Supports destination-specific recommendations.

## Features

* Personalized travel planning
* Solo, couple, family, and group trip recommendations
* Day-wise itinerary generation
* Budget-based travel suggestions
* Accommodation recommendations
* Transportation guidance
* Local culture and food recommendations
* Nearby place discovery
* Current travel advisories and news
* Festival and event updates
* Hidden gem recommendations
* Witty travel jokes

## Installation

### 1. Install UV

```powershell
pip install uv
```

### 2. Initialize the Project

```powershell
uv init .
```

This creates the project configuration files.

### 3. Install Dependencies

```powershell
uv add google-adk python-dotenv
```

- **google-adk**: Framework for building AI agents.
- **python-dotenv**: Manages environment variables securely.

### 4. Create a `.env` File

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the Application

```powershell
uv run adk web travel_planner
```

### 6. Run the Application

Start the ADK web interface:

```powershell
uv run adk web travel_planner
```

### 7. Run on a Custom Port

```powershell
uv run adk web travel_planner --port 8001


## Example Query

```text
I'm planning a 10-day solo trip to Japan in October with a budget of $2,000.

Please:
- Recommend destinations.
- Create a detailed itinerary.
- Suggest accommodations and transportation.
- Recommend food and cultural experiences.
- Include hidden gems.
- Check current travel advisories and events.
- Provide safety and packing tips.
- End with a witty travel joke.
```

## Technologies Used

* Python
* Google ADK
* Gemini Models
* Google Search Tool
* Agent Tools
* UV Package Manager

## Future Improvements

* Flight recommendation integration
* Hotel booking integration
* Weather forecasting tools
* Interactive maps
* Expense tracking
* Multi-country itinerary planning

## License

This project is intended for educational and learning purposes.
