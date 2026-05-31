# Relatório de Contribuição Individual e Rastreabilidade de Pesquisa

**Disciplina:** Engenharia de Software  
**Projeto Analisado:** [Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)  
**Auditoria Técnica (Vídeo):**  
 

## Integrantes:
* ARTHUR SOARES SANTANA (202400051087)
* ARTUR JOSÉ SOARES SANTOS (202400072372)
* ANGELO DE SOUSA MUTTI (202100045555)
* CHRISTIAN WILL SILVA SANTOS NUNES (202400050796)
* EDUARDO FERREIRA BOMFIM FILHO (202400050811)
* EDUARDO CURCINO MONTEIRO FILHO (202400051102)
* IURI MAURICIO MAIA PEREIRA (202400051120)
* RIAN PURIFICAÇÃO DE OLIVEIRA (202400051013)

---

## Detalhamento das Contribuições por Eixo

### 1. Eixo A: O Pulso da Gestão (MPS.BR - GPR)
* **Responsável:** 
* **O que fez:**
* **Onde procurou as informações:**

### 2. Eixo B: Anatomia do Código (SOLID & DRY)
* **Responsável: Eduardo Ferreira** 
* **O que fez: Conduziu o Teste de Stress Arquitetural para identificar dívidas técnicas. Diagnosticou violações críticas de Inversão de Dependência (DIP) no instanciamento de LLMs, quebra de Responsabilidade Única (SRP) na classe principal de busca (God Object), e repetição sistêmica de lógica (DRY) nos nós de geração. Com base nos achados, elaborou a proposta de refatoração aplicando padrões de projeto GoF (Factory, Strategy e Template Method).**
* **Onde procurou as informações: Onde procurou as informações: A investigação foi feita diretamente no código-fonte do Scrapegraph-ai, rastreando o acoplamento e a coesão nos diretórios centrais de execução. As evidências foram extraídas especificamente das pastas scrapegraphai/graphs/ (com foco no abstract_graph.py) e scrapegraphai/nodes/ (inspecionando o fetch_node.py e os arquivos da família generate_answer).**

  
### 3. Eixo C: Padrões de Projeto (GoF)
* **Responsáveis:**
* **O que fez:** 
* **Onde procurou as informações:**

### 4. Plano de Resgate Sugerido
* **Responsável:** 
* **O que fez:** 
* **Onde procurou as informações:** 
