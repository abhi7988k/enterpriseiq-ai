

\# EnterpriseIQ — AI-Powered Enterprise Assistant



EnterpriseIQ is a full-stack AI-powered application that combines Generative AI, Retrieval-Augmented Generation (RAG), and enterprise application development.



\## Tech Stack



\- Frontend: React.js, JavaScript, HTML, CSS

\- Backend: Java, Spring Boot, Spring Security, JWT

\- AI Service: Python, FastAPI, LangChain

\- Vector Database: ChromaDB

\- Embeddings: Hugging Face Sentence Transformers

\- Database: MySQL



\## Features



\- User registration and authentication

\- JWT-based API security

\- AI-powered chatbot

\- Document-based question answering using RAG

\- Semantic search with vector embeddings

\- REST API integration across services



\## Architecture



React Frontend

&#x20;   |

&#x20;   v

Spring Boot Backend

&#x20;   |

&#x20;   v

FastAPI AI Service

&#x20;   |

&#x20;   v

RAG Pipeline

&#x20;   |

&#x20;   +-- ChromaDB

&#x20;   +-- Document Knowledge Base

&#x20;   +-- LLM



\## Project Structure



enterpriseiq-ai/

├── app/                 # Python AI service

├── backend/backend/     # Spring Boot application

├── frontend/            # React application

├── Data/                # Knowledge-base documents

├── .gitignore

└── README.md



\## Local Development



1\. Configure the required environment variables.

2\. Start MySQL.

3\. Start the FastAPI AI service on port 8000.

4\. Start the Spring Boot backend.

5\. Start the React development server.

6\. Open the frontend and test the chatbot.



\## Security



API keys, database passwords, JWT secrets, virtual environments, and generated vector database files should not be committed to Git.



\## Project Status



Under active development.



