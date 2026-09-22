"""
FastAPI Backend Application Entrypoint.
AgriCarbon Agent - Vietnam Japan AI Hackathon 2026 (Track 3: Green Growth)
Authoritative source: PROJECT.md § Backend Service
"""

import sys
import logging
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.app.api.routes import router
from backend.app.services.engine_service import init_preset_cache

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("agricarbon.backend")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup warmup and graceful shutdown."""
    logger.info("Initializing AgriCarbon Multi-Agent Backend Service...")
    # Pre-warm preset cache for instantaneous demo responses (<0.5s)
    init_preset_cache()
    logger.info("Preset cache warmed up successfully. Multi-Agent Engine ready for TiB Tokyo demo.")
    yield
    logger.info("Shutting down AgriCarbon Backend Service cleanly.")


def create_app() -> FastAPI:
    """Application factory creating configured FastAPI app instance."""
    app = FastAPI(
        title="AgriCarbon Agent Backend API",
        description=(
            "Autonomous Multi-Agent System for Precision Irrigation, Fertilizer Optimization, "
            "and Cryptographic Supply Chain Carbon Auditing (Vietnam Japan AI Hackathon 2026)."
        ),
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json"
    )

    # Enable CORS for Streamlit and web frontends
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Global exception handler
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled server error on {request.url.path}: {str(exc)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "Internal server error occurred in multi-agent execution pipeline.",
                "details": str(exc)
            }
        )

    # Include routes
    app.include_router(router)

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
