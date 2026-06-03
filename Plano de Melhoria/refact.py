from abc import ABC, abstractmethod

class LLMFactory(ABC):
    @abstractmethod
    def create_model(self, llm_params: dict):
        pass

class DeepSeekFactory(LLMFactory):
    def create_model(self, llm_params: dict):
        from scrapegraphai.models import DeepSeek
        return DeepSeek(**llm_params)

class OpenAIFactory(LLMFactory):
    def create_model(self, llm_params: dict):
        from langchain.chat_models import init_chat_model
        return init_chat_model(**llm_params)

class LLMProviderRegistry:
    def __init__(self):
        self._factories = {
            "deepseek": DeepSeekFactory(),
            "openai": OpenAIFactory(),
        }

    def get_provider(self, provider_name: str, params: dict):
        factory = self._factories.get(provider_name)
        if not factory:
            raise ValueError(f"Provedor {provider_name} não suportado.")
        return factory.create_model(params)

class AbstractGraph:
    def _create_llm(self, llm_config: dict):
        registry = LLMProviderRegistry()
        return registry.get_provider(llm_params["model_provider"], llm_params)
