# 🏭 Sistema de Gestão de Peças Industriais

**Interface Gráfica Animada para Controle de Qualidade e Armazenamento**

Sistema de automação digital desenvolvido para resolver problemas de inspeção manual de peças em linhas de produção industrial.

---

## 📋 Descrição do Projeto

Este sistema automatiza o processo de controle de qualidade de peças fabricadas, eliminando atrasos, falhas de conferência e reduzindo custos operacionais.

### Funcionalidades Principais:

✅ **Menu Interativo Completo** - 5 opções funcionais conforme requisitos  
✅ **Cadastro Manual de Peças** - Insira peso, cor e comprimento de cada peça  
✅ **Esteira Industrial Animada** - Visualização realista e compacta do processo  
✅ **Representação Visual Inteligente** - Peças mostram cor real e tamanho proporcional  
✅ **Scanner de Qualidade** - Avaliação automática baseada em critérios pré-definidos  
✅ **Feedback Visual Instantâneo** - Cores e mensagens indicam aprovação/reprovação  
✅ **Armazenamento Inteligente** - Caixas fecham automaticamente com 10 peças  
✅ **Estatísticas em Tempo Real** - Acompanhamento de taxas de aprovação e produção  
✅ **Relatórios Completos** - Análises detalhadas com métricas de qualidade  

---

## 🎯 Critérios de Qualidade

Uma peça é **APROVADA** somente se atender **TODOS** os critérios:

| Característica | Especificação |
|---------------|---------------|
| **Peso** | Entre 95g e 105g |
| **Cor** | Azul OU Verde |
| **Comprimento** | Entre 10cm e 20cm |

Se **qualquer** critério falhar, a peça é **REPROVADA** e o sistema informa o motivo específico.

---

## 🚀 Como Executar o Sistema

### Pré-requisitos

- **Python 3.6 ou superior** instalado no computador
- **Tkinter** (já vem incluído com Python, não precisa instalar!)
- Sistema operacional: Windows, Linux ou macOS

### Passo a Passo

1. **Baixe ou clone este repositório:**
   ```bash
   git clone git@github.com:gustavo9br/sistema-gestao-pecas-industriais.git
   cd sistema-gestao-pecas-industriais
   ```

2. **Execute o sistema:**
   ```bash
   python sistema_gestao_pecas.py
   ```

3. **Interface gráfica abrirá automaticamente!**

---

## 🎮 Como Usar o Sistema

### Tela Principal

Quando você executar o programa, verá uma interface gráfica com:

```
┌────────────────────────────────────────────────────────────┐
│  🏭 SISTEMA DE GESTÃO DE PEÇAS INDUSTRIAIS                │
├────────────────────┬───────────────────────────────────────┤
│                    │  📊 ESTATÍSTICAS                      │
│  🏭 LINHA DE       │  Total de Peças: 0                    │
│     PRODUÇÃO       │  ✅ Aprovadas: 0 (0%)                 │
│                    │  ❌ Reprovadas: 0 (0%)                │
│  ═══════════════   │  📦 Caixas Fechadas: 0                │
│        🔍          │  📦 Caixa Atual: 0/10                 │
│  ═══════════════   │                                        │
│                    │  📜 ÚLTIMAS PEÇAS                     │
│  📋 MENU           │  (histórico das peças processadas)    │
│  INTERATIVO        │                                        │
│  1. Cadastrar      │                                        │
│  2. Listar         │                                        │
│  3. Remover        │                                        │
│  4. Caixas         │                                        │
│  5. Relatório      │                                        │
│                    │                                        │
│  📋 PEÇA ATUAL     │                                        │
│  Aguardando...     │                                        │
└────────────────────┴───────────────────────────────────────┘
```

### 1️⃣ Cadastrar Nova Peça

**Clique no botão:** 1. 🔧 **Cadastrar Nova Peça**

O que acontece:
1. Abre janela de cadastro para você inserir:
   - Peso (em gramas)
   - Cor (azul, verde, vermelho, etc.)
   - Comprimento (em centímetros)
