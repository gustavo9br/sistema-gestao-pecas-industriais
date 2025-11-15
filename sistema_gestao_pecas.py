"""
Sistema Visual de Gestão de Peças Industriais
Interface Gráfica com Esteira Animada e Controle de Qualidade

Desenvolvido para automação digital na indústria
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import time


class SistemaVisualPecas:
    def __init__(self, root):
        self.root = root
        self.root.title("🏭 Sistema de Gestão de Peças Industriais")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1e1e2e")
        
        # Dados do sistema
        self.pecas_cadastradas = []
        self.pecas_aprovadas = []
        self.pecas_reprovadas = []
        self.caixas_fechadas = []
        self.caixa_atual = []
        self.proximo_id = 1
        
        # Controle de animação
        self.peca_atual = None
        self.animacao_ativa = False
        self.posicao_esteira = 0
        
        # Cores
        self.cor_fundo = "#1e1e2e"
        self.cor_primaria = "#89b4fa"
        self.cor_sucesso = "#a6e3a1"
        self.cor_erro = "#f38ba8"
        self.cor_texto = "#cdd6f4"
        self.cor_card = "#313244"
        
        self.criar_interface()
        
    def criar_interface(self):
        """Cria toda a interface gráfica"""
        
        # ========== CABEÇALHO ==========
        frame_header = tk.Frame(self.root, bg=self.cor_primaria, height=80)
        frame_header.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(
            frame_header,
            text="🏭 SISTEMA DE GESTÃO DE PEÇAS INDUSTRIAIS",
            font=("Arial", 24, "bold"),
            bg=self.cor_primaria,
            fg=self.cor_fundo
        ).pack(pady=20)
        
        # ========== ÁREA PRINCIPAL ==========
        frame_principal = tk.Frame(self.root, bg=self.cor_fundo)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # COLUNA ESQUERDA - Esteira e Controles
        frame_esquerda = tk.Frame(frame_principal, bg=self.cor_fundo)
        frame_esquerda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Área da Esteira
        self.criar_area_esteira(frame_esquerda)
        
        # Controles
        self.criar_controles(frame_esquerda)
        
        # Informações da Peça Atual
        self.criar_info_peca(frame_esquerda)
        
        # COLUNA DIREITA - Estatísticas e Status
        frame_direita = tk.Frame(frame_principal, bg=self.cor_fundo, width=350)
        frame_direita.pack(side=tk.RIGHT, fill=tk.Y)
        frame_direita.pack_propagate(False)
        
        self.criar_estatisticas(frame_direita)
        self.criar_lista_ultimas_pecas(frame_direita)
        
    def criar_area_esteira(self, parent):
        """Cria a área da esteira com animação"""
        frame = tk.LabelFrame(
            parent,
            text="🏭 LINHA DE PRODUÇÃO",
            font=("Arial", 14, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Canvas para a esteira
        self.canvas = tk.Canvas(
            frame,
            bg="#2e2e3e",
            height=300,
            highlightthickness=2,
            highlightbackground=self.cor_primaria
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Desenhar esteira inicial
        self.desenhar_esteira()
        
    def desenhar_esteira(self):
        """Desenha a esteira e suas linhas"""
        self.canvas.delete("esteira")
        
        # Linhas da esteira (efeito de movimento)
        largura = self.canvas.winfo_width() if self.canvas.winfo_width() > 1 else 700
        altura = self.canvas.winfo_height() if self.canvas.winfo_height() > 1 else 300
        
        # Faixa da esteira
        y_centro = altura // 2
        self.canvas.create_rectangle(
            0, y_centro - 50, largura, y_centro + 50,
            fill="#3e3e4e", outline=self.cor_primaria, width=2, tags="esteira"
        )
        
        # Linhas de movimento (simular esteira rolando)
        for i in range(-5, 20):
            x = (i * 80 + self.posicao_esteira) % largura
            self.canvas.create_line(
                x, y_centro - 50, x, y_centro + 50,
                fill="#5e5e6e", width=2, tags="esteira"
            )
        
        # Área de inspeção (scanner)
        x_scanner = largura * 0.7
        self.canvas.create_rectangle(
            x_scanner - 5, y_centro - 60, x_scanner + 5, y_centro + 60,
            fill=self.cor_primaria, outline="", tags="esteira"
        )
        self.canvas.create_text(
            x_scanner, y_centro - 80,
            text="🔍 SCANNER",
            font=("Arial", 10, "bold"),
            fill=self.cor_primaria,
            tags="esteira"
        )
        
        # Saídas (aprovado/reprovado)
        # Saída superior - APROVADO
        self.canvas.create_rectangle(
            largura - 100, 20, largura - 20, 80,
            fill=self.cor_sucesso, outline="", tags="esteira"
        )
        self.canvas.create_text(
            largura - 60, 50,
            text="✅\nAPROVADO",
            font=("Arial", 9, "bold"),
            fill=self.cor_fundo,
            tags="esteira"
        )
        
        # Saída inferior - REPROVADO
        self.canvas.create_rectangle(
            largura - 100, altura - 80, largura - 20, altura - 20,
            fill=self.cor_erro, outline="", tags="esteira"
        )
        self.canvas.create_text(
            largura - 60, altura - 50,
            text="❌\nREPROVADO",
            font=("Arial", 9, "bold"),
            fill=self.cor_fundo,
            tags="esteira"
        )
        
    def animar_esteira(self):
        """Anima a esteira em movimento"""
        if self.animacao_ativa:
            self.posicao_esteira = (self.posicao_esteira + 5) % 80
            self.desenhar_esteira()
            
            # Se tem peça, move ela
            if self.peca_atual and hasattr(self, 'peca_x'):
                self.mover_peca()
            
            self.root.after(50, self.animar_esteira)
    
    def mover_peca(self):
        """Move a peça pela esteira"""
        largura = self.canvas.winfo_width() if self.canvas.winfo_width() > 1 else 700
        altura = self.canvas.winfo_height() if self.canvas.winfo_height() > 1 else 300
        y_centro = altura // 2
        x_scanner = largura * 0.7
        x_final_sucesso = largura - 60
        x_final_erro = largura - 60
        
        # Move a peça
        self.peca_x += 8
        
        # Redesenha a peça
        self.canvas.delete("peca")
        
        # Cor da peça
        cores_validas = {
            'azul': '#89b4fa',
            'verde': '#a6e3a1',
            'vermelho': '#f38ba8',
            'amarelo': '#f9e2af',
            'roxo': '#cba6f7'
        }
        cor_peca = cores_validas.get(self.peca_atual['cor'], '#888888')
        
        # Desenha a peça
        tamanho = 30
        self.canvas.create_rectangle(
            self.peca_x - tamanho, y_centro - tamanho,
            self.peca_x + tamanho, y_centro + tamanho,
            fill=cor_peca, outline="#ffffff", width=2, tags="peca"
        )
        self.canvas.create_text(
            self.peca_x, y_centro,
            text=f"#{self.peca_atual['id']}",
            font=("Arial", 10, "bold"),
            fill="#ffffff",
            tags="peca"
        )
        
        # Verifica se chegou no scanner
        if abs(self.peca_x - x_scanner) < 10 and not self.peca_atual.get('avaliada'):
            self.avaliar_peca_visual()
            self.peca_atual['avaliada'] = True
        
        # Verifica se chegou no final
        if self.peca_x > largura:
            # Peça saiu da esteira
            self.finalizar_peca()
    
    def avaliar_peca_visual(self):
        """Avalia a peça visualmente no scanner"""
        # Flash no scanner
        self.canvas.create_rectangle(
            0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(),
            fill="white", stipple="gray50", tags="flash"
        )
        self.root.after(100, lambda: self.canvas.delete("flash"))
        
        # Avalia a peça
        aprovado, motivos = self.avaliar_peca(
            self.peca_atual['peso'],
            self.peca_atual['cor'],
            self.peca_atual['comprimento']
        )
        
        self.peca_atual['aprovado'] = aprovado
        self.peca_atual['motivos_reprovacao'] = motivos
        
        # Efeito visual de aprovação/reprovação
        if aprovado:
            self.mostrar_feedback("✅ APROVADA!", self.cor_sucesso)
        else:
            self.mostrar_feedback("❌ REPROVADA!", self.cor_erro)
        
        # Atualiza informações
        self.atualizar_info_peca()
    
    def mostrar_feedback(self, texto, cor):
        """Mostra feedback visual na tela"""
        largura = self.canvas.winfo_width() if self.canvas.winfo_width() > 1 else 700
        altura = self.canvas.winfo_height() if self.canvas.winfo_height() > 1 else 300
        
        feedback = self.canvas.create_text(
            largura // 2, altura // 2 - 80,
            text=texto,
            font=("Arial", 32, "bold"),
            fill=cor,
            tags="feedback"
        )
        
        # Remove feedback após 1 segundo
        self.root.after(1000, lambda: self.canvas.delete("feedback"))
    
    def finalizar_peca(self):
        """Finaliza o processamento da peça"""
        # Adiciona às listas
        self.pecas_cadastradas.append(self.peca_atual)
        
        if self.peca_atual['aprovado']:
            self.pecas_aprovadas.append(self.peca_atual)
            self.armazenar_peca_aprovada(self.peca_atual)
        else:
            self.pecas_reprovadas.append(self.peca_atual)
        
        # Atualiza estatísticas
        self.atualizar_estatisticas()
        self.adicionar_historico(self.peca_atual)
        
        # Limpa a peça
        self.peca_atual = None
        self.animacao_ativa = False
        self.canvas.delete("peca")
        
        # Reabilita botão
        self.btn_gerar.config(state=tk.NORMAL)
    
    def criar_controles(self, parent):
        """Cria os botões de controle"""
        frame = tk.LabelFrame(
            parent,
            text="⚙️ CONTROLES",
            font=("Arial", 12, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            padx=15,
            pady=15
        )
        frame.pack(fill=tk.X, pady=(0, 10))
        
        # Botão principal - Gerar Peça
        self.btn_gerar = tk.Button(
            frame,
            text="🔧 GERAR NOVA PEÇA",
            font=("Arial", 14, "bold"),
            bg=self.cor_primaria,
            fg=self.cor_fundo,
            command=self.gerar_peca_aleatoria,
            height=2,
            cursor="hand2",
            relief=tk.RAISED,
            bd=3
        )
        self.btn_gerar.pack(fill=tk.X, pady=(0, 10))
        
        # Frame para botões secundários
        frame_btns = tk.Frame(frame, bg=self.cor_card)
        frame_btns.pack(fill=tk.X)
        
        # Botão Relatório
        btn_relatorio = tk.Button(
            frame_btns,
            text="📊 Relatório",
            font=("Arial", 11),
            bg=self.cor_card,
            fg=self.cor_texto,
            command=self.mostrar_relatorio,
            cursor="hand2",
            relief=tk.GROOVE,
            bd=2
        )
        btn_relatorio.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        # Botão Caixas
        btn_caixas = tk.Button(
            frame_btns,
            text="📦 Caixas",
            font=("Arial", 11),
            bg=self.cor_card,
            fg=self.cor_texto,
            command=self.mostrar_caixas,
            cursor="hand2",
            relief=tk.GROOVE,
            bd=2
        )
        btn_caixas.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        # Botão Limpar
        btn_limpar = tk.Button(
            frame_btns,
            text="🗑️ Limpar",
            font=("Arial", 11),
            bg=self.cor_erro,
            fg=self.cor_fundo,
            command=self.limpar_sistema,
            cursor="hand2",
            relief=tk.GROOVE,
            bd=2
        )
        btn_limpar.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    def criar_info_peca(self, parent):
        """Cria área de informações da peça atual"""
        self.frame_info = tk.LabelFrame(
            parent,
            text="📋 PEÇA EM PROCESSAMENTO",
            font=("Arial", 12, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            padx=15,
            pady=15
        )
        self.frame_info.pack(fill=tk.X)
        
        self.label_info = tk.Label(
            self.frame_info,
            text="Aguardando nova peça...",
            font=("Arial", 11),
            bg=self.cor_card,
            fg=self.cor_texto,
            justify=tk.LEFT
        )
        self.label_info.pack(anchor=tk.W)
    
    def criar_estatisticas(self, parent):
        """Cria painel de estatísticas"""
        frame = tk.LabelFrame(
            parent,
            text="📊 ESTATÍSTICAS",
            font=("Arial", 12, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            padx=15,
            pady=15
        )
        frame.pack(fill=tk.X, pady=(0, 10))
        
        # Total
        self.label_total = self.criar_label_stat(frame, "Total de Peças:", "0")
        
        # Aprovadas
        frame_aprovadas = tk.Frame(frame, bg=self.cor_card)
        frame_aprovadas.pack(fill=tk.X, pady=5)
        
        tk.Label(
            frame_aprovadas,
            text="✅ Aprovadas:",
            font=("Arial", 10),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(side=tk.LEFT)
        
        self.label_aprovadas = tk.Label(
            frame_aprovadas,
            text="0 (0%)",
            font=("Arial", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_sucesso
        )
        self.label_aprovadas.pack(side=tk.RIGHT)
        
        # Reprovadas
        frame_reprovadas = tk.Frame(frame, bg=self.cor_card)
        frame_reprovadas.pack(fill=tk.X, pady=5)
        
        tk.Label(
            frame_reprovadas,
            text="❌ Reprovadas:",
            font=("Arial", 10),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(side=tk.LEFT)
        
        self.label_reprovadas = tk.Label(
            frame_reprovadas,
            text="0 (0%)",
            font=("Arial", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_erro
        )
        self.label_reprovadas.pack(side=tk.RIGHT)
        
        # Separador
        tk.Frame(frame, height=2, bg=self.cor_primaria).pack(fill=tk.X, pady=10)
        
        # Caixas
        self.label_caixas = self.criar_label_stat(frame, "📦 Caixas Fechadas:", "0")
        self.label_caixa_atual = self.criar_label_stat(frame, "📦 Caixa Atual:", "0/10")
    
    def criar_label_stat(self, parent, texto, valor):
        """Cria um label de estatística"""
        frame_stat = tk.Frame(parent, bg=self.cor_card)
        frame_stat.pack(fill=tk.X, pady=5)
        
        tk.Label(
            frame_stat,
            text=texto,
            font=("Arial", 10),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(side=tk.LEFT)
        
        label_valor = tk.Label(
            frame_stat,
            text=valor,
            font=("Arial", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_primaria
        )
        label_valor.pack(side=tk.RIGHT)
        
        return label_valor
    
    def criar_lista_ultimas_pecas(self, parent):
        """Cria lista das últimas peças processadas"""
        frame = tk.LabelFrame(
            parent,
            text="📜 ÚLTIMAS PEÇAS",
            font=("Arial", 12, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        self.listbox_historico = tk.Listbox(
            frame,
            font=("Courier", 9),
            bg="#2e2e3e",
            fg=self.cor_texto,
            selectbackground=self.cor_primaria,
            yscrollcommand=scrollbar.set,
            relief=tk.FLAT
        )
        self.listbox_historico.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox_historico.yview)
    
    # ========== LÓGICA DO SISTEMA ==========
    
    def gerar_peca_aleatoria(self):
        """Gera uma peça com dados aleatórios"""
        if self.animacao_ativa:
            return
        
        # Desabilita botão
        self.btn_gerar.config(state=tk.DISABLED)
        
        # Gera dados aleatórios
        # 70% de chance de ser aprovada
        if random.random() < 0.7:
            # Peça aprovada
            peso = random.uniform(95, 105)
            cor = random.choice(['azul', 'verde'])
            comprimento = random.uniform(10, 20)
        else:
            # Peça com algum problema
            opcao = random.randint(1, 4)
            
            if opcao == 1:  # Problema no peso
                peso = random.choice([random.uniform(80, 94), random.uniform(106, 120)])
                cor = random.choice(['azul', 'verde'])
                comprimento = random.uniform(10, 20)
            elif opcao == 2:  # Problema na cor
                peso = random.uniform(95, 105)
                cor = random.choice(['vermelho', 'amarelo', 'roxo'])
                comprimento = random.uniform(10, 20)
            elif opcao == 3:  # Problema no comprimento
                peso = random.uniform(95, 105)
                cor = random.choice(['azul', 'verde'])
                comprimento = random.choice([random.uniform(5, 9), random.uniform(21, 30)])
            else:  # Múltiplos problemas
                peso = random.uniform(80, 120)
                cor = random.choice(['vermelho', 'amarelo', 'roxo', 'azul', 'verde'])
                comprimento = random.uniform(5, 30)
        
        # Cria a peça
        self.peca_atual = {
            'id': self.proximo_id,
            'peso': round(peso, 2),
            'cor': cor,
            'comprimento': round(comprimento, 2),
            'aprovado': None,
            'motivos_reprovacao': [],
            'avaliada': False
        }
        self.proximo_id += 1
        
        # Inicia animação
        self.peca_x = 50  # Posição inicial
        self.animacao_ativa = True
        self.animar_esteira()
        
        # Atualiza info
        self.atualizar_info_peca()
    
    def avaliar_peca(self, peso, cor, comprimento):
        """
        Avalia se a peça está aprovada
        Retorna: (aprovado: bool, motivos: list)
        """
        motivos = []
        
        if peso < 95 or peso > 105:
            motivos.append(f"Peso fora do padrão ({peso}g)")
        
        cor_lower = cor.lower().strip()
        if cor_lower not in ['azul', 'verde']:
            motivos.append(f"Cor inválida ('{cor}')")
        
        if comprimento < 10 or comprimento > 20:
            motivos.append(f"Comprimento fora ({comprimento}cm)")
        
        return len(motivos) == 0, motivos
    
    def armazenar_peca_aprovada(self, peca):
        """Armazena peça aprovada em caixa"""
        self.caixa_atual.append(peca)
        
        if len(self.caixa_atual) == 10:
            numero_caixa = len(self.caixas_fechadas) + 1
            self.caixas_fechadas.append({
                'numero': numero_caixa,
                'pecas': self.caixa_atual.copy(),
                'quantidade': 10
            })
            
            # Mostra mensagem
            messagebox.showinfo(
                "📦 Caixa Fechada!",
                f"Caixa #{numero_caixa} foi fechada com 10 peças!\n\n"
                f"Total de caixas: {len(self.caixas_fechadas)}"
            )
            
            self.caixa_atual = []
    
    def atualizar_info_peca(self):
        """Atualiza as informações da peça atual"""
        if not self.peca_atual:
            self.label_info.config(text="Aguardando nova peça...")
            return
        
        texto = f"ID: #{self.peca_atual['id']}\n"
        texto += f"Peso: {self.peca_atual['peso']}g\n"
        texto += f"Cor: {self.peca_atual['cor']}\n"
        texto += f"Comprimento: {self.peca_atual['comprimento']}cm\n"
        
        if self.peca_atual.get('avaliada'):
            if self.peca_atual['aprovado']:
                texto += "\n✅ STATUS: APROVADA"
                self.label_info.config(fg=self.cor_sucesso)
            else:
                texto += "\n❌ STATUS: REPROVADA\n"
                texto += "Motivos:\n" + "\n".join(f"• {m}" for m in self.peca_atual['motivos_reprovacao'])
                self.label_info.config(fg=self.cor_erro)
        else:
            texto += "\n⏳ Aguardando avaliação..."
            self.label_info.config(fg=self.cor_texto)
        
        self.label_info.config(text=texto)
    
    def atualizar_estatisticas(self):
        """Atualiza os números das estatísticas"""
        total = len(self.pecas_cadastradas)
        aprovadas = len(self.pecas_aprovadas)
        reprovadas = len(self.pecas_reprovadas)
        
        perc_aprov = (aprovadas / total * 100) if total > 0 else 0
        perc_reprov = (reprovadas / total * 100) if total > 0 else 0
        
        self.label_total.config(text=str(total))
        self.label_aprovadas.config(text=f"{aprovadas} ({perc_aprov:.1f}%)")
        self.label_reprovadas.config(text=f"{reprovadas} ({perc_reprov:.1f}%)")
        self.label_caixas.config(text=str(len(self.caixas_fechadas)))
        self.label_caixa_atual.config(text=f"{len(self.caixa_atual)}/10")
    
    def adicionar_historico(self, peca):
        """Adiciona peça ao histórico"""
        status = "✅" if peca['aprovado'] else "❌"
        texto = f"#{peca['id']:03d} | {status} | {peca['peso']:6.2f}g | {peca['cor']:8s}"
        
        self.listbox_historico.insert(0, texto)
        
        # Limita a 50 itens
        if self.listbox_historico.size() > 50:
            self.listbox_historico.delete(tk.END)
    
    def mostrar_relatorio(self):
        """Mostra janela com relatório completo"""
        if not self.pecas_cadastradas:
            messagebox.showinfo("📊 Relatório", "Nenhuma peça cadastrada ainda!")
            return
        
        # Cria janela de relatório
        janela = tk.Toplevel(self.root)
        janela.title("📊 Relatório Completo")
        janela.geometry("600x500")
        janela.configure(bg=self.cor_fundo)
        
        # Texto do relatório
        texto = tk.Text(
            janela,
            font=("Courier", 10),
            bg=self.cor_card,
            fg=self.cor_texto,
            wrap=tk.WORD,
            padx=15,
            pady=15
        )
        texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Gera relatório
        total = len(self.pecas_cadastradas)
        aprovadas = len(self.pecas_aprovadas)
        reprovadas = len(self.pecas_reprovadas)
        
        perc_aprov = (aprovadas / total * 100) if total > 0 else 0
        perc_reprov = (reprovadas / total * 100) if total > 0 else 0
        
        relatorio = "=" * 60 + "\n"
        relatorio += "  RELATÓRIO COMPLETO - SISTEMA DE GESTÃO DE PEÇAS\n"
        relatorio += "=" * 60 + "\n\n"
        
        relatorio += "📈 ESTATÍSTICAS GERAIS\n"
        relatorio += "-" * 60 + "\n"
        relatorio += f"Total de peças cadastradas: {total}\n"
        relatorio += f"Peças aprovadas: {aprovadas} ({perc_aprov:.1f}%)\n"
        relatorio += f"Peças reprovadas: {reprovadas} ({perc_reprov:.1f}%)\n\n"
        
        relatorio += "📦 ARMAZENAMENTO\n"
        relatorio += "-" * 60 + "\n"
        relatorio += f"Caixas fechadas: {len(self.caixas_fechadas)}\n"
        relatorio += f"Peças na caixa atual: {len(self.caixa_atual)}/10\n"
        relatorio += f"Total armazenado: {len(self.caixas_fechadas) * 10 + len(self.caixa_atual)}\n\n"
        
        if self.pecas_aprovadas:
            peso_medio = sum(p['peso'] for p in self.pecas_aprovadas) / len(self.pecas_aprovadas)
            comp_medio = sum(p['comprimento'] for p in self.pecas_aprovadas) / len(self.pecas_aprovadas)
            
            azul = sum(1 for p in self.pecas_aprovadas if p['cor'].lower() == 'azul')
            verde = sum(1 for p in self.pecas_aprovadas if p['cor'].lower() == 'verde')
            
            relatorio += "✅ ANÁLISE DAS PEÇAS APROVADAS\n"
            relatorio += "-" * 60 + "\n"
            relatorio += f"Peso médio: {peso_medio:.2f}g\n"
            relatorio += f"Comprimento médio: {comp_medio:.2f}cm\n"
            relatorio += f"Cor azul: {azul} ({azul/aprovadas*100:.1f}%)\n"
            relatorio += f"Cor verde: {verde} ({verde/aprovadas*100:.1f}%)\n\n"
        
        if self.pecas_reprovadas:
            relatorio += "❌ PEÇAS REPROVADAS\n"
            relatorio += "-" * 60 + "\n"
            for peca in self.pecas_reprovadas[-10:]:  # Últimas 10
                relatorio += f"\nID #{peca['id']}: {peca['peso']}g, {peca['cor']}, {peca['comprimento']}cm\n"
                for motivo in peca['motivos_reprovacao']:
                    relatorio += f"  • {motivo}\n"
        
        texto.insert('1.0', relatorio)
        texto.config(state=tk.DISABLED)
    
    def mostrar_caixas(self):
        """Mostra janela com as caixas fechadas"""
        if not self.caixas_fechadas:
            messagebox.showinfo("📦 Caixas", "Nenhuma caixa fechada ainda!")
            return
        
        # Cria janela
        janela = tk.Toplevel(self.root)
        janela.title("📦 Caixas Fechadas")
        janela.geometry("500x400")
        janela.configure(bg=self.cor_fundo)
        
        # Frame com scroll
        frame_principal = tk.Frame(janela, bg=self.cor_fundo)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame_principal)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        texto = tk.Text(
            frame_principal,
            font=("Courier", 10),
            bg=self.cor_card,
            fg=self.cor_texto,
            yscrollcommand=scrollbar.set,
            padx=15,
            pady=15
        )
        texto.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=texto.yview)
        
        # Lista caixas
        conteudo = f"📦 TOTAL DE CAIXAS FECHADAS: {len(self.caixas_fechadas)}\n"
        conteudo += f"📦 Peças na caixa atual: {len(self.caixa_atual)}/10\n\n"
        conteudo += "=" * 50 + "\n\n"
        
        for caixa in self.caixas_fechadas:
            conteudo += f"📦 CAIXA #{caixa['numero']}\n"
            conteudo += "-" * 50 + "\n"
            conteudo += f"Quantidade: {caixa['quantidade']} peças\n"
            conteudo += "Peças: " + ", ".join(f"#{p['id']}" for p in caixa['pecas']) + "\n\n"
        
        texto.insert('1.0', conteudo)
        texto.config(state=tk.DISABLED)
    
    def limpar_sistema(self):
        """Limpa todos os dados do sistema"""
        if not self.pecas_cadastradas:
            messagebox.showinfo("🗑️ Limpar", "Sistema já está vazio!")
            return
        
        resposta = messagebox.askyesno(
            "⚠️ Confirmar Limpeza",
            "Tem certeza que deseja limpar TODOS os dados?\n\n"
            "Esta ação não pode ser desfeita!"
        )
        
        if resposta:
            self.pecas_cadastradas = []
            self.pecas_aprovadas = []
            self.pecas_reprovadas = []
            self.caixas_fechadas = []
            self.caixa_atual = []
            self.proximo_id = 1
            self.peca_atual = None
            self.animacao_ativa = False
            
            self.listbox_historico.delete(0, tk.END)
            self.atualizar_estatisticas()
            self.atualizar_info_peca()
            
            messagebox.showinfo("✅ Limpo", "Sistema limpo com sucesso!")


def main():
    """Função principal"""
    root = tk.Tk()
    app = SistemaVisualPecas(root)
    root.mainloop()


if __name__ == "__main__":
    main()





