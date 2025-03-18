import requests
import os

API_URL = "https://api.cricapi.com/v1/currentMatches"
API_KEY = os.getenv("CRICKET_API_KEY")

def get_live_scores():
    try:
        response = requests.get(API_URL, params={"apikey": API_KEY})
        data = response.json()
        
        # Data extraction logic
        matches = data.get("data", [])
        if not matches:
            return "❌ No live matches found."

        score_info = []
        for match in matches:
            teams = match.get("teams", [])
            if "India" not in teams:
                continue  # Skip matches without India
            
            team1 = teams[0]
            team2 = teams[1]
            
            # Score extraction
            score_data = match.get("score", [])
            score_details = "\n".join([
                f"{entry['inning']} - {entry['r']}/{entry['w']} ({entry['o']} overs)"
                for entry in score_data
            ]) if score_data else "Score details unavailable"

            score_info.append(f"🏏 {team1} vs {team2}\n{score_details}")

        return "\n\n".join(score_info) if score_info else "📢 No ongoing India matches."

    except Exception as e:
        print(f"Error fetching cricket scores: {e}")
        return "⚠️ Error fetching scores."
