"""


https://platform.openai.com/docs/assistants/tools/file-search

"""

from src.client import Client

import pandas as pd
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d",
    format="%(levelname)s - %(asctime)s - %(message)s")


class FileManager(Client):
    """
    For iterating over requests with the OpenAI file storage.
    """

    def __init__(self):
        super().__init__()

    def list(self):
        """
        Calls list file method from OpenAI.

        Creates a generator object that iterates over all files
        that persist in authenticated API client.

        Usage::

            >>> file_mgr = FileManager()
        """
        return self.client.files.list()

    def delete_all(self, loaded_files):
        """
        Mass removal of all files associated with an assistant.
        (This helps with maintenance...use with caution)
        """

        logging.info(f"{len(loaded_files)} file(s) are prepped for deletion")
        confirmation = input(
            "Are you sure you want to delete all files? (y/N): ").strip().lower()
        if confirmation == "y":
            for record in loaded_files:
                # API request # TBD Pass on template?
                self.client.files.delete(record)
            logging.info(f"All {len(loaded_files)} records have been deleted")
        else:
            logging.info(f"Deletion canceled")

    def upload(self, file_name, purpose):
        """
        Upload purpose types:
            - assistants
            - assistants_output
            - batch
            - batch_output
            - fine-tune
            - fine-tune-results
            - vision

        https://platform.openai.com/docs/api-reference/files/object
        """
        return self.client.files.create(
            file=open(file_name, "rb"), purpose=purpose)

    def batch_upload(self, vector_id, loaded_files):
        """
        Batch upload files to a specified vector store.
        One vector store can have many files

        Usage::

            >>> file_manager = FileManager()
            >>> vector_id = vector_ids.get('development_vector')
            >>> file_manager.batch_upload(vector_id)

        """

        try:
            self.file_streams = [open(file, "rb") for file in loaded_files]
            self.file_batch = self.client.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_id, files=self.file_streams)
            self.batch_status = self.file_batch.status
            self.batch_file_counts = self.file_batch.file_counts

            logging.info(f"Batch Status: {self.batch_status}")
            logging.info(f"Batch file counts: {self.batch_file_counts}")
            logging.info(f"Upload complete")
        except Exception as err:
            logging.error(f"Houston we have a problem: {err}")


if __name__ == "__main__":
    FileManager()
