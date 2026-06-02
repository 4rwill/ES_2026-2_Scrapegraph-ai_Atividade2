# Padrão Facade

## Observações da Auditoria: Interface Simples, Orquestração Complexa
Do ponto de vista do consumidor da biblioteca, a API mantém-se extremamente simples: basta instanciar um grafo e chamar o método `run()`.

## Implementação: `base_graph.py`
Internamente, a classe `BaseGraph` atua como uma **Facade**. Ela orquestra a travessia de nós, a resolução condicional, integração com telemetria e o fluxo de dados entre os componentes. O usuário interage com uma interface unificada que oculta toda a complexidade da orquestração dos grafos de processamento.