2. Ao clicar "Processar Peça", ela aparece na esteira
3. A peça se move automaticamente com:
   - **Cor real** da peça
   - **Tamanho proporcional** (baseado no comprimento e peso)
   - **ID e peso** exibidos na peça
4. Passa pelo **scanner azul** (🔍) que faz a avaliação
5. Sistema exibe resultado com animação:
   - ✅ **APROVADA!** (texto verde)
   - ❌ **REPROVADA!** (texto vermelho)
6. Peça segue para a saída correspondente
7. Estatísticas são atualizadas automaticamente

**Exemplo de Peça Aprovada:**
```
ID: #1
Peso: 100.0g
Cor: azul
Comprimento: 15.0cm

✅ STATUS: APROVADA
```

**Exemplo de Peça Reprovada:**
```
ID: #2
Peso: 120.0g
Cor: vermelho
Comprimento: 25.0cm

❌ STATUS: REPROVADA
Motivos:
• Peso fora do padrão (120.0g)
• Cor inválida ('vermelho')
• Comprimento fora (25.0cm)
```

### 2️⃣ Listar Peças Aprovadas/Reprovadas

**Clique no botão:** 2. 📋 **Listar Peças Aprovadas/Reprovadas**

Abre uma janela mostrando:
- Tabela com todas as peças **aprovadas** (ID, peso, cor, comprimento)
- Tabela com todas as peças **reprovadas** com motivos detalhados

### 3️⃣ Remover Peça Cadastrada

**Clique no botão:** 3. 🗑️ **Remover Peça Cadastrada**

- Lista todas as peças do sistema
- Selecione uma peça para remover
- Confirma antes de excluir

### 4️⃣ Listar Caixas Fechadas

**Clique no botão:** 4. 📦 **Listar Caixas Fechadas**

Mostra todas as caixas que foram fechadas automaticamente:
- Cada caixa tem exatamente **10 peças aprovadas**
- Lista os IDs das peças dentro de cada caixa
- Mostra quantas peças estão na caixa atual (em preenchimento)

### 5️⃣ Gerar Relatório Final

**Clique no botão:** 5. 📊 **Gerar Relatório Final**

Abre uma janela com informações completas e detalhadas:

- **Estatísticas Gerais:**
  - Total de peças cadastradas
  - Percentual de aprovação e reprovação
  
- **Armazenamento:**
  - Número de caixas fechadas
  - Peças na caixa atual
  - Total de peças armazenadas

- **Análise de Peças Aprovadas:**
  - Peso médio
  - Comprimento médio
  - Distribuição de cores (azul vs verde)

- **Peças Reprovadas:**
  - Lista detalhada com motivos de cada reprovação

---

## 📊 Entradas e Saídas do Sistema

### Entradas (Manual)

O sistema permite **cadastro manual** de cada peça através de formulário:

**Dados Solicitados:**
- **Peso** (em gramas) - Ex: 100
- **Cor** (texto livre) - Ex: azul, verde, vermelho, amarelo, etc.
- **Comprimento** (em centímetros) - Ex: 15

**Representação Visual Inteligente:**
- A peça aparece com a **cor real** informada
- **Largura** proporcional ao comprimento (10cm = pequena, 20cm = grande)
- **Altura** proporcional ao peso (95g = fina, 105g = grossa)
- **ID e peso** são exibidos na própria peça durante movimento

### Exemplos de Entradas

**Peça 1 (Aprovada):**
```
Peso: 100.0g
Cor: azul
Comprimento: 15.0cm
```

**Peça 2 (Aprovada - Limites):**
```
Peso: 95.0g
Cor: verde
Comprimento: 10.0cm
```

**Peça 3 (Reprovada - Peso):**
```
Peso: 110.0g
Cor: azul
Comprimento: 15.0cm
→ Motivo: Peso fora do padrão (110.0g - padrão: 95-105g)
```

