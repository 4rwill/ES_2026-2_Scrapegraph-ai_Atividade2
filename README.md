# Relatório de Contribuição Individual e Rastreabilidade de Pesquisa

**Disciplina:** Engenharia de Software  
**Projeto Analisado:** [Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai)  
**Auditoria Técnica (Vídeo):** [Link](https://drive.google.com/drive/folders/1xMU6NOEZfy4K7-564g1G7WbRA-ra4nd_)
 

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
* **Responsáveis: Rian P. e Arthur Soares** 
* **O que fez:** Estruturou as diretrizes para o Eixo A de Gestão. Para isso, foi estabelecido um padrão de entrega obrigatório baseado no tripé "Evidência, Análise Crítica e Risco", aplicando-o práticos em três subitens fundamentais: o rastreamento do histórico de decisões arquiteturais complexas (Arqueologia de Issues), a investigação de falhas de acoplamento e limites rígidos ocultos no sistema (Gestão de Riscos Ocultos) e a avaliação do impacto da pressa e das automações sobre a qualidade das revisões e do suporte (Ritmo de Entrega e Code Review), finalizando com a elaboração de um roteiro de discurso para a apresentação dos resultados.
* **Onde procurou as informações:** As evidências técnicas e comportamentais da equipe foram extraídas diretamente de discussões e registros específicos da plataforma, incluindo as abas de Issues e Milestones ,além do histórico de Pull Requests para auditar o uso de ferramentas de automação. Por fim, a contextualização teórica e os critérios de maturidade aplicados na análise crítica foram baseados nas normas e boas práticas de governança técnica do modelo MPS.BR (especialmente o Nível F - Garantia da Qualidade).

### 2. Eixo B: Anatomia do Código (SOLID & DRY)
* **Responsável: Eduardo Ferreira e Artur José** 
* **O que fez: Conduziu o Teste de Stress Arquitetural para identificar dívidas técnicas. Diagnosticou violações críticas de Inversão de Dependência (DIP) no instanciamento de LLMs, quebra de Responsabilidade Única (SRP) na classe principal de busca (God Object), e repetição sistêmica de lógica (DRY) nos nós de geração. Com base nos achados, elaborou a proposta de refatoração aplicando padrões de projeto GoF (Factory, Strategy e Template Method).**
* **Onde procurou as informações: A investigação foi feita diretamente no código-fonte do Scrapegraph-ai, rastreando o acoplamento e a coesão nos diretórios centrais de execução. As evidências foram extraídas especificamente das pastas scrapegraphai/graphs/ (com foco no abstract_graph.py) e scrapegraphai/nodes/ (inspecionando o fetch_node.py e os arquivos da família generate_answer).**

  
### 3. Eixo C: Padrões de Projeto (GoF)
* **Responsáveis:** Ângelo Mutti e Iuri Mauricio
* **O que fez:** Conduziu a análise dos padrões de projeto presentes nos arquivos estudados, identificando o uso predominante de Strategy na seleção de diferentes fluxos de execução, além de indícios de Composite composição de pipelines com blocos reutilizáveis. Também avaliou a presença parcial de Template Method nós de geração de resposta, apontando uma oportunidade de melhoria para reduzir duplicação e centralizar etapas comuns, como preparação de prompts, processamento em partes, chamada ao modelo e agregação dos resultados. A análise foi relacionada com os conceitos clássicos dos padrões GoF e comparada com as explicações do Refactoring Guru.
* **Onde procurou as informações:** Grande parte da investigação foi feita nos arquivos smart_scraper_graph.py, search_graph.py, smart_scraper_multi_graph.py, smart_scraper_multi_concat_graph.py, search_link_graph.py, generate_answer_node.py, generate_answer_csv_node.py e generate_answer_omni_node.py. Esses arquivos foram analisados em conjunto com as referências conceituais do Refactoring Guru, usadas para comparar a estrutura encontrada com os padrões Strategy, Composite e Template Method.

### 4. Plano de Resgate Sugerido
* **Responsáveis:** Christian Will e Eduardo Monteiro
* **O que fez:** Realizamos um diagnóstico arquitetural profundo no núcleo do framework ScrapeGraphAI com o objetivo de identificar dívidas técnicas críticas e formular um plano de intervenção estrutural e gerencial. A auditoria focou em sanar problemas severos de acoplamento e repetição de código. Mapeamos uma forte violação do Princípio de Inversão de Dependência (DIP) e a presença de *Vendor Lock-in* na instanciação dos provedores de Inteligência Artificial. Para resolver isso, projetamos a "Refatoração Conceitual I", aplicando o padrão criacional *Factory Method* aliado a um *Registry* dinâmico, o qual documentamos com diagramas de classes UML para ilustrar a nova arquitetura desacoplada. Além disso, estruturamos a "Refatoração Conceitual II", propondo a implementação do padrão comportamental *Template Method* para os nós de geração (família *generate_answer*). Essa solução visa centralizar o fluxo base do algoritmo, mitigando ativamente a duplicação de código (violação do DRY) e facilitando a manutenibilidade.

* **Onde procurou as informações:** O trabalho forense foi extraído diretamente da leitura do código-fonte no repositório oficial do ScrapeGraphAI no GitHub. A inspeção concentrou-se nos módulos principais de orquestração de grafos, dissecando os arquivos de configuração e classes base como `abstract_graph.py` e `smart_scraper_graph.py`. Para fundamentar as soluções arquiteturais e de processos, cruzamos as evidências do código com o enunciado da Atividade 2 da disciplina, além de utilizarmos a literatura técnica consagrada sobre Padrões de Projeto Orientados a Objetos (GoF), os princípios SOLID e as diretrizes oficiais do Guia Geral do MPS.BR, com foco específico nos resultados esperados para a Gerência de Projetos (GPR).
