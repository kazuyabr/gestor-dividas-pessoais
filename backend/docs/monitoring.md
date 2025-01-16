# Sistema de Monitoramento

## Visão Geral

O sistema de monitoramento foi implementado para fornecer visibilidade sobre o funcionamento da API, registrando logs de acesso, erros e métricas do sistema.

## Configuração

As configurações de monitoramento são controladas através das seguintes variáveis de ambiente:

| Variável | Descrição |
|----------|-----------|
| `LOG_LEVEL` | Nível de log (INFO, ERROR, etc) |
| `LOG_FORMAT` | Formato dos logs (json ou standard) |
| `LOG_DIR` | Diretório onde os logs serão armazenados |
| `ENABLE_ACCESS_LOGS` | Habilita/desabilita logs de acesso |
| `ENABLE_ERROR_LOGS` | Habilita/desabilita logs de erro |

## Logs

O sistema gera dois tipos principais de logs:

### 1. Access Logs

- Registra todas as requisições à API
- Inclui método HTTP, path, status code e tempo de processamento
- Localização: `{LOG_DIR}/access.log`

### 2. Error Logs

- Registra erros e exceções
- Inclui stack trace e informações detalhadas do erro
- Localização: `{LOG_DIR}/error.log`

## Endpoints de Monitoramento

### 1. GET /api/v1/metrics

- Retorna métricas do sistema
- Inclui uso de CPU, memória e disco
- Informações sobre tamanho dos logs
- Versão da API e ambiente

### 2. GET /api/v1/health

- Verifica a saúde da aplicação
- Status atual do sistema
- Tempo de uptime
- Versão da API

## Uso no Windows 11

Para visualizar logs em tempo real:
