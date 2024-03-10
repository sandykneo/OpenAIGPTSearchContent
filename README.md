# OpenAIGPTSearchContent
Softwares - Need PythonCharm

Azure Portal access-
Need to create 
- Azure Storage service
- Azure AI Search
- Azure COntiner Registry
- Azure App Service> WebApp and choose Docker Continer.
- Need to create secret key in OpenAI key.

Run the below code in the terminal from top to bottom - 
- Run 1 - python .\blob.py
- Run 2 - python .\azurecognitive_search.py
- Run 3 - streamlit run .\application.py
- docker ps
- docker login yourcontainerregistryname.azurecr.io --username <XXXX> --password <XXXX
- docker build -t yourcontainerregistryname.azurecr.io/app:v1 .
- docker push yourcontainerregistryname.azurecr.io/app:v1
- docker images

Note - Rename env.json to .env file for it to work
environment.json file content would be used to update the configuration settings in Azure App Service

startup command - python -m streamlit run application.py --server.port 8000 --server.address 0.0.0.0
