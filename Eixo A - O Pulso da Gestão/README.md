# Eixo A: O Pulso da Gestão (MPS.BR - GPR)

Este repositório contém as evidências e a auditoria do **Eixo A**, que avalia a maturidade da Gerência de Projetos (GPR) do ScrapeGraphAI, com base nas diretrizes do MPS.BR. Nossa análise focou em como a equipe planeja as entregas, controla os riscos e aprova o código.

## 🔍 1. Arqueologia de Issues (Controle de Escopo)
Investigamos como a equipe lida com novas demandas da comunidade, utilizando como evidência a **Issue #831**.
* **Diagnóstico:** Risco Baixo. 
* **Motivo:** A equipe utiliza templates rigorosos, mantém a discussão técnica focada e entrega exatamente o que foi planejado, blindando o projeto contra a inflação do escopo (Feature Creep).

## ⚠️ 2. Gestão de Riscos Ocultos (Dívida Técnica)
Analisamos como o projeto gerencia pendências estruturais e arquiteturais.
* **Diagnóstico:** Risco Alto.
* **Motivo:** Encontramos diversos marcadores de dívida técnica (comentários `# TODO` e `# FIXME`) escondidos diretamente no código-fonte (ex: `burr_bridge.py`), sem qualquer rastreabilidade no Backlog oficial. Como o sistema depende de APIs pagas de IA, essa falta de controle eleva os riscos operacionais e financeiros.

## 🚀 3. Ritmo de Entrega e Code Review
Avaliamos o fluxo de integração de código (Pull Requests) e a cadência de lançamentos (Releases).
* **Diagnóstico:** Risco Médio.
* **Motivo:** O projeto lança atualizações de forma muito rápida. O problema é que essa agilidade sacrifica a validação técnica: as aprovações de código são muitas vezes superficiais (comentários como "LGTM" - Looks Good To Me), sem discussão profunda ou exigência de testes.

---

## 🛠️ Plano de Resgate (Ações Imediatas)
Para elevar a governança do projeto e mitigar os riscos encontrados, sugerimos:
1. **Automação da Dívida Técnica:** Integrar ferramentas no GitHub Actions para converter automaticamente comentários "TODO" em tarefas rastreáveis no painel de gerência.
2. **Implementação de Circuit Breaker:** Colocar "disjuntores" na comunicação com as APIs de IA para cortar requisições em caso de falhas seguidas, protegendo os custos do usuário.
3. **Governança Estrita de Code Review:** Exigir revisões densas de código e aprovação obrigatória em testes automatizados antes de aceitar qualquer modificação na ramificação principal.
