# OpenAIGPTSearchContent
Softwares - Need PythonCharm

Azure Portal access- Create the below resources
- Azure Storage service
- Azure AI Search
- Azure Container Registry
- Azure App Service> WebApp and choose Docker Container.
- Create a secret key in the OpenAI key and update the same in the .env file

How to setup -
1. Open the LangChainAzureSearch Folder in Pycharm.
2. Select Base interpreter as 3.11.8 when you receive a prompt. It would include Virtual environment creation as well.
3. Activate the virtual environment -  Pychram Terminal run: .venv\scripts\activate
4. Run: pip install -r requirements.txt

After the setup is complete, run the below code in the terminal from top to bottom - 
- Run 1 - python .\blob.py
- Run 2 - python .\azurecognitive_search.py
- Run 3 - streamlit run .\application.py


Deployment
- docker ps
- docker login yourcontainerregistryname.azurecr.io --username <yourusername> --password <yourpassword>
- docker build -t yourcontainerregistryname.azurecr.io/app:v1 .
- docker push yourcontainerregistryname.azurecr.io/app:v1
- docker images

Note - Rename env.json to .env file for it to work
environment.json file content would be used to update the configuration settings in Azure App Service

startup command - python -m streamlit run application.py --server.port 8000 --server.address 0.0.0.0
