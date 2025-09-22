# Gitlab Gists API

Production-ready HTTP API service that fetches GitHub user gists.

## Dependencies

- python3
- FastAPI: Production web framework
- Uvicorn: ASGI production server
- httpx: Async HTTP client
- pytest: Test automation framework

## Features

- RESTful API with OpenAPI documetation at `/docs`
- Health check endpoint at `/health`
- Async implementation for performance under load
- Test automation suite
- Production ready container with health checks 

## API Endpoints 

- `GET /{user}` - Returns JSON array of user's public gists
- `GET /health` - Service health check with timestamps

## Development 

```bash
python -m venv .venv
source .venv/bin/activate 
# or source .venv/bin/activate.fish for fish shell
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
# API available at http://localhost:8080
# Interactive docs at http://localhost:8080/docs
```

## Testing 

./tests.sh
pytest -v 

## Docker Deployment(this is something i would do in prod) 

docker build -t gists-api . 
docker run -p 8080:8080 gists-api

# Docker cleanup

docker stop test-container && docker rm test-container

## CI/CD Pipeline Ready 
- Automated test suite with validation
- Docker health checks configured for orchestration
- Service structured for easy pipeline integration
- Health and monitoring endpoints available 
- Error handling for external API dependencies
