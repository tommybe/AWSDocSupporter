# AWSDocSupporter

## vector_db
Module responsible for creating vector db. db is dumped to the upper directory of md files directory,to 'vectors' subdirectory.
To run, use click command. Example:
```
python path_to/VectorDBCreator_runner.py
--path_to_md_files_dir='path_to_md_files_directory'
--open_ai_api_key='your_api_key'
```

## lmm_questioner
Module responsible for making flask server with LMM questioning service.
Has 2 endpoints to communicate with the server:
 - ```http://<flask_host>:<flask_port>/get_answer/<question>``` to ask question and get answer
 - ```http://<flask_host>:<flask_port>/get_document/<question>``` to ask question and get document with answer

To run, use click command. Example:
```
python aws_doc_supporter/lmm_questioner/question_server.py 
--open_ai_api_key='your_openai_api_key' 
--path_to_vector_db='path_to_md_files_directory' 
--flask_host='0.0.0.0' 
--flask_port=5000
```