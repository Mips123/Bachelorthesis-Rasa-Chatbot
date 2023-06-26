from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from py2neo import Graph, Node, Relationship


class ActionSaveEntitiesToGraph(Action):
    def name(self) -> Text:
        return "action_save_entities_to_graph"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        entities = tracker.get_latest_entity_values("entity")
        relationships = tracker.get_latest_entity_values("relationship")

        save_entities_to_graph(entities, relationships)

        dispatcher.utter_message(text="Entities and relationships have been saved to the graph database.")

        return []


def save_entities_to_graph(entities, relationships):
    try:
        # Verbindung zur Graphdatenbank herstellen
        graph = Graph("bolt://localhost:7687", auth=("neo4j", "Testtest"))

        # Entitäten als Knoten speichern
        for entity in entities:
            node = Node("Entity", name=entity.name, value=entity.value)
            graph.create(node)

        # Beziehungen als Kanten speichern
        for relationship in relationships:
            start_node = Node("Entity", name=relationship.start_entity.name)
            end_node = Node("Entity", name=relationship.end_entity.name)
            edge = Relationship(start_node, relationship.type, end_node)
            graph.create(edge)

        # Erfolgreich gespeichert
        print("Entities and relationships have been saved to the graph database.")

    except Exception as e:
        # Fehler beim Verbindungsaufbau oder Speichern in der Datenbank
        print("An error occurred while saving entities and relationships to the graph database:", str(e))