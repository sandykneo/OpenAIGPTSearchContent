# OpenAIGPTSearchContent
Softwares - 
Need PythonCharm

Azure Portal access-
Need to create 
   Azure Storage service 
   Azure AI Search
   Azure COntiner Registry
   Azure App Service> WebApp and choose Docker Continer. 
Need to create secret key in OpenAI key.

Run the below code in the terminal from top to bottom - 
1.Run 1 - python .\blob.py
2.Run 2 - python .\azurecognitive_search.py
3.Run 3 - streamlit run .\application.py  
4. docker ps
5. docker login <containerregistryname>.azurecr.io --username <XXXX> --password <XXXX>
6. docker build -t <containerregistryname>.azurecr.io/app:v1 .
7. docker push <containerregistryname>.azurecr.io/app:v1
8. docker images

Note - Rename env.json to .env file for it to work
environment.json file content would be used to update the configuration settings in Azure App Service

python -m streamlit run application.py --server.port 8000 --server.address 0.0.0.0
