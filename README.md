## Hot to run project.

- All model building happens in `NLP_research.ipynb`
- Use [dvc](https://dvc.org/) to manage versions of dataset
  - `pip install 'dvc[gdrive]'`
  - `dvc pull` - to download current dataset to `dataset/`

## Demo

- pull docker image: `docker pull basicec/nlp:latest`
- run docker image: `docker run -p 4242:4242 basicec/nlp:latest`
- try: `curl 'http://localhost:4242/echo?echo=Hello'`