from neo4j import GraphDatabase
from dotenv import load_dotenv
from pathlib import Path
import os
import csv

#load.env
env_path = Path (__file__).resolve().parent/".env"
load_dotenv(dotenv_path=env_path)

URL = os.getenv("NEO4J_URL_LOCAL")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD_LOCAL")

AUTH = (USERNAME, PASSWORD)

class Neo4jProvider:
    def __init__(self):
        try:
            self.driver = GraphDatabase.driver(URL, auth=AUTH)
            self.driver.verify_connectivity()
            print("Succesfully Connected to Neo4j")
        except Exception as e:
            print("Error Connecting to Neo4j:", e)
            raise

    def closeconnection(self):
        if self.driver:
            self.driver.close()
            print("Connection to Neo4j Closed")

    def create_customers_nodes(self, csv_file):
        with self.driver.session()as session:
            with open(csv_file, 'r', encoding="utf-8") as file:
                reader= csv.DictReader(file)

                for row in reader:
                    session.run(
                        """
                        CREATE (c:Customers {
                            customer_id: $customer_id,
                            name: $name,
                            city: $city
                        })
                        """,
                        customer_id=row["customer_id"],
                        name=row["name"],
                        city=row["city"]
                    )

            print(f"Nodes Customers Created from {csv_file}")

    def create_accounts_nodes(self, csv_file):
        with self.driver.session()as session:
            with open(csv_file, 'r', encoding="utf-8") as file:
                reader= csv.DictReader(file)

                for row in reader:
                    session.run(
                        """
                        CREATE (a:Accounts {
                            account_id: $account_id,
                            account_type: $account_type,
                            balance: $balance
                        })
                        """,
                        account_id = row["account_id"],
                        account_type = row["account_type"],
                        balance = int(row["balance"])
                    )

            print(f"Nodes Accounts Created from {csv_file}")
    
    def create_merchants_nodes(self, csv_file):
        with self.driver.session()as session:
            with open(csv_file, 'r', encoding="utf-8") as file:
                reader= csv.DictReader(file)

                for row in reader:
                    session.run(
                        """
                        CREATE (m:Merchants {
                            merchant_id: $merchant_id,
                            name: $name,
                            category: $category
                        })
                        """,
                        merchant_id = row["merchant_id"],
                        name = row["name"],
                        category = row["category"]
                    )

            print(f"Nodes Merchants Created from {csv_file}")

if __name__ == "__main__":
    neo4j = Neo4jProvider()
    neo4j.create_customers_nodes ("customers.csv")
    neo4j.create_accounts_nodes ("accounts.csv")
    neo4j.create_merchants_nodes ("merchants.csv")
    neo4j.closeconnection()
