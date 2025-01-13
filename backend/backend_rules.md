# Regras do Backend

1. **Testes Primeiro**
   - Manter o padrão TDD já estabelecido nos testes existentes
   - Cobertura mínima de 80% conforme configurado no pyproject.toml

2. **Padronização de Código**
   - Documentação em português-BR
   - Commits seguindo conventional commits
   - Manter estrutura de pastas atual (src/routes, src/schemas, etc)

3. **Arquitetura e Segurança**
   - Continuar usando FastAPI com autenticação JWT
   - Manter separação de responsabilidades (routes, schemas, models)
   - Implementar validações de dados com Pydantic

4. **Banco de Dados**
   - Continuar usando SQLAlchemy para operações DB
   - Manter migrations com Alembic para novas alterações
   - Seguir padrão de nomenclatura das tabelas existentes

5. **API e Endpoints**
   - Manter versionamento v1 da API
   - Documentar novos endpoints seguindo padrão OpenAPI existente
   - Implementar tratamento de erros consistente

6. **Regras de Negócio**
   - Validar regras de dívidas na camada service
   - Manter lógica de status de dívidas (Pendente, Pago, Vencida)
   - Implementar validações de datas e valores

7. **Qualidade de Código**
   - Usar typing hints em todas as funções
   - Seguir padrões de nomes já estabelecidos
   - Manter organização modular do código

8. **Monitoramento**
   - Implementar logs para operações críticas
   - Registrar erros de autenticação e validação

Total de regras: 8 categorias principais
