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
* Prompt: only way to communicate with LLM
* you can customize prompt
    - Langchain is trying to collect user's prompt in hub
* `template.format()` returns `string`
* you can validate your prompt by using parameter

## 3.3 Output Parser and LCEL
### Output Parser
* Sometimes you need to transform output response
    - Response -> list, dictionary, tuple, ...
* you can inherit `BaseOutputParser` to make your own parser.

### Lanchain Expression Language
* Make your code much shorter
* Ingrdients
    - chat model
    - template
    - output parser
* chain: makes this ingrdients together
* `|` operator connects these
    ```python
    chain = template | chat | CommaOutputParser()
    chain.invoke(input={"param_1": value_1, "param_2": value_2})
    ```
* internally, when you `invoke` langchain will call:
    1. `.format_messages()`
    2. `.predict()`
    3. `.parse()`
* By this syntax, you can create multiple chains and combine each chain
    ```python
    chain_1 = template_1 | chat_1 | output_parser_1
    chain_2 = template_2 | chat_2 | output_parser_2
    chain_all = chain_1 | chain_2 | output_parser_3
    ```

## 3.4 Chaining Chains
* How LCEL works?
    - official document: [link](https://python.langchain.com/docs/expression_language/interface)
* components of langchain
    - **Prompt**
        - get input as dictionary
        - returns output as `PromptValue`
    - **LLM, ChatModel**
        - get input as single string, list of chat messages or a `PromptValue`
        - returns `ChatMessage`
    - **OutputParser**
        - get input as the output of an LLM or ChatModel (`ChatMessage`)
* How to make chain of chains
    ```python
    chef_chain = chef_prompt | chat
    veg_chain = veg_chef_prompt | chat

    final_chain = {"recipe": chef_chain} | veg_chain
    final_chain.invoke(
        {
            "cuisine": "indian"
        }
    )
    ```

## 3.5 Recap
* **Runnable Map**: first dict runs first, then second one runs (whatever output is)
    ```python
    {"recipe": chef_chain} | veg_chain
    ```
    - because second one (`veg_chain`) needs `recipe` (which is key of dict)
    - mapping output of one chain to an input of the other chain
* `streaming=True`
    - allows us to see response **as it is generating**
* `callbacks`
    - prints every letter console asap

# 4. Model IO
* Langchain has a lot of useful modules
## 4.0 Introductions
* **Model I/O**: Prompts, Language models, Output parsers
    - what we have learned
* **Retrival**: How we can get external data and input into our model
    - Text embedding models, Vector stores, ...
* **Chain**: construct sequence of models
* **Agent**: Make AI autonomous
    - chain itself chooses tools to use
* **Memory**: add memory to chatbot
* **Callbacks**: can see what model is doing
* Theory study order
    - Model I/O -> Memory
    - then we build apps

## 4.1 FewShotPromptTemplate
* Prompts can be saved in disk and loaded
    - you can save prompts in database or in file system
* Fewshot Learning
    - Fewshot: give examples to the model
    - `FewShotPromptTemplate`: can format examples
    - When you want to build a auto-reply bot, you can use your reply histories
* using `FewShotPromptTemplate`
    1. format your example data
        ```python
        example_template = """
            Human: {question}
            AI: {answer}
        """
        example_prompt = PromptTemplate.from_template(example_template)
        ```
    2. define `FewShotPromptTemplate`
        - `suffix`: define how the question looks to user
            - `input_variables`: check validation
    3. call `prompt.format()`
        - it completes question with `suffix` we writes

## 4.2 FewShotChatMessagePromptTemplate
* Doesn't need `suffix`, `input_variables` 

## 4.3 LengthBasedExampleSelector
* Dynamic example selector
    - can decide How many examples feed to prompt
    - API spent money depends on number of examples
* `max_length`: only select examples under the number of `max_length` characters
* Can create own example selector
    - inherits `BaseExampleSelector` and override `select_exampels(self)`, `add_example(self)`

## 4.4 Serialization and Composition
* How to load prompts from disk
    - Save your prompt and share
* you can save your prompt in json or yaml format
    ```python
    from langchain.prompts import load_prompt

    promt = load_promt("./promt.json")
    ```
* Compose many prompts together
    ```python
    from langchain.prompts.pipeline import PipelinePromptTemplate

    intro = PromptTemplate.from_template(
    """
    You are a role playing assistant.
    And you are impersonating a {character}
    """
    )

    example = PromptTemplate.from_template(
        """
        This is an example of how you talk:

        Human: {example_question}
        You: {example_answer}
    """
    )

    start = PromptTemplate.from_template(
        """
        Start now!

        Human: {question}
        You:
    """
    )

    final = PromptTemplate.from_template(
        """
        {intro}
                                        
        {example}
                                
        {start}
    """
    )

    prompts = [
        ("intro", intro),
        ("example", example),
        ("start", start),
    ]


    full_prompt = PipelinePromptTemplate(
        final_prompt=final,
        pipeline_prompts=prompts,
    )
    ```

## 4.5 Caching
* can save money: doesn't have to re-call API
    ```python
    from langchain.globals import set_llm_cache
    from langchain.cache import InMemoryCache

    set_llm_cache(InMemoryCache())
    ```
* also you can shorten time
    - do not hit LLM, the model reuses the answer
* If you want to see log, you can use `set_debug(True)`
* `InMemoryCache` only saves data in your memory (Not on Disk)
    - so it erases data if you re-start your script
* `SQLiteCache` saves data in your database
    ```python
    from langchain.globals import set_llm_cache
    from langchain.cache import SQLiteCache

    set_llm_cache(SQLiteCache("cache.db")) # creates database
    ```
* check out other third-party tools in here: 
    - https://python.langchain.com/docs/integrations/providers

## 4.6 Serialization
* Save & Load Model (+ check how many money I spent)
* check how many money I spent
    ```python
    from langchain.callbacks import get_openai_callback

    with get_openai_callback() as usage:
        chat.predict("What is the recipe for soju?")
        print(usage)
    ```
* Serialzation
    - Save model: `chat.save("model.json")`
    - Load model: 
        ```python
        from langchain.llms.loading import load_llm

        chat = load_llm("model.json")
        ```

# 5. Memory
* Langchaign has a few memory modules
* OpenAI API doesn't apply memory
* We will learn different kinds of memory modules and how to implement them to our model

## 5.0 ConversationBufferMemory
* Saves whole conversation
* **Inefficient**: when conversation gets long, it needs to save large prompt
* Useful in **text completion**

## 5.1 ConversationBufferWindowMemory
* Difference with `ConversationBufferMemory`:
    - saves a part of conversation (not entire one)
    - ex. saves last 5 messages -> when 6th message comes, first message is discarded
* Useful when you want to keep your memory size
* But chatbot **will not able to remember very long ago conversation**

## 5.2 ConversationSummaryMemory
* Makes use of LLM -> **costs money to use**
* It saves **summary** of conversation! (Not the entire text)
    - If you have very long conversation this will be very useful
    - will be efficient in token usage when the conversation is very very long

## 5.3 ConversationSummaryBufferMemory
* Mixture of `ConversationBufferMemory` and `ConversationSummaryMemory`
* when conversation hits **limit**, it summarizes old messages -> Able to keep track of recent conversation while save old messages
    - `max_token_limit` is the limit we use
* `SystemMessage` tells whether it is ummarized

## 5.4 ConversationKGMemory
* Conversation Knowledge Graph Memory
* Also uses LLM
* Builds entity's knowledge graph - summary of important pieces
* you can check other types of Memory modules: https://python.langchain.com/docs/modules/memory/types
* `Entity`: [What is Named Entity Recognition(NER)?](https://www.datacamp.com/blog/what-is-named-entity-recognition-ner)
* There are many integrations between memory and database

## 5.5 Memory on LLMChain
* How to plug memory into our chain
### 1. LLM Chain
* off-the-shelf chain: general purpose chain <-> build our own code
    ```python
    chain = LLMChain(
        llm=llm,
        memory=memory,
        prompt=PromptTemplate.from_template("{question}"),
        verbose=True, # for debug
    )
    ```
* memory is being updated, but it doesn't feed data into prompt
* -> You should tell Memory class to **put content inside Template**
    - `memory_key`: gives formatted key string which is used in template

## 5.6 Chat Based Memory
* `MessagesPlaceholder`: can receive message whether it is created by human or AI
    - you cannot know how many messages are created above and who sent them.
    - so it is convenient to use `MessagesPlaceholder`
        ```python
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful AI talking to a humn"),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),

            ]
        )
        ```
    
## 5.7 LCEL Based Memory
### 2. Build your own code (Langchain Expression Language)
* Recommended way, but very manual process
* `RunnablePassthrough`: assign values by calling a function
    ```python 
    from langchain.schema.runnable import RunnablePassthrough

    def load_memory(_):
        return memory.load_memory_variables({})["chat_history"]

    chain = RunnablePassthrough.assign(chat_history=load_memory) | prompt | llm
    ```
    - **Caution**: every component gets input from former component and returns output to next component
    - which means, `load_memory` function would get input value when `chain.invoke({"question": "What is your name?"})`

## 5.8 Recap
* Saving Memory of Our LLM
    1. Using LLM Chain
    2. Using Chat Prompt Template
    3. Manual way (LCEL)
        - recommended way: because you can do many things with memory; persist it load it from somewhere else
        - other frameworks hide what happens inside

# 6. RAG
* Build our own document GPT App
## 6.0 Introductions
* not using Streamlit yet: start with jupyter notbook
    - bad UI, but good to learn building blocks
* **RAG**: Retrieval Augmented Generation
    - using extra sources (ex. private document) to provide to our model for better performance
    - expand capability of LLM
    - our model receives these:
        1. Question
        2. extra data: Context <- extra sources we provide to the model
        3. (data which is already used for training the model)
    - There are many ways to build RAG

## 6.1 Data Loaders and Splitters
* First step of RAG: **Retrieval**
* Load
    - There are a huge number of Data Loaders that Langchain provides
        - official document: https://python.langchain.com/docs/integrations/document_loaders/
    - `UnstructuredFileLoader` is compatible with different kinds of file types
* Transform: Split the document before you embed
    - `RecursiveCharacterTextSplitter`: use `chunk_overlap` to make sure not cut in middle of a sententce
    - `CharacterTextSplitter`: use `separater`

## 6.2 Tiktoken
* Token is different with character or word
    - Test: https://platform.openai.com/tokenizer
* Tiktoken is published by OpenAI
    - `from_tiktoken_encoder`

## 6.3 Vectors
* Embed
    - Turn human language into numbers to make computers understand
    - =**Vectorizaion**
    - You can do operations with numbers
    - You can calculate distance -> use distance to find similar words
    - **Purpose of Embedding: Search Database to find similar words**
* Useful sites
    - https://turbomaze.github.io/word2vecjson/
    - https://www.youtube.com/watch?v=2eWuYf-aZE4

## 6.4 Vector Store
* how to save money?: Embedding is not free
* Langchain has OpenAI Embedding Models
    ```python
    from langchain.embeddings import OpenAIEmbeddings

    embeddings = OpernAIEmbeddings()
    embeddings.embed_query("Hi")
    ```
* You should save embeddings not to call every time you want to embed
* Vector stores save vectors locally (or on cloud)
* Open source free Vector Store: `Chroma`
    - It saves vectors locally
    ```python
    from langchain.vectorstores import Chroma

    loader = UnstructredFileLoader("./files/george_orwell_1984_ch1.txt")
    docs = loader.load_and_split(text_splitter=splitter)
    vectorstore = Chroma.from_documents(docs, embeddings)
    ```
    - now you can **search** in your local vector store!
* Cache your embeddings to save money
    ```python
    from langchain.embeddings import CachedBackedEmbeddings
    from langchain.storage import LocalFileStore

    cache_dir = LocalFileStore("./.cache/")
    cached_embeddings = CachedBackedEmbeddings(
        underlying_embeddings=embeddings,
        document_embedding_cache=cache_dir,
    )

    vectorstore = Chroma.from_documents(docs, cached_embeddings)
    ```

## 6.5 Langsmith
* https://www.langchain.com/langsmith
    - sign up and wait for invitation code

## 6.6 RetrievalQA
* Document chains
* LLM Chain is considered as legacy
    - preferred to use LCEL (LangChain Expression Language)
        - better to see all configurations
* `Stuff` documents chain
    ```python
    from langchain.chains import RetrievalQA
    
    chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff",
        retriever=vectorstore.as_retriever(), # interface of class which retrieves documents from many places like cloud, vector store
    )

    chain.run("Describe Victory Mansions")
    ```
* Langsmith would show how internal sysmtem works
    ```
    Retriever
    >> StuffDocumentsChain
        >> LLMChain
            >> ChatOpenAI
    ```
    - Final Prompt constitutes like this:
        - `System`: "Use the following pieces of context to answer the user's question. ... "
            - Puts all documents it founds (how `Stuff` chain_type works)
        - `Human`: "Describe Victory Mansions"
* `RetrievalQA` can change `chain_type` easily
    ```python
    chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="refine", # "map_reduce", "map_rerank"
        retriever=vectorstore.as_retriever(),
    )
    ```
    - reference: https://python.langchain.com/docs/modules/data_connection/retrievers/
    - a bit obscure: hard to customize yet
        - lack explaination yet

## 6.7 Recap
* What happens so far
    1. Load Files
    2. Split files to handle big documents with smaller pieces
    3. Embedding: make vectors
    4. Save embedding to cache (for cheaper bill)
    5. Call Vector store
    6. RetrievalQA (chain) 
        - `llm`, `chain_type`, `retriever`
    7. Run it! - magic happens!
* Various types of `chain_type`
    - "stuff", "refine", "map_reduce", "map_rerank"
* Next time we will implement "stuff" by ourself 
    - Every internal process will be exposed.

## 6.8 Stuff LCEL Chain
* make Stuff Chain with LCEL (reference: https://python.langchain.com/docs/expression_language/interface)
    ```python
    retriever = vectorstore.as_retriver()
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Answer questions using only the following context. If you don't know the answer just say yhou don't know, don't make it up:\n\n{context}"),
            ("human", "{question}")
        ]
    )
    llm = ChatOpenAI(temperature=0.1)

    chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

    chain.invoke("Describe Victory Mansions")
    ```
* much more clear than using obscure modules

## 6.9 Map Reduce LCEL Chain
* How Map Reduce chain works
    1. prepare list of docs
    2. for each doc in list, make `promp | llm` chain
    3. get each response from list and put them all together -> final doc
    4. final doc | prompt | llm
* script
    ```python
    
    map_doc_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                Use the following portion of a long document to see if any of the text is relevant to answer the question. Return any relevant text verbatim.
                ------
                {portion}
                """
            ),
            ("human", "{question}"),
        ]
    )
    map_doc_chain = map_doc_prompt | llm

    def map_docs(inputs):
        documents = inputs['documents']
        question = inputs['question']
        
        results = [map_doc_chain.invoke({"portion": doc.page_content, "question": question}).content for doc in documents]
        return "\n\n".join(results)
    
    map_chain = {"documents": retriever, "question": RunnablePassthrough()} | RunnableLambda(map_docs)

    final_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                Given the following extracted parts of a long document and a question, create a final answer.
                If you don't know the answer, just say that you don't know. Don't try to make up an answer.
                ------
                {context}
                """
            ),
            ("human", "{question}"),
        ]
    )

    chain ={"context": map_chain, "question": RunnablePassthrough()} | final_prompt | llm

    chain.invoke("Describe Victory Mansions")
    ```

## 6.10 Recap
* recap what we have done at last lecture
* `RunnableLambda` get function which is runnable
* Next time learn beautiful interface `Streamlit`

# 7. DocumentGPT
## 7.0 Introduction
* [Streamlit](https://streamlit.io)
* import and run stream lit
    ```bash
    streamlit run home.py
    ```
    -> will run local server

## 7.1 Magic
* at 7.0, we learned how to import streamlit and applied 3 kinds of **widgets**
* `st.write`: what streamlit calls **Magic**
    - it will print out everything
    - why magic?
        - just putting `a` is same with `st.write(a)`
* There are a lot of widgets streamlit provides

## 7.2 Data Flow
* Every time your data changes, whole python file would run again
    - Differenct with Web development framework like React
* You can cache

## 7.3 Multi Page
* How to create side bars
* easy way
    ```python
    st.sidebar.title("sidebar 1")
    ```
* proper way
    ```python
    with st.sidebar:
        st.title("sidebar 1")
        st.text_input("xxx")
    ```
* proper way means that the pattern is used a lot for differents kinds of widgets
    ```python
    tab_a, tab_b, tab_c = st.tabs(["A", "B", "C"])

    with tab_a:
        st.write("a")
    
    with tab_b:
        st.write("b")

    with tab_c:
        st.write("c")

    ```
* `st.set_page_config()` can configure your browser tab name

## 7.4 Chat Messages
* start to build chat bot with streamlit and langchain 
* **IMPORTANT**: when data changed file runs again!
    - You need a system that saves data
    - `st.session_state`

## 7.5 Recap
* `session_state`: used for data that should not be forgotten

## 7.6 Uploading Documents
* recap RAG
    1. load file
    2. split file
    3. embed -> cache
    4. vectorstore -> retriever
        - Stuff LCEL
    5. make prompt
* will learn how to cache in Streamlit
    - Streamlit runs your code top to bottom
* configure .env directory to read API Key
    - Streamlit uses secrets

## 7.7 Chat History
* streamlit runs from top to bottom every time you refresh
* streamlit is smart enough to know changes of files

## 7.8 Chain
* You can build retriever -> prompt manually, but we will do it with chain
    * manual invoke
        ```python
        docs = retriever.invoke(message)
        docs = "\n\n".join(document.page_content for document in docs)
        prompt = template.format_messages(context=docs, question=message)
        ```
* recap `RunnableLambda()`, `RunnablePassthrough()`

## 7.9 Streaming
* Instead of waiting for whole response, let's apply callback handler
* `BaseCallbackHandler`
* `*args`: recieves arguments like this:
    - `on_llm_start(1, 2, 3, 4)`
* `**kwargs`: recieves keyworded arguments like this:
    - `on_llm_start(a=1, a=4, b=1)`
* `CallbackHandler` is called when `llm` is invoked
    - if it is invoked **inside chate_message**, then message_box.markdown() is treated as chat_message()!
    - but it is not saved in our cache. -> if we ask another question, previous answer text would be disappeared
    - we use `on_llm_end()` to save in our cache

## 7.10 Recap
* streamlit -> make UI
* upload and save file to cache
* langchain which uses OpenAI Chat model
    - invoke it with streamlit message
* how to stream AI message
* Next time
    - Next embedding (llm) model
    - not to pay money
    - not to send our data to others
* Code challenge
    - chain doesn't have memory yet -> **make langchain memory**

# 8. PrivateGPT
## 8.0 Introduction
* Will swap our embedding and chat model
* Download model and will run our model offline
* HuggingFace, GPT4All, Ollama

## 8.1 HuggingFaceHub
* https://huggingface.co/
* How to Download models to our local PC and use them
    - 2ways: Download vs Inference API
* Inference API
    - `mistralai/Mistral-7B-Instruct-v0.2` is free API
    - you can check API document here: https://huggingface.co/docs/api-inference/index
    - you can make prototype with free
* You can develop your prompt by checking out and study the model(this time `mistralai`)'s official documentation
    - https://docs.mistral.ai/
    - If you follow format which docuemnts provide, you can develop your model performance.

## 8.2 HuggingFacePipeline
* Download a model and run in our local
    - Nvidea GPU is much faster (MacBook would be slow)
* For practice, we will download GPT2
* `device`: 0 for GPU, -1 for CPU
    - 0 doesn't work for MacBook Pro

## 8.3 GPT4All
* Another awesome way to run local model on our computer
    - https://gpt4all.io/index.html
* Not many models yet (less than HuggingFaceHub)
* Download and run model like this:
    ```python
    llm = GPT4All(
        model="./falcon.bin",
    )
    ```

## 8.4 Ollama
* Nico's favorite way to use LLM locally
* Download model from official site
    - https://ollama.com/download
* check downloaded: run `ollama` in terminal
* run mistral
    ```bash
    ollama run mistral
    ```
    - When you run it first time, it would download the model
* How Ollama works
    1. makes a server in your machine
    2. when you run a command, then an API hits the server
    3. the server returns values with streaming
* `ollama` has many commands like `list`, `rm`, ...
* You can use ollama model in Lanchain Framework
    ```python
    from langchain.embeddings import OllamaEmbeddings
    from langchain.chat_models import ChatOllama
    ```
* Mistral is a instruct-based model, So you should give specific instructions to your model

## 8.5 Conclusions
* next time: 
    - how to bring data from webiste like Wikipedia to build QuizGPT
    - more about streamlit
* Code Challenge: create input with select box widget
    - allow to change model

# 9. QuizGPT
## 9.0 Introduction
* **output parser**: force model to answer in specific format
* only available features in OpenAI GPT3 and GPT4
    - **Function Calling**: can describe how our function behaves and what parameters it needs to LLM
        - LLM will reply with function

## 9.1 WikipediaRetriever
* How to get document from Wikipedia
    ```python
    from langchain.retrievers import WikipediaRetriever
    ```

## 9.2 GPT-4 Turbo
* Find a way to give all text to LLM to generate questions about it
* GPT-4 Turbo has a large context window

## 9.3 Questions Prompt
* Build chain to generate questions
* Give examples to prompt to format the questions
    - you should consider prompt - performance of the llm depends on it
