from neo4j import GraphDatabase

def connection_neo4j():
    URI = "neo4j+ssc://281b1681.databases.neo4j.io"
    AUTH = ("neo4j", "_fDF3MorZQTdnu6-GcF0YD7XYcHYzzb6za_5xo7nySE")

    try:
        driver = GraphDatabase.driver(URI, auth=(AUTH))
        session = driver.session()
        print("Conexão com o Neo4j realizada com sucesso!")
        return driver, session
    except Exception as e:
        print(f"Erro ao conectar ao Neo4j: {e}")
        return None