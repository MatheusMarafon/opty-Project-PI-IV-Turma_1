"""
MongoDB database configuration and connection.
"""

# --- IMPORTS ---
from pymongo import AsyncMongoClient
from pymongo import MongoClient
from typing import Optional


# --- CODE ---
class MongoDBSetup:
    """
    MongoDB connection manager.
    """

    def __init__(self, db_name: str, mongodb_url: str) -> None:
        """
        Initialize MongoDB connection manager.

        :param db_name: Name of the database
        :param mongodb_url: MongoDB connection URL
        """
        self.__db_name = db_name
        self.__mongodb_url = mongodb_url

        self.client: Optional[AsyncMongoClient] = None
        self.__client_sync: Optional[MongoClient] = None

        self.connect_db()
        self.create_indexes()


    def connect_db(self):
        """
        Connect to MongoDB.
        """

        # Get MongoDB URL from config
        mongodb_url = self.__mongodb_url

        # Initialize MongoDB client
        self.client = AsyncMongoClient(mongodb_url)


    def close_db(self):
        """
        Close MongoDB connection.
        """

        # Close the client if it exists
        if self.client:
            self.client.close()


    def get_database(self):
        """
        Get database instance.
        """
        db_name = self.__db_name
        return self.client[db_name]


    def get_collection(self, collection_name: str):
        """
        Get collection instance.

        :param collection_name: Name of the collection
        """
        db = self.get_database()
        return db[collection_name]


    def create_indexes(self):
        """
        Create indexes.
        """
        try:
            # Get MongoDB configuration
            mongodb_url = self.__mongodb_url
            db_name = self.__db_name

            # sync client only for index creation
            self.__client_sync = MongoClient(mongodb_url)

            # Get the database and collection
            db = self.__client_sync[db_name]
            users_collection = db["users"]

            # Create unique indices
            users_collection.create_index("email", unique=True)
            users_collection.create_index("supabase_id", unique=True)

            # Close sync client
            self.__client_sync.close()

        # error occurs during index creation: log warning
        except Exception as e:  # pylint: disable=W0718
            print(f'[WARNING   ] Could not create indexes: {str(e)}')
