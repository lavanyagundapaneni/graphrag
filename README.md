# Pure graphrag
This repository contains a Python application that demonstrates how to use Neo4j for graph-based data storage and querying, combined with LangChain's LLM capabilities (using the Ollama LLaMA 2:7b model) to generate answers to questions based on the graph data.

## Features
1. Connect to a Neo4j database and execute queries.
2. Fetch and process data from the graph database.
3. Use LangChain with the Ollama LLaMA model to generate natural language answers based on graph data.
4. using the graph data generate a formatted answer.

## Configuration
1. ### Neo4j Configuration:
   Ensure you have a running instance of Neo4j. Update the Neo4j connection settings in the script with your database credentials:/n
    URI:The address of your Neo4j instance (e.g., bolt://localhost:7687)./n
    Username: Your Neo4j username (default is usually neo4j)./n
    Password: The password for your Neo4j database./n
2. ### Python Environment Setup:
   Install the necessary Python libraries using pip:
   ` pip install langchain_community neo4j `
   
   




