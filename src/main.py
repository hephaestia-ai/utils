from src.config import vector_ids
from load_files.search import Search
from load_files.file_manager import FileManager
from load_files.vector_manager import VectorManager


# Get vector id for files to be uploaded to
# Development vector is for testing purposes only. 
# Vectors align with different types of assistants, and should be immutable
vector_id = vector_ids.get('development_vector')


# Search a directory for file extensions 
# Add data to variable 'loaded files' to be processed
def loaded_files():

    stack = Search()
    stack.search('src', '.py')
    return stack.data 

    
# Using the file manager to batch upload loaded files 
# to specific vector 
def load_files(vector_id):

    file_manager = FileManager()
    file_manager.batch_upload(vector_id, loaded_files=loaded_files())

# Load a singular file, provide full name and upload purpose
def load_file(file_name, purpose):

    file_manager = FileManager()
    file_manager.upload(file_name, purpose)

def get_load_status(vector_id):

    vector_manager = VectorManager()
    vector_metadata = vector_manager.get_vector_file_counts(vector_id=vector_id)
