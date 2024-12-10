# datapizza-se-test

Questa libreria fornisce un'interfaccia di base per l'interazione con i Large Language Models (LLMs)

## Caratteristiche principali

*   **Interfaccia astratta:** La classe astratta `LLMClient` definisce un'interfaccia comune per interagire con diversi LLMs.
*   **Classi mock:** Sono incluse classi mock per OpenAI e Anthropic, che consentono di testare il codice senza dover interagire con i modelli reali.
*   **Gestione degli errori:** La libreria include meccanismi per la gestione degli errori, garantendo la robustezza del codice.
*   **Validazione dell'input:** La libreria utilizza Pydantic per la validazione dell'input, garantendo che i dati inviati ai modelli siano corretti.
*   **Logging:** La libreria utilizza il modulo `logging` per registrare le operazioni eseguite e gli eventuali errori.
*   **Test unitari:** La libreria include una suite di test unitari per verificare il corretto funzionamento dei componenti.
*   **Containerizzazione:** La libreria può essere eseguita in un container Docker, semplificando la distribuzione e il testing.

## Installazione
