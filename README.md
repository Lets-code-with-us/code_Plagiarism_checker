# Code Plagiarism Checker

FastAPI-based backend for code similarity/plagiarism scoring using preprocessing + TF-IDF + cosine similarity.

## Features

- Accepts code and language id through an HTTP API.
- Removes comments based on language style.
- Creates a temporary source file in `temp/`.
- Tokenizes code and vectorizes with `TfidfVectorizer`.
- Computes similarity score using cosine similarity (returned internally as percentage).

## Tech Stack

- Python 3.12+
- FastAPI
- scikit-learn

## Project Structure

```
.
├── main.py                    # FastAPI app and routes
├── base/model.py              # TF-IDF vectorization + similarity search
├── model/code.py              # Request body schema (Pydantic)
├── modules/preprocess.py      # Language-aware comment removal + token prep
├── modules/genrate_code_file.py # Writes submitted code to temp file
├── temp/                      # Generated temporary source files
├── setup.bash                 # Create virtual environment (uv)
└── activate.bash              # Activate virtual environment
```

## Supported Languages

Language ids used by the API:

- `0` → C
- `1` → C++
- `2` → Java
- `3` → JavaScript (node)
- `4` → Rust
- `5` → Python

## Setup

### 1) Create virtual environment

```bash
./setup.bash
```

### 2) Activate environment

```bash
source .venv/bin/activate
# or
./activate.bash
```

### 3) Install dependencies

```bash
pip install -e .
```

## Run Server

```bash
fastapi dev main.py
```

App runs at `http://127.0.0.1:8000` by default.

## API

### `GET /`

Health check/sample route.

Response:

```json
{
	"Hello": "World"
}
```

### `POST /`

Request body:

```json
{
	"language": 0,
	"code": "#include <stdio.h>\nint main(){return 0;}"
}
```

Current response:

```json
{
	"message": "Done"
}
```

## How Scoring Works (Current Implementation)

1. Input code is preprocessed (comment removal by language).
2. Cleaned code is saved in `temp/` with language extension.
3. File content is split into tokens and used as corpus.
4. TF-IDF matrix is built from corpus.
5. Cosine similarity score is computed against a query snippet.

## Current Limitation

The current `POST /` route computes a score internally but uses a hardcoded query snippet and does not return the score in the API response yet.

## License

This project is licensed under the MIT License.