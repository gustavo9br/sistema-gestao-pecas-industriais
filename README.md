# 🏭 Sistema de Gestão de Peças Industriais

**Interface Gráfica Animada para Controle de Qualidade e Armazenamento**

Sistema de automação digital desenvolvido para resolver problemas de inspeção manual de peças em linhas de produção industrial.

---

## 📋 Descrição do Projeto

Este sistema automatiza o processo de controle de qualidade de peças fabricadas, eliminando atrasos, falhas de conferência e reduzindo custos operacionais.

### Funcionalidades Principais:

✅ **Geração Automática de Peças** - Clique no botão e peças com dados aleatórios são geradas  
✅ **Esteira Industrial Animada** - Visualização realista do processo de produção  
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
   python sistema_gestao_pecas_visual.py
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
│  ⚙️ CONTROLES      │  (histórico das peças processadas)    │
│  🔧 GERAR NOVA     │                                        │
│      PEÇA          │                                        │
│  📊 📦 🗑️         │                                        │
│                    │                                        │
│  📋 PEÇA ATUAL     │                                        │
│  Aguardando...     │                                        │
└────────────────────┴───────────────────────────────────────┘
```

### 1️⃣ Gerar Nova Peça

**Clique no botão grande:** 🔧 **GERAR NOVA PEÇA**

O que acontece:
1. Uma peça com dados aleatórios aparece na esteira
2. A peça se move automaticamente da esquerda para direita
3. Passa pelo **scanner azul** (🔍) que faz a avaliação
4. Sistema exibe resultado com animação:
   - ✅ **APROVADA!** (texto verde grande)
   - ❌ **REPROVADA!** (texto vermelho grande)
5. Peça segue para a saída correspondente
6. Estatísticas são atualizadas automaticamente

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

### 2️⃣ Visualizar Relatório Completo

**Clique no botão:** 📊 **Relatório**

Abre uma janela com informações detalhadas:

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

### 3️⃣ Ver Caixas Fechadas

**Clique no botão:** 📦 **Caixas**

Mostra todas as caixas que foram fechadas automaticamente:
- Cada caixa tem exatamente **10 peças aprovadas**
- Lista os IDs das peças dentro de cada caixa
- Mostra quantas peças estão na caixa atual (em preenchimento)

### 4️⃣ Limpar Sistema

**Clique no botão:** 🗑️ **Limpar**

Remove todos os dados e reinicia o sistema (solicita confirmação antes).

---

## 📊 Entradas e Saídas do Sistema

### Entradas (Automáticas)

O sistema **gera automaticamente** dados aleatórios para cada peça:

**Geração Inteligente:**
- **70% de chance** de gerar peça aprovada (parâmetros dentro dos critérios)
- **30% de chance** de gerar peça com defeitos:
  - Peso fora do padrão (80g a 120g)
  - Cor inválida (vermelho, amarelo, roxo)
  - Comprimento fora do padrão (5cm a 30cm)
  - Ou múltiplos problemas combinados

Isso simula uma linha de produção real onde nem todas as peças são perfeitas.

### Exemplos de Entradas Geradas

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
| `gerar_peca_aleatoria()` | Cria peça com dados aleatórios inteligentes |
| `avaliar_peca()` | Valida se peça atende aos critérios de qualidade |
| `animar_esteira()` | Cria efeito visual de esteira em movimento |
| `mover_peca()` | Move a peça pela linha de produção |
| `armazenar_peca_aprovada()` | Adiciona peça à caixa e gerencia fechamento |
| `mostrar_relatorio()` | Gera relatório completo com estatísticas |
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

**Esteira (Centro-Esquerda):**
- Fundo escuro com linhas em movimento
- Simula esteira industrial rolante
- Peças aparecem e se movem automaticamente

**Scanner (Centro):**
- Barra vertical azul
- Indica ponto de inspeção
- Flash branco ao avaliar peça

**Saídas (Direita):**
- Saída Superior: ✅ APROVADO (verde)
- Saída Inferior: ❌ REPROVADO (vermelho)

**Painel de Controles:**
- Botão principal grande para gerar peças
- Botões secundários: Relatório, Caixas, Limpar

**Painel de Estatísticas:**
- Atualização em tempo real
- Cores intuitivas (verde = bom, vermelho = problema)

**Histórico:**
- Lista das últimas 50 peças processadas
- Formato compacto e legível

### Cores do Sistema

- 🔵 **Azul** (#89b4fa): Elementos interativos, scanner, botões
- 🟢 **Verde** (#a6e3a1): Aprovado, sucesso, estatísticas positivas
- 🔴 **Vermelho** (#f38ba8): Reprovado, erro, alertas
- 🟡 **Amarelo** (#f9e2af): Avisos, peças amarelas
- 🟣 **Roxo** (#cba6f7): Destaques, peças roxas

---

## 🎯 Casos de Teste

### Teste 1: Processamento Básico

**Ação:** Clicar no botão "🔧 GERAR NOVA PEÇA" 5 vezes

**Resultado Esperado:**
- 5 peças são geradas
- Cada uma se move pela esteira
- Sistema avalia automaticamente
- Estatísticas são atualizadas
- Histórico mostra as 5 peças

### Teste 2: Fechamento de Caixa

**Ação:** Continuar gerando peças até fechar uma caixa

**Resultado Esperado:**
- Quando 10 peças aprovadas são atingidas
- Aparece mensagem: "📦 Caixa #1 FECHADA com 10 peças!"
- Contador de caixas fechadas incrementa
- Nova caixa inicia: 0/10

### Teste 3: Relatório com Dados

**Ação:** 
1. Gerar 20 peças
2. Clicar em "📊 Relatório"

**Resultado Esperado:**
- Janela de relatório abre
- Mostra estatísticas completas
- Exibe médias das peças aprovadas
- Lista peças reprovadas com motivos

### Teste 4: Visualização de Caixas

**Ação:**
1. Gerar peças até fechar 2 caixas (20 aprovadas)
2. Clicar em "📦 Caixas"

**Resultado Esperado:**
- Janela mostra 2 caixas fechadas
- Lista IDs das peças em cada caixa
- Mostra status da caixa atual

### Teste 5: Limpeza do Sistema

**Ação:**
1. Gerar várias peças
2. Clicar em "🗑️ Limpar"
3. Confirmar

**Resultado Esperado:**
- Todos os dados são removidos
- Estatísticas voltam a zero
- Histórico é limpo
- Sistema pronto para novo uso

---

## 🌟 Diferenciais do Sistema

### Visual e Intuitivo
✅ Interface gráfica moderna com tema profissional  
✅ Animações suaves que simulam processo real  
✅ Feedback visual instantâneo (cores, mensagens)  

### Automático e Eficiente
✅ Geração automática de peças (não precisa digitar dados)  
✅ Avaliação instantânea de qualidade  
✅ Armazenamento e fechamento de caixas automático  

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

Desenvolvido como projeto acadêmico para a disciplina de **Algoritmos e Lógica de Programação** da **UNIFECAF**.

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
python sistema_gestao_pecas_visual.py

# Clique no botão "GERAR NOVA PEÇA" e veja a mágica acontecer! ✨
```

---

**Sistema de Gestão de Peças Industriais v1.0**  
*Automatizando a indústria com Python* 🐍🏭✨
