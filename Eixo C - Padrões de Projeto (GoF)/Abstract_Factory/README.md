# Padrão Criacional: Abstract Factory

## Observações da Auditoria: Violação de DIP
A criação concreta de provedores de LLM encontra-se centralizada no método `_create_llm` do arquivo `abstract_graph.py`. O uso de um catálogo manual (`known_providers`) e cadeias condicionais (`if/elif`) para instanciar as classes aumenta o acoplamento e dificulta a adição de novos provedores.

## Recomendação: Abstract Factory
Introduzir uma **Abstract Factory** (ou `LLMFactory`) para encapsular famílias de criação (instância LLM, parâmetros de autenticação, rate limiter). Isso permite o registro dinâmico de fábricas e melhora significativamente a testabilidade e extensibilidade do sistema, respeitando o Princípio da Inversão de Dependência (DIP).
