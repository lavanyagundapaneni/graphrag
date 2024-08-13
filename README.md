# Pure graphrag
This repository contains a Python application that demonstrates how to use Neo4j for graph-based data storage and querying, combined with LangChain's LLM capabilities (using the Ollama LLaMA 2:7b model) to generate answers to questions based on the graph data.

## Features
1. Connect to a Neo4j database and execute queries.
2. Fetch and process data from the graph database.
3. Use LangChain with the Ollama LLaMA model to generate natural language answers based on graph data.
4. using the graph data generate a formatted answer.

## Configuration
1. ### Neo4j Configuration:
   Ensure you have a running instance of Neo4j. Update the Neo4j connection settings in the script with your database credentials:
    - URI:The address of your Neo4j instance (e.g., bolt://localhost:7687).
    - Username: Your Neo4j username (default is usually neo4j).
    - Password: The password for your Neo4j database.
2. ### Python Environment Setup:
   Install the necessary Python libraries using pip:
   ` pip install langchain_community neo4j ollama`

## Create Python Script:
   Create a Python script (e.g., neo4j_llama_integration.py) and add the following code:

```from neo4j import GraphDatabase
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Step 3.1: Neo4j connection settings
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

# Step 3.2: Initialize Neo4j driver
try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
except Exception as e:
    print(f"Error initializing Neo4j driver: {e}")
    raise

# Step 3.3: Function to execute a query and fetch results from Neo4j
def fetch_data_from_neo4j(query, parameters=None):
    try:
        with driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]
    except Exception as e:
        print(f"Error fetching data from Neo4j: {e}")
        return []

# Step 3.4: Initialize Ollama LLaMA 2:7b model
llm = Ollama(model="llama2:7b")

# Step 3.5: Function to generate graph-based answers
def generate_graph_rag(question, graph_data):
    # Define the prompt template
    prompt_template = """
    You are a language model interacting with a Neo4j graph database. 
    The following is data retrieved from the graph database. 
    Answer the question using only this data. Do not generate or infer any information that is not directly present in the data.

    Graph Data: {graph_data}

    Question: {question}

    Answer the question using only the provided graph data.
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["graph_data", "question"])

    # Create LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)

    try:
        # Generate answer
        response = chain.run(graph_data=graph_data, question=question)
        return response
    except Exception as e:
        print(f"Error generating answer: {e}")
        return "Error generating answer."
```
   
   




