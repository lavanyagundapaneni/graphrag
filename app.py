from neo4j import GraphDatabase
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Neo4j connection settings
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

# Initialize Neo4j driver
try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
except Exception as e:
    print(f"Error initializing Neo4j driver: {e}")
    raise

# Function to execute a query and fetch results from Neo4j
def fetch_data_from_neo4j(query, parameters=None):
    try:
        with driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]
    except Exception as e:
        print(f"Error fetching data from Neo4j: {e}")
        return []

# Initialize Ollama LLaMA 2:7b model
llm = Ollama(model="llama2:7b")

# Function to generate graph-based answers
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

# Example usage
# Define your graph query here
graph_query = """
MATCH (s:Student)-[:WANTS_TO_PURUSE]->(d:Degree)-[:AT_UNIVERSITY]->(uni:University)
WHERE uni.name = 'University of California, Berkeley'
RETURN s.name AS student_name, d.name AS degree_name
"""

# Fetch data from Neo4j
data = fetch_data_from_neo4j(graph_query)

# Convert the fetched data to a string format to be passed into the prompt
graph_data = "\n".join([f"{record['student_name']} is pursuing {record['degree_name']}" for record in data])

# Define a question related to the fetched data
question = "Which students are pursuing a degree at University of California, Berkeley?"

# Generate and print the answer using LLaMA 2:7b
answer = generate_graph_rag(question, graph_data)
print("Generated Answer:")
print(answer)

print("Fetched Data from Neo4j:")
print(data)
