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
