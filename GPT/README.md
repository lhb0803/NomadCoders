# 2. Introduction
## 2.1 Requirements
* Don't need any deeplearning knowledge
* Python: Only requirements
    - Langchain, FastAPI, Streamlit
* Extremely Easy to build GPT apps

## 2.2 What Are We Using?
### Langchain
* Framework to build LLM model (makes it much easier)
* A lot of useful modules
    - ex. Module for Memory, Document, Embedding, Prompt, ...
* Can compose a lot of different company's models

### Streamlit
* Generate UI for AI application without using JS stuff

### Pinecone
* Database for vector

### Hugginface
* Can get other model that is not GPT
    - Can learn to host other model
* Github for AI
    - Still GPT is BEST

### FastAPI
* Easy framework to build API

## 2.3 OpenAI Requirements
* Need to subscribe ChatGPT Plus (paid service)
* Create API key
    - need to enroll credit card
    - **MUST put usage limit** (useful for debug)

## 2.5 Virtual Environment
* Isolate installation depending on project
* get requirements.txt from lecuture ([link](https://gist.github.com/serranoarevalo/72d77c36dde1cc3ffec34105eb666140))

## 2.6 Jupyter Notebook
* with vscode

# 3. Welcome to Langchain
## 3.0 LLMs and Chat Models
* familiarize with LLM
* LLM vs Chat Model
* Various models to use but APIs are unified -> very easy to use
* When jupyter notebook runs, environment variables in `.env` file are loaded
    - should name the variable exactly `OPENAI_API_KEY`

## 3.1 Predict Messages
* Chat Model can do conversation (group fo messages)
* you can put argument when initiate constructor
    - `temperature`: low -> not clever model vs high -> randomness
* `Message`: you can make a list of message
    - `SystemMessage`, `AIMessage`, `HumanMessage`
* next lecture: make prompt more useful

## 3.2 Prompt Templates
* 