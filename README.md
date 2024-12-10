# datapizza-se-test

Questa libreria fornisce un'interfaccia di base per l'interazione con i Large Language Models (LLMs)

## Setup

*   Assicurarsi di avere Docker Desktop, Python (In questo caso è stato scritto utilizzando come interprete Python 3.12) installati, e nel caso di Docker, che sia aperto
*   Scaricare i file dalla repository o clonarla in locale e crearsi un'alberatura in modo tale da avere i file python e i file accessori all'interno dello spazio di lavoro creato
*   Aprire un terminale dalla folder dove abbiamo creato lo spazio di lavoro e lanciare il comando `docker build -t llmclient .`

## Test

Per testare il funzionamento ci sono due possibilità
*   Tramite lancio del `llmclient_test.py`
*   Tramite docker, utilizzando `docker run llmclient` oppure sfruttando il docker-compose con questo comando `docker-compose up`

NB: Nel secondo caso Docker Desktop deve rimanere attivo

Per l'immediatezza dell'esecuzione, i dati "dinamici" sono stati messi hard-coded all'interno del codice, come ad esempio i nomi dei modelli.

