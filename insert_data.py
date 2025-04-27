#!/usr/bin/env python3
"""
MCP Tools - MongoDB Data Insertion Utility

This script provides functions to insert data into MongoDB collections.
It supports single document and batch insertions with validation options.
"""

import sys
from typing import Dict, List, Optional, Union
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import PyMongoError


class MongoDBInserter:
    """A class to handle MongoDB insertion operations."""

    def __init__(self, connection_string: str, db_name: str):
        """
        Initialize the MongoDB connection.
        
        Args:
            connection_string: MongoDB connection URI
            db_name: Name of the database to use
        """
        try:
            self.client = MongoClient(connection_string)
            self.db = self.client[db_name]
            print(f"Connected to MongoDB database: {db_name}")
        except PyMongoError as e:
            print(f"Failed to connect to MongoDB: {e}")
            sys.exit(1)
    
    def get_collection(self, collection_name: str) -> Collection:
        """
        Get a reference to a MongoDB collection.
        
        Args:
            collection_name: Name of the collection
            
        Returns:
            MongoDB collection object
        """
        return self.db[collection_name]
    
    def insert_one(self, collection_name: str, document: Dict) -> Optional[str]:
        """
        Insert a single document into a collection.
        
        Args:
            collection_name: Name of the collection
            document: Document to insert
            
        Returns:
            The inserted document's ID if successful, None otherwise
        """
        try:
            collection = self.get_collection(collection_name)
            result = collection.insert_one(document)
            print(f"Document inserted with ID: {result.inserted_id}")
            return str(result.inserted_id)
        except PyMongoError as e:
            print(f"Error inserting document: {e}")
            return None
    
    def insert_many(self, collection_name: str, documents: List[Dict], 
                   ordered: bool = True) -> Optional[List[str]]:
        """
        Insert multiple documents into a collection.
        
        Args:
            collection_name: Name of the collection
            documents: List of documents to insert
            ordered: If True, insertion stops on first error
            
        Returns:
            List of inserted document IDs if successful, None otherwise
        """
        try:
            collection = self.get_collection(collection_name)
            result = collection.insert_many(documents, ordered=ordered)
            print(f"Inserted {len(result.inserted_ids)} documents")
            return [str(id) for id in result.inserted_ids]
        except PyMongoError as e:
            print(f"Error inserting documents: {e}")
            return None
    
    def upsert_one(self, collection_name: str, filter_query: Dict, 
                  update_data: Dict) -> Optional[str]:
        """
        Update a document or insert it if it doesn't exist.
        
        Args:
            collection_name: Name of the collection
            filter_query: Query to find the document
            update_data: Data to update or insert
            
        Returns:
            The document's ID if successful, None otherwise
        """
        try:
            collection = self.get_collection(collection_name)
            result = collection.update_one(
                filter_query, 
                {"$set": update_data}, 
                upsert=True
            )
            
            if result.upserted_id:
                print(f"Document upserted with ID: {result.upserted_id}")
                return str(result.upserted_id)
            else:
                print(f"Document updated, matched count: {result.matched_count}")
                return "updated"
        except PyMongoError as e:
            print(f"Error upserting document: {e}")
            return None
    
    def close(self):
        """Close the MongoDB connection."""
        if hasattr(self, 'client'):
            self.client.close()
            print("MongoDB connection closed")


def example_usage():
    """Example demonstrating how to use the MongoDBInserter class."""
    # Replace with your MongoDB connection details
    CONNECTION_STRING = "mongodb://localhost:27017/"
    DB_NAME = "mcp_database"
    
    # Initialize the inserter
    inserter = MongoDBInserter(CONNECTION_STRING, DB_NAME)
    
    # Example single document insertion
    doc = {
        "name": "Block Data",
        "id": "minecraft:stone",
        "properties": {
            "hardness": 1.5,
            "resistance": 6.0,
            "tool": "pickaxe"
        },
        "version": "1.19"
    }
    inserter.insert_one("blocks", doc)
    
    # Example batch insertion
    items = [
        {
            "name": "Diamond Pickaxe",
            "id": "minecraft:diamond_pickaxe",
            "durability": 1561,
            "enchantability": 10
        },
        {
            "name": "Golden Apple",
            "id": "minecraft:golden_apple",
            "stackable": True,
            "food_points": 4
        }
    ]
    inserter.insert_many("items", items)
    
    # Example upsert
    filter_query = {"id": "minecraft:dirt"}
    update_data = {
        "name": "Dirt Block",
        "properties": {
            "hardness": 0.5,
            "tool": "shovel"
        },
        "version": "1.19"
    }
    inserter.upsert_one("blocks", filter_query, update_data)
    
    # Close the connection
    inserter.close()


if __name__ == "__main__":
    # This is just an example. In a real application,
    # you might want to parse command line arguments.
    print("This is a MongoDB insertion utility for MCP Tools.")
    print("To use this module, import it in your Python script.")
    print("Example: from insert_data import MongoDBInserter")
    
    # Uncomment to run the example:
    # example_usage()