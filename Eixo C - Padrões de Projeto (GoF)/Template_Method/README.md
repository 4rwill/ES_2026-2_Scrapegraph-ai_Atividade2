# Padrão Template Method

## Observações da Auditoria: Duplicação Sistêmica
Identificou-se uma duplicação sistêmica nos nós de geração. Eles replicam a mesma lógica de particionamento de texto e tratamento de *timeouts*.

### Arquivos Impactados
- `generate_answer_node.py`
- `generate_answer_csv_node.py`
- `generate_answer_omni_node.py`

## Solução Proposta: Template Method
A aplicação do padrão **Template Method** resolve essa dívida técnica. Ao centralizar o fluxo comum (particionamento, tratamento de erros) em uma classe base única, reduz-se a repetição de código, tornando a arquitetura mais gerenciável e profissional. O padrão aparece pontualmente em algumas partes da hierarquia, mas sua formalização nos nós de geração traria benefícios imediatos.
