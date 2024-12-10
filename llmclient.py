import logging
from abc import ABC, abstractmethod
from typing import Dict, Any

from pydantic import BaseModel, Field

# Configurazione del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LLMClient(ABC):
    """
    Classe astratta che definisce l'interfaccia per l'interazione con i Large Language Models (LLMs).
    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def load_model(self, model_name: str, **kwargs) -> None:
        """
        Carica e configura un LLM.

        Args:
            model_name (str): Nome del modello da caricare.
            **kwargs: Argomenti aggiuntivi per la configurazione del modello.
        """
        pass

    @abstractmethod
    def generate_response(self, prompt: str, user_id: str, **kwargs) -> Dict[str, Any]:  # Aggiunto user_id
        """
        Genera una risposta da un LLM.

        Args:
            prompt (str): Prompt da inviare al modello.
            user_id (str): ID utente per la richiesta.  # Aggiunto user_id
            **kwargs: Argomenti aggiuntivi per la generazione della risposta.

        Returns:
            Dict[str, Any]: Dizionario contenente la risposta e altre informazioni.
        """
        pass

    @abstractmethod
    def handle_error(self, error: Exception) -> None:
        """
        Gestisce gli errori che si verificano durante l'interazione con il modello.

        Args:
            error (Exception): Eccezione che rappresenta l'errore.
        """
        pass

class OpenAIMockClient(LLMClient):
    """
    Simula risposte di un LLM OpenAI.
    """

    def load_model(self, model_name: str, **kwargs) -> None:
        logging.info(f"OpenAIMockClient: Caricamento del modello {model_name} con parametri {kwargs}")

    def generate_response(self, prompt: str, user_id: str, **kwargs) -> Dict[str, Any]:  # Aggiunto user_id
        logging.info(f"OpenAIMockClient: Generazione di una risposta per il prompt '{prompt}' con parametri {kwargs} e user_id {user_id}")  # Aggiunto user_id
        return {"response": "Questa è una risposta simulata da OpenAIMockClient."}

    def handle_error(self, error: Exception) -> None:
        logging.error(f"OpenAIMockClient: Errore: {error}")

class AnthropicMockClient(LLMClient):
    """
    Simula risposte di un LLM Anthropic.
    """

    def load_model(self, model_name: str, **kwargs) -> None:
        logging.info(f"AnthropicMockClient: Caricamento del modello {model_name} con parametri {kwargs}")

    def generate_response(self, prompt: str, user_id: str, **kwargs) -> Dict[str, Any]:  # Aggiunto user_id
        logging.info(f"AnthropicMockClient: Generazione di una risposta per il prompt '{prompt}' con parametri {kwargs} e user_id {user_id}")  # Aggiunto user_id
        return {"response": "Questa è una risposta simulata da AnthropicMockClient."}

    def handle_error(self, error: Exception) -> None:
        logging.error(f"AnthropicMockClient: Errore: {error}")

class GenerateResponseInput(BaseModel):  # Classe Pydantic per la validazione dell'input
    prompt: str = Field(..., description="Prompt da inviare al modello.")
    user_id: str = Field(..., description="ID utente per la richiesta.")
    other_parameters: Dict[str, Any] = Field(default_factory=dict, description="Argomenti aggiuntivi per la generazione della risposta.")

class GenerateResponseOutput(BaseModel):  # Classe Pydantic per la validazione dell'output
    response: str