**Peça 4 (Reprovada - Múltiplos):**
```
Peso: 85.0g
Cor: vermelho
Comprimento: 25.0cm
→ Motivos:
  • Peso fora do padrão (85.0g)
  • Cor inválida ('vermelho')
  • Comprimento fora (25.0cm)
```

### Saídas do Sistema

**No Painel de Informações:**
```
📋 PEÇA EM PROCESSAMENTO
ID: #5
Peso: 102.5g
Cor: verde
Comprimento: 18.2cm

✅ STATUS: APROVADA
```

**Nas Estatísticas:**
```
📊 ESTATÍSTICAS
Total de Peças: 25
✅ Aprovadas: 20 (80.0%)
❌ Reprovadas: 5 (20.0%)
📦 Caixas Fechadas: 2
📦 Caixa Atual: 0/10
```

**No Histórico:**
```
📜 ÚLTIMAS PEÇAS
#025 | ✅ | 100.00g | azul
#024 | ❌ | 120.00g | vermelho
#023 | ✅ |  98.50g | verde
#022 | ✅ | 102.00g | azul
...
```

**No Relatório Completo:**
```
===============================================
  RELATÓRIO COMPLETO
===============================================

📈 ESTATÍSTICAS GERAIS
Total de peças cadastradas: 25
Peças aprovadas: 20 (80.0%)
Peças reprovadas: 5 (20.0%)

📦 ARMAZENAMENTO
Caixas fechadas: 2
Peças na caixa atual: 0/10
Total armazenado: 20

✅ ANÁLISE DAS PEÇAS APROVADAS
Peso médio: 100.25g
Comprimento médio: 15.50cm
Cor azul: 12 peças (60.0%)
Cor verde: 8 peças (40.0%)

❌ PEÇAS REPROVADAS
ID #2: 120.0g, vermelho, 25.0cm
  • Peso fora do padrão (120.0g)
  • Cor inválida ('vermelho')
  • Comprimento fora (25.0cm)
...
```

---

## 🔧 Estrutura Técnica do Sistema

### Tecnologias Utilizadas

- **Python 3.6+** - Linguagem de programação
- **Tkinter** - Interface gráfica (GUI)
- **Canvas** - Renderização de gráficos 2D (esteira, peças, animações)
- **Random** - Geração de dados aleatórios

### Conceitos de Programação Aplicados

✅ **Programação Orientada a Objetos (POO)** - Sistema organizado em classes  
✅ **Estruturas de Dados** - Listas e dicionários para gerenciar peças e caixas  
✅ **Estruturas Condicionais** - Validação de critérios de qualidade  
✅ **Estruturas de Repetição** - Loops para processar múltiplas peças  
✅ **Funções Modulares** - Código organizado em funções especializadas  
✅ **Animação em Tempo Real** - Loops recursivos com `after()`  
✅ **Event Handling** - Tratamento de eventos de botões  
✅ **Canvas Graphics** - Desenho e animação 2D  

### Principais Funções

| Função | Descrição |
|--------|-----------|
| `cadastrar_peca_manual()` | Abre formulário para cadastro de peça |
| `listar_pecas()` | Lista todas as peças aprovadas e reprovadas |
| `remover_peca()` | Remove peça cadastrada do sistema |
| `avaliar_peca()` | Valida se peça atende aos critérios de qualidade |
| `animar_esteira()` | Cria efeito visual de esteira em movimento |
| `mover_peca()` | Move a peça pela linha com tamanho proporcional |
| `armazenar_peca_aprovada()` | Adiciona peça à caixa e gerencia fechamento |
| `mostrar_relatorio()` | Gera relatório completo com estatísticas |
| `mostrar_caixas()` | Exibe todas as caixas fechadas |
| `atualizar_estatisticas()` | Atualiza contadores em tempo real |

---

## 📦 Armazenamento Automático em Caixas

### Como Funciona

1. **Peças aprovadas** vão automaticamente para a **caixa atual**
2. Quando a caixa atinge **10 peças**, ela é **fechada automaticamente**
3. Uma **nova caixa vazia** é iniciada
4. Sistema mostra mensagem: "📦 Caixa #X FECHADA com 10 peças!"

