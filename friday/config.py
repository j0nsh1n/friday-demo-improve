"""Centralized configuration for F.R.I.D.A.Y."""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # === Providers ===
    STT_PROVIDER = os.getenv("STT_PROVIDER", "sarvam")
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")
    TTS_PROVIDER = os.getenv("TTS_PROVIDER", "elevenlabs")

    # === LLM ===
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    # === TTS ===
    ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")  # Bella (reliable)
    ELEVENLABS_MODEL = os.getenv("ELEVENLABS_MODEL", "eleven_turbo_v2_5")
    OPENAI_TTS_VOICE = os.getenv("OPENAI_TTS_VOICE", "nova")
    TTS_SPEED = float(os.getenv("TTS_SPEED", "1.15"))

    # === Sarvam (fallback) ===
    SARVAM_TTS_LANGUAGE = "en-IN"
    SARVAM_TTS_SPEAKER = "rohan"

    # === MCP Server ===
    MCP_SERVER_PORT = int(os.getenv("MCP_SERVER_PORT", "8000"))

    # === Logging ===
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

config = Config()