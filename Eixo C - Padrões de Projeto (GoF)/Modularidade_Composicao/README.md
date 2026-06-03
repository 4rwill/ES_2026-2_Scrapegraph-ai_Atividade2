# Reaproveitamento de Pipeline e Modularidade por Composição

## Observações da Auditoria
O projeto reutiliza blocos de processamento por recombinação. Isso demonstra uma forte tendência à modularidade por composição, o que reduz drasticamente a duplicação de código e facilita a manutenção.

### Arquivos de Evidência
- `search_graph.py`: Reutiliza `SmartScraperGraph` via `GraphIteratorNode`.
- `smart_scraper_multi_graph.py`: Variante que gerencia múltiplos scrapes.
- `smart_scraper_multi_concat_graph.py`: Troca apenas a etapa de agregação/concatenação.
- `search_link_graph.py`: Outro exemplo de reutilização de lógica de busca.

A composição de nós sugere um uso parcial de **Composite**, embora sem a hierarquia recursiva típica e contrato uniforme rigoroso em todos os níveis.
