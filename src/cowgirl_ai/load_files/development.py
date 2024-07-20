from file_manager import FileManager
from search import Search

vector_id = "vs_BpS14hR5vN5BXZ1SQq5uWMoW"
file_manager = FileManager()

# First find and load files to iterate over
stack = Search()
stack.search('src/cowgirl_ai/load_files', '.py') # Directory with files we want uploaded
loaded_files = stack.data


# This is so fucked. 

# file_manager.delete_all(loaded_files=loaded_files)
# # file_manager.batch_upload(vector_id=vector_id, loaded_files=loaded_files)
# # print(file_manager.list())




