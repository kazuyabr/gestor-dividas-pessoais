# Regras de Autenticação - Keycloak Integration

## Regras para o desenvolvimento
1 - Sempre separe o planejamento em passos distintos
2 - A cada passo me informe nosso progresso
3 - Sempre me informe a quantidade de regras atuais aplicadas
4 - Salve estas regras em um rules_keycloak.md
5 - Manter sempre o que ja funciona e caso haja alteração ou remoção me alerte sobre a possibilidade de erro
6 - Nunca remova importações ja existentes
7 - Sempre faça o import do que você estiver utilizando
8 - Respeite os escopos de variaveis e importação para melhor organização
9 - Sempre revise o código completo para evitar importações no meio do código a fim de não desrespeitar a regra 8
10 - Sempre use comando git flow para iniciar features, fix, releases, entre outros para melhor organizar os commits e versionamento.
11 - itens novos para o python sempre use como gestor de dependencias o uv.py e salve no pyproject.toml e faça sync com requirements e requirements-dev
12 - itens novos para angular sempre use o yarn e salve as novas dependencias através de add do yarn para que isto seja registrado corretamente no package.json .
13 - Para o projeto angular sempre use yarn e sempre crie scripts para encurtar os comandos como por exemplo yarn build:web para compilar para web. Como web é padrão o yarn build tambem sera para web, mas logo teremos outros builds de outros sistemas operacionais e por isso é importante ja organizar deste modo.
14 - Ao informar progresso sempre informe o que ja foi feito e o que ainda falta fazer para que eu tenha uma visão mais aproximada de inicio e fim.
15 - Importantissimo: respeite todas essas regras anteriores quanto novas e as consulte antes de qualquer etapa ou planejamento ou passo que for dar.

## Regras Atuais Identificadas
1. Autenticação via JWT
2. Proteção de rotas no frontend via Guards
3. Interceptação de requisições HTTP para adicionar token
4. Gerenciamento de sessão via localStorage
5. Logout com limpeza de dados locais
6. Redirecionamento pós-login para dashboard
7. Verificação de token expirado
8. Refresh token automático

## Novas Regras com Keycloak
1. Manter compatibilidade com sistema atual
2. Usar OIDC para autenticação
3. Implementar SSO
4. Manter fluxo de autorização existente
5. Preservar dados do usuário atual
