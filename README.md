# BankGraphDB

Graph database project using Neo4j to model banking transactions and relationships between customers, accounts, and merchants.

---

## Project Overview

BankGraphDB demonstrates how graph databases can represent financial transaction networks.
Using Neo4j, this project models relationships between customers, accounts, and merchants to analyze financial interactions.

Graph databases are particularly useful for detecting patterns in complex relationships such as financial fraud, transaction networks, and account connections.

---

## Technologies Used

* Python
* Neo4j
* Cypher Query Language
* CSV datasets

---

## Graph Data Model

This project models financial entities as nodes and relationships.

### Nodes

* Customer
* Account
* Merchant

### Relationships

Customer → OWNS → Account
Account → TRANSFER → Account
Account → PAYMENT → Merchant

---

## Example Cypher Query

Find transfers between accounts:

```cypher
MATCH (a:Account)-[t:TRANSFER]->(b:Account)
RETURN a, b, t
LIMIT 10
```

Find payments to merchants:

```cypher
MATCH (a:Account)-[:PAYMENT]->(m:Merchant)
RETURN a, m
LIMIT 10
```

---

## Dataset

The project uses CSV datasets to populate the graph database:

* customers.csv
* accounts.csv
* merchants.csv
* transactions.csv

---

## Running the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run the script:

```
python BankGraph.py
```

---

## Potential Use Cases

* Fraud detection
* Transaction network analysis
* Financial relationship discovery
* Graph-based financial analytics
