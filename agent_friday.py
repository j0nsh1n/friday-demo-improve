"""
F.R.I.D.A.Y. Voice Agent — Phase 1 (Stability + Personality)
"""

import logging
import asyncio
from dotenv import load_dotenv

from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.voice import Agent

# Plugins
from livekit.plugins import groq as lk_groq
from livekit.plugins import elevenlabs as lk_elevenlabs
from livekit.plugins import sarvam

from friday.config import config
from friday.prompts.jarvis_system_prompt import SYSTEM_PROMPT   # ← this should now work

load_dotenv()

logger = logging.getLogger("friday-agent")
logger.setLevel(logging.INFO if not config.DEBUG else logging.DEBUG)

# ---------------------------------------------------------------------------
# Build providers
# ---------------------------------------------------------------------------

def _build_stt():
    if config.STT_PROVIDER == "sarvam":
        logger.info("STT → Sarvam Saaras v3")
        return sarvam.STT()
    raise ValueError(f"Unknown STT_PROVIDER: {config.STT_PROVIDER}")

def _build_llm():
    if config.LLM_PROVIDER == "groq":
        logger.info(f"LLM → Groq ({config.GROQ_MODEL})")
        return lk_groq.LLM(model=config.GROQ_MODEL)
    raise ValueError(f"Unknown LLM_PROVIDER: {config.LLM_PROVIDER}")

def _build_tts():
    if config.TTS_PROVIDER == "elevenlabs":
        logger.info(f"TTS → ElevenLabs (voice: {config.ELEVENLABS_VOICE_ID})")
        return lk_elevenlabs.TTS(
            voice_id=config.ELEVENLABS_VOICE_ID,
            model=config.ELEVENLABS_MODEL,
        )
    raise ValueError(f"Unknown TTS_PROVIDER: {config.TTS_PROVIDER}")

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def entrypoint(ctx: JobContext):
    logger.info("🚀 F.R.I.D.A.Y. online — Iron Man mode activated")

    agent = Agent(
        instructions=SYSTEM_PROMPT,
        stt=_build_stt(),
        llm=_build_llm(),
        tts=_build_tts(),
    )

    await ctx.connect()
    await agent.start(ctx)
    logger.info("✅ FRIDAY is listening. Say something!")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))