### Exemplo de Fluxo

```
Peça #1 aprovada → Caixa atual: 1/10
Peça #2 aprovada → Caixa atual: 2/10
Peça #3 reprovada → Caixa atual: 2/10 (reprovadas não vão para caixa)
Peça #4 aprovada → Caixa atual: 3/10
...
Peça #10 aprovada → Caixa atual: 10/10
                  → 📦 Caixa #1 FECHADA!
                  → Nova caixa iniciada: 0/10
Peça #11 aprovada → Caixa atual: 1/10
...
```

---

## 🎨 Interface Visual

### Elementos da Tela

**Esteira (Topo):**
- Tamanho fixo e compacto (700x180px)
- Fundo escuro com linhas em movimento
- Simula esteira industrial rolante
- Peças aparecem com cor real e tamanho proporcional

**Scanner (Centro da Esteira):**
- Barra vertical azul
- Indica ponto de inspeção
- Flash branco ao avaliar peça

**Saídas (Direita da Esteira):**
- Saída Superior: ✅ OK (verde)
- Saída Inferior: ❌ REP (vermelho)

**Menu Interativo:**
- 1. Cadastrar Nova Peça
- 2. Listar Peças Aprovadas/Reprovadas
- 3. Remover Peça Cadastrada
- 4. Listar Caixas Fechadas
- 5. Gerar Relatório Final

**Painel de Estatísticas:**
- Atualização em tempo real
- Cores intuitivas (verde = bom, vermelho = problema)

**Histórico:**
- Lista das últimas 50 peças processadas
- Formato compacto e legível

### Cores das Peças (Representação Real)

As peças aparecem na esteira com sua **cor real**:

- 🔵 **Azul** - Peças azuis aparecem em azul real
- 🟢 **Verde** - Peças verdes aparecem em verde real
- 🔴 **Vermelho** - Peças vermelhas aparecem em vermelho real
- 🟡 **Amarelo** - Peças amarelas aparecem em amarelo real
- 🟣 **Roxo** - Peças roxas aparecem em roxo real
- 🟠 **Laranja** - Peças laranjas aparecem em laranja real
- E mais cores suportadas: rosa, marrom, preto, branco, cinza

---

## 🎯 Casos de Teste

### Teste 1: Cadastro e Processamento

**Ação:** 
1. Clicar em "1. Cadastrar Nova Peça"
2. Inserir: Peso=100, Cor=azul, Comprimento=15
3. Clicar "Processar Peça"
4. Repetir 5 vezes com dados variados

**Resultado Esperado:**
- 5 peças são cadastradas e processadas
- Cada uma aparece com cor real e tamanho proporcional
- Peças se movem pela esteira
- Sistema avalia automaticamente no scanner
- Estatísticas são atualizadas
- Histórico mostra as 5 peças

### Teste 2: Fechamento de Caixa

**Ação:** Continuar gerando peças até fechar uma caixa

**Resultado Esperado:**
- Quando 10 peças aprovadas são atingidas
- Aparece mensagem: "📦 Caixa #1 FECHADA com 10 peças!"
- Contador de caixas fechadas incrementa
- Nova caixa inicia: 0/10

### Teste 3: Listagem de Peças

**Ação:** 
1. Cadastrar várias peças
2. Clicar em "2. Listar Peças Aprovadas/Reprovadas"

**Resultado Esperado:**
- Janela mostra tabelas separadas
- Peças aprovadas com todos os dados
- Peças reprovadas com motivos detalhados

### Teste 4: Relatório Completo

**Ação:** 
1. Cadastrar 20 peças
2. Clicar em "5. Gerar Relatório Final"

**Resultado Esperado:**
- Janela de relatório abre
- Mostra estatísticas completas
- Exibe médias das peças aprovadas
- Lista peças reprovadas com motivos

### Teste 5: Visualização de Caixas

