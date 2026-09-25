# Gemini AI – Intelligent Document Analyzer

Reads a document, summarizes it with Gemini AI, generates interview
questions from it, and stores the results in MongoDB.

## Layered Architecture

```
main.py                                     <- Presentation layer (entry point)
layers/
  config/settings.py                        <- Configuration layer
  exceptions.py                             <- Shared exception types
  data_access/
    file_reader.py                          <- Data access: reads the document
    mongo_repository.py                     <- Data access: MongoDB persistence
  business/
    gemini_service.py                       <- Business: Gemini API calls
    document_analyzer_service.py            <- Business: orchestrates the workflow
```

Each layer only talks to the layer directly below it:
`main.py` → `business` → `data_access`. The data access layer never
imports the business layer, and the business layer never imports Gemini
or Mongo SDKs directly outside of `gemini_service.py` /
`mongo_repository.py`, so each piece can be swapped or unit-tested
independently.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and fill in your values:
   ```bash
   cp .env.example .env
   ```
   - `GEMINI_API_KEY` — get one from https://aistudio.google.com/app/apikey
   - `MONGO_URI` — e.g. `mongodb://localhost:27017` or an Atlas connection string
   - `DOCUMENT_PATH` — defaults to the included `sample_document.txt`

3. Make sure MongoDB is running (locally or Atlas) and reachable at `MONGO_URI`.

## Run

```bash
python main.py
```

## Expected Output

```
Document Read Successfully.
Document Summary Generated Successfully.
Interview Questions Generated Successfully.
Analysis Saved to MongoDB.
Operation Completed Successfully.

--- Summary ---
<Gemini-generated summary>

--- Interview Questions ---
1. <question 1>
2. <question 2>
...

Saved MongoDB Record ID: <mongo object id>
```

## Notes

- Swap `DOCUMENT_PATH` in `.env` to point at any `.txt` file you want analyzed.
- All failure modes (missing file, bad API key, unreachable MongoDB) raise a
  specific exception type from `layers/exceptions.py` and are caught in
  `main.py`, which prints `Operation Failed: <reason>` instead of crashing.
