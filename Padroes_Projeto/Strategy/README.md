# Padrão Strategy

## Observações da Auditoria
O comportamento configurável na construção de grafos indica claramente um uso de **Strategy**. O grafo troca algoritmos e orquestrações em tempo de execução conforme parâmetros (`html_mode`, `reasoning`, `reattempt`), sem alterar a interface externa.

### Arquivo em Destaque: `smart_scraper_graph.py`
A construção de variações no método `_create_graph()` demonstra a seleção de diferentes orquestrações baseada na configuração.

## Recomendações: O "God Object" e a Solução via Strategy
A classe de busca no arquivo `fetch_node.py` atua como um "God Object", violando a Responsabilidade Única (SRP) ao misturar requisições web, controle de navegadores e parsing de arquivos.

### Proposta
Extrair essas funções para carregadores especialistas (ex: `WebLoader`, `PDFLoader`). A classe principal passa a apenas delegar a execução através de uma interface Strategy, garantindo isolamento e segurança.