**Ação:**
1. Cadastrar peças até fechar 2 caixas (20 aprovadas)
2. Clicar em "4. Listar Caixas Fechadas"

**Resultado Esperado:**
- Janela mostra 2 caixas fechadas
- Lista IDs das peças em cada caixa
- Mostra status da caixa atual

### Teste 6: Remoção de Peça

**Ação:**
1. Cadastrar várias peças
2. Clicar em "3. Remover Peça Cadastrada"
3. Selecionar uma peça
4. Confirmar remoção

**Resultado Esperado:**
- Lista mostra todas as peças cadastradas
- Peça selecionada é removida após confirmação
- Estatísticas são atualizadas automaticamente

---

## 🌟 Diferenciais do Sistema

### Visual e Intuitivo
✅ Interface gráfica moderna com tema profissional  
✅ Animações suaves que simulam processo real  
✅ Feedback visual instantâneo (cores, mensagens)  

### Automático e Eficiente
✅ Menu interativo com todas as funcionalidades exigidas  
✅ Cadastro manual com validação de dados  
✅ Avaliação instantânea de qualidade  
✅ Armazenamento e fechamento de caixas automático  
✅ Representação visual realista (cor e tamanho das peças)  

### Informativo e Completo
✅ Estatísticas atualizadas em tempo real  
✅ Relatórios detalhados com análises  
✅ Histórico de todas as peças processadas  

### Profissional e Escalável
✅ Código organizado com POO  
✅ Interface responsiva e bem estruturada  
✅ Pronto para expansão com sensores IoT, ML, etc.  

---

## 🔮 Possíveis Expansões Futuras

Este sistema é um protótipo funcional. Em um ambiente industrial real, poderia ser expandido com:

### Hardware
- **Sensores IoT:** Balança digital, câmera com IA, sensor laser
- **Atuadores:** Braços robóticos para direcionamento de peças
- **PLCs:** Integração com controladores industriais

### Software
- **Machine Learning:** Previsão de defeitos antes da produção
- **Dashboard Web:** Interface acessível de qualquer lugar
- **Banco de Dados:** Persistência de dados históricos
- **API REST:** Integração com sistemas ERP/MES
- **Relatórios Avançados:** Gráficos, análise preditiva

### Funcionalidades
- **Múltiplas Linhas:** Gerenciar várias esteiras simultaneamente
- **Rastreabilidade:** QR Code em cada peça
- **Alertas:** Notificações quando taxa de reprovação aumentar
- **Manutenção Preditiva:** Prever falhas nos equipamentos

---

## 🎓 Aplicação Pedagógica

Este projeto demonstra conceitos fundamentais de:

- ✅ **Algoritmos e Lógica de Programação**
- ✅ **Estruturas de Dados** (listas, dicionários)
- ✅ **Programação Orientada a Objetos**
- ✅ **Interface Gráfica com Tkinter**
- ✅ **Animações e Gráficos 2D**
- ✅ **Automação Industrial**
- ✅ **Controle de Qualidade**

É uma ponte entre teoria e prática, mostrando como conceitos de programação resolvem problemas reais da indústria.

---

## 👨‍💻 Autor

**Gustavo Martins**  
Aluno da disciplina de **Algoritmos e Lógica de Programação**  
**UNIFECAF** - 2025

---

## 📝 Licença

Este é um projeto acadêmico desenvolvido para fins educacionais.

---

## 🚀 Começe Agora!

```bash
# Clone o repositório
git clone git@github.com:gustavo9br/sistema-gestao-pecas-industriais.git

# Entre na pasta
cd sistema-gestao-pecas-industriais

# Execute o sistema
python sistema_gestao_pecas.py

# Use o menu interativo:
# 1. Cadastre peças manualmente
# 2. Veja peças se movendo na esteira com cor e tamanho reais
# 3. Acompanhe estatísticas em tempo real! ✨
```

---

**Sistema de Gestão de Peças Industriais v1.0**  
*Automatizando a indústria com Python* 🐍🏭✨
