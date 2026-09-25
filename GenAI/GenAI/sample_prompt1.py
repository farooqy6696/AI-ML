# ============================================================
# Install Packages:
# pip install google-genai python-dotenv
# ============================================================
 
import os
from google import genai
from dotenv import load_dotenv
 
# ============================================================
# Load Environment Variables
# ============================================================
 
load_dotenv()
 
# ============================================================
# Check Question Relevance
# ============================================================
 
def is_sql_related(question: str) -> bool:
 
    prompt = f"""
    You are a strict classifier.
 
    Return ONLY YES or NO.
 
    Return YES only if the question is clearly related to:
    - SQL
    - SQL Queries
    - Relational Databases
    - Database Concepts
    - MySQL
    - PostgreSQL
    - Microsoft SQL Server
    - Oracle SQL
    - SQLite
    - Database Tables
    - SELECT, INSERT, UPDATE, DELETE
    - JOINs
    - GROUP BY
    - ORDER BY
    - WHERE
    - HAVING
    - Subqueries
    - CTEs
    - Window Functions
    - Stored Procedures
    - Views
    - Indexes
    - Primary Keys
    - Foreign Keys
    - Constraints
    - Normalization
    - Transactions
    - SQL Functions
 
    Return NO for:
    - Greetings
    - Random text
    - Gibberish
    - Unclear inputs
    - Personal conversation
    - Python questions
    - Java questions
    - C/C++ questions
    - JavaScript questions
    - HTML/CSS questions
    - FastAPI or Flask questions
    - General programming questions not related to databases
    - AI/ML questions
    - Non-technical topics
 
    Examples:
 
    Question: What is a SQL JOIN?
    Answer: YES
 
    Question: How do I use GROUP BY in SQL?
    Answer: YES
 
    Question: Explain the difference between DELETE and TRUNCATE.
    Answer: YES
 
    Question: What is a primary key?
    Answer: YES
 
    Question: Write a query to find the second highest salary.
    Answer: YES
 
    Question: hi
    Answer: NO
 
    Question: What is a Python dictionary?
    Answer: NO
 
    Question: Explain FastAPI dependency injection.
    Answer: NO
 
    Question: What is machine learning?
    Answer: NO
 
    Question: What is Java?
    Answer: NO
 
    Question: Tell me a joke.
    Answer: NO
 
    Question:
    {question}
 
    Answer:
    """
 
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
 
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config={
            "temperature": 0
        }
    )
 
    answer = response.text.strip().upper()
 
    return answer == "YES"
 
 
# ============================================================
# Generate Response
# ============================================================
 
def generate(question: str):
 
    # Restrict Non-SQL Questions
    if not is_sql_related(question):
 
        print(
            "\n⚠️ I'm currently designed to provide responses only "
            "for SQL and database-related learning queries.\n"
            "Please ask a question related to SQL or databases.\n"
        )
 
        return
 
    # Gemini Client
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
 
    model = "gemini-3-flash-preview"
 
    # System Prompt
    system_prompt = """
    You are an AI SQL learning assistant.
 
    Your job is to help users learn SQL and database concepts.
 
    You can answer questions related to:
    - SQL queries
    - SELECT, INSERT, UPDATE, DELETE
    - WHERE, GROUP BY, ORDER BY, HAVING
    - JOINs
    - Subqueries
    - CTEs
    - Window functions
    - Aggregate functions
    - SQL functions
    - Primary keys
    - Foreign keys
    - Constraints
    - Database relationships
    - Normalization
    - Indexes
    - Views
    - Stored procedures
    - Transactions
    - MySQL
    - PostgreSQL
    - SQL Server
    - Oracle SQL
    - SQLite
    - Relational database concepts
 
    Rules:
    - Respond only to SQL and database-related learning queries.
    - Keep explanations clear and beginner-friendly.
    - Provide SQL examples when useful.
    - Explain queries step by step when appropriate.
    - Use code blocks for SQL code.
    - If the question is unrelated to SQL or databases, politely refuse.
    - Do not answer questions about unrelated programming languages or technologies.
    """
 
    full_prompt = f"""
    {system_prompt}
 
    User Question:
    {question}
    """
 
    # Streaming Response
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=full_prompt,
    ):
        if chunk.text:
            print(chunk.text, end="")
 
 
# ============================================================
# Main
# ============================================================
 
if __name__ == "__main__":
 
    question = input("Enter your SQL question: ")
 
    generate(question)
 
 

 