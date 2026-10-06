import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    QDRANT_API_KEY=os.getenv('QDRANT_API_KEY')
    QDRANT_URL=os.getenv('QDRANT_CLUSTER_ENDPOINT')
    GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')
    QDRANT_COLLECTION='enterprise_rag'

    GROQ_MODEL=os.getenv('GROQ_MODEL') 
    GROQ_API_KEY=os.getenv('GROQ_API_KEY')
    GROQ_FALLBACK_API_KEY=os.getenv('GROQ_FALLBACK_API_KEY')

    # --- LLM GATEWAY (PORTKEY) ---
    PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
    GROQ_SLUG =  os.getenv("GROQ_SLUG")    # primary: @rag/llama-3.3-70b-versatile
    GROQ_SLUG_2 = os.getenv("GROQ_SLUG_2")  # fallback: @brag/llama-3.1-8b-instant
    
settings= Settings()