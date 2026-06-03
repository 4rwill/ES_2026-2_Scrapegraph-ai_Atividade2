# 🛠️ Tópico 4: Plano de Resgate Sugerido

> **Refatoração GoF e Elevando a Maturidade com MPS.BR**

Este diretório consolida os artefatos, códigos de prova de conceito (PoC) e a fundamentação teórica produzidos na etapa final da **Auditoria Forense de Software** do projeto ScrapeGraphAI.

O objetivo principal desta frente é mitigar dívidas técnicas arquiteturais severas no núcleo do sistema, eliminando antipadrões, e propor um roadmap alinhado ao nível G do modelo **MPS.BR** para elevar a maturidade da engenharia de software da equipe mantenedora.

---

## 📂 Estrutura do Diretório e Evidências

Os arquivos a seguir detalham tanto os problemas mapeados na base original de código quanto as provas de conceito das refatorações sugeridas:

### 🚨 Arquivos Analisados (O Problema)
- 📄 **`abstract_graph.py`**: Arquivo base original que evidenciou forte acoplamento na orquestração dos grafos e violação direta do Princípio de Inversão de Dependência (DIP).
- 📄 **`smart_scraper_graph.py`**: O "God Object" da arquitetura. Concentra excessiva responsabilidade no roteamento e configuração de nós, ferindo o Princípio de Responsabilidade Única (SRP).

### 💡 Provas de Conceito (A Solução GoF)
- 🧪 **`refact.py`**: Demonstra a aplicação do padrão criacional **Factory Method** aliado a um **Registry Dinâmico**. Resolve o *Vendor Lock-in* na instanciação de LLMs (OpenAI, DeepSeek, etc.) e isola a lógica de criação de provedores do restante do framework.
- 🧪 **`refact-template-method.py`**: Implementação da superclasse `BaseGenerationNode` focada em mitigar a extrema duplicação de código (violação do DRY) no processamento dos nós de LLM, utilizando o padrão comportamental **Template Method**.

---

## 🎯 Diagnóstico e Ações de Melhoria

A auditoria revelou que, embora o ScrapeGraphAI ofereça um ecossistema valioso e funcional para extração via LLM, seu núcleo arquitetural apresenta riscos de escalabilidade. A tabela abaixo resume as "doenças" e os "remédios" propostos:

| Sintoma (Dívida Técnica) | Causa / Violação | Remédio Proposto (Refatoração) |
| :--- | :--- | :--- |
| **Código Engessado na Instanciação de LLMs** | Acoplamento forte com as bibliotecas provedoras / Violação do DIP | Padrão **Factory Method** + Registry |
| **Duplicação Maciça nos Nós de Geração** | Falta de abstração do fluxo comum / Violação do princípio DRY | Padrão **Template Method** |
| **Classe Central Inflexível (God Object)** | `SmartScraperGraph` orquestra e decide regras de negócio / Violação do SRP | Padrão **Strategy** (Roadmap futuro) |

---

## 📈 Roadmap Gerencial (Alinhamento MPS.BR - Nível G)

Assumindo a liderança técnica deste repositório e visando consolidar as melhorias estruturais propostas acima, o objetivo gerencial inicial é adequar o processo de Gerência de Projetos (GPR). Precisamos garantir que o escopo e os riscos do projeto deixem de ser tratados de forma orgânica e passem a ser monitorados sistematicamente. Considerando também os novos diagnósticos forenses a respeito de duplicação sistêmica, propomos 3 ações prioritárias imediatas:

### 1. Automação do Rastreamento de Dívida Técnica (Gerência de Requisitos e Escopo)
- **Diagnóstico:** Como visto no Eixo A, há marcadores de dívida técnica e integrações frágeis ocultas em comentários de código.
- **Ação:** Implementar automações (ex: `todo-to-issue` no GitHub Actions) para que qualquer marcador inserido no código gere instantaneamente um item rastreável no backlog, visível para o planejamento das próximas releases.

### 2. Blindagem de APIs de IA centralizada via Template Method (Gerência de Riscos)
- **Diagnóstico:** O sistema confia no tratamento primário de repetições, expondo o ciclo de vida da aplicação a instabilidades e falhas silenciosas advindas de provedores externos. Devido à dispersão da infraestrutura em múltiplos nós paralelos redundantes (Eixo B), gerenciar e conter esses riscos operacionais de rede tornava-se inviável.
- **Ação:** Padronizar a implementação do padrão *Circuit Breaker* no fluxo de carregamento das LLMs. Utilizando a nova superclasse de controle arquitetural `BaseGenerationNode`, o acoplamento do disjuntor de segurança é injetado em um único ponto focal comum, cortando conexões instáveis de forma centralizada para mitigar loops de requisições e proteger o consumo financeiro de tokens do usuário final.

### 3. Governança Restrita com Controle Estático de Redundância (Monitoramento e Controle)
- **Diagnóstico:** O ritmo acelerado de entregas da comunidade tem atropelado a validação de arquitetura, gerando aceites superficiais (LGTM) em Pull Requests críticos. Esta falta de restrição permitiu a proliferação direta da cópia massiva de lógica de processamento nos nós de extração.
- **Ação:** Bloquear a injeção direta de código no `main`. Instituir aprovações obrigatórias por múltiplos mantenedores centrais, checagem mandatória por 100% da esteira de testes automatizados e introduzir ferramentas de análise estática de similaridade de código (como detectores de clonagem do SonarQube/Ruff) na esteira de CI/CD para rejeitar commits automáticos que violem os limites de duplicação do princípio DRY.

---

## 🏁 Conclusão

A aplicação cirúrgica dos padrões **Criacionais** e **Comportamentais**, somada a um controle rigoroso de governança técnica baseada no **MPS.BR**, representa o caminho definitivo para garantir a escalabilidade, resiliência e a evolução orgânica do ScrapeGraphAI em ambientes corporativos e de alta demanda.