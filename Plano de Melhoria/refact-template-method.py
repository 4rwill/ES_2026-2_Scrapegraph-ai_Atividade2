from abc import ABC, abstractmethod

class BaseGenerationNode(ABC):
    """
    Superclasse abstrata que centraliza a orquestração e tratamento de timeouts.
    """
    def executeNode(self, state):
        docChunks = self.getDocChunks(state)
        promptTemplate = self.getPromptTemplate()
        outputParser = self.getOutputParser()
        
        chainsDict = self.buildChains(docChunks, promptTemplate, outputParser)
        asyncRunner = RunnableParallel(chainsDict)
        
        try:
            batchResults = asyncRunner.invoke({"question": state.get("userPrompt")})
            return self.processMergedResults(state, batchResults)
        except TimeoutError as timeoutException:
            return self.handleTimeoutError(timeoutException)

    @abstractmethod
    def getPromptTemplate(self):
        pass

    @abstractmethod
    def getOutputParser(self):
        pass

class GenerateAnswerCsvNode(BaseGenerationNode):
    def getPromptTemplate(self):
        return PromptTemplate(
            template=TEMPLATE_CHUNKS_CSV_PROMPT,
            inputVariables=["question"]
        )
        
    def getOutputParser(self):
        return self.llmModel.outputParser



