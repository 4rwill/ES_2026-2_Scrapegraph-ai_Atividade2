# Auditoria de Código - Eixo 2 (Anatomia do Código: SOLID & DRY)

Esta pasta contém a análise de maturidade do projeto **Scrapegraph-ai** sob a ótica de engenharia de software (foco em MPS.BR), identificando gargalos arquiteturais que impactam a manutenibilidade e escalabilidade.

## 1. Violação de DIP (Inversão de Dependência)
**Arquivo:** `scrapegraphai/graphs/abstract_graph.py`  
**Problema:** Alto acoplamento com a biblioteca LangChain e provedores específicos. A classe base instacia diretamente implementações concretas de fornecedores em vez de depender de uma abstração.

### Evidência:
```python
if llm_params["model_provider"] not in {"oneapi", "nvidia", "ernie", "deepseek", ...}:
    return init_chat_model(**llm_params)
else:
    model_provider = llm_params.pop("model_provider")
    if model_provider == "clod":
        return CLoD(**llm_params)
    if model_provider == "deepseek":
        return DeepSeek(**llm_params)
    # ... repetição para cada provedor existente
```

---

## 2. God Objects (Violação de SRP - Responsabilidade Única)
**Arquivo:** `scrapegraphai/nodes/fetch_node.py`  
**Problema:** A classe `FetchNode` centraliza lógicas que deveriam estar distribuídas. Ela gerencia requisições HTTP, orquestração de navegadores (Playwright), parsing de arquivos (PDF, CSV) e manipulação de DataFrames.

### Evidência:
```python
handlers = {
    "json_dir": self.handle_directory,
    "pdf": self.handle_file,
    "csv": self.handle_file,
    # ... orquestra diversos tipos de IO no mesmo nó
}

if input_type == "pdf":
    loader = PyPDFLoader(source)
    return loader.load()
elif input_type == "csv":
    import pandas as pd
    return [Document(page_content=str(pd.read_csv(source)))]
```

---

## 3. Violação de DRY (Don't Repeat Yourself)
**Arquivos:** `generate_answer_node.py`, `generate_answer_csv_node.py`, `generate_answer_omni_node.py`  
**Problema:** Duplicação sistêmica da lógica de orquestração de LLMs, processamento em chunks, tratamento de falhas (timeouts) e retentativas entre os diferentes nós de geração.

### Evidência:
```python
# Lógica de chunking e processamento paralelo replicada integralmente em múltiplos arquivos
chains_dict = {}
for i, chunk in enumerate(tqdm(doc, desc="Processing chunks")):
    prompt = PromptTemplate(template=template_chunks_prompt, ...)
    chain_name = f"chunk{i + 1}"
    chains_dict[chain_name] = prompt | self.llm_model
    # ... lógica idêntica repetida em 3+ nós diferentes
```

---

## Resumo da Auditoria
A arquitetura atual prioriza a rapidez na entrega de funcionalidades em detrimento da robustez estrutural. Os principais impactos identificados são:
- **Fragilidade:** Mudanças em bibliotecas externas (ex: Pandas ou PyPDF) podem quebrar o núcleo de busca.
- **Baixa Coesão:** Arquivos com múltiplos tarefas não relacionadas.
- **Dificuldade de Extensão:** Adicionar um novo provedor exige alteração no core da biblioteca.