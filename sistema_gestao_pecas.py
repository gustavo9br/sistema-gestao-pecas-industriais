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
            font=("Arial", 12, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            padx=8,
            pady=8
        )
        frame.pack(fill=tk.X, pady=(0, 10))
        
        # Canvas para a esteira (tamanho fixo)
        self.canvas = tk.Canvas(
            frame,
            bg="#2e2e3e",
            width=700,
            height=180,
            highlightthickness=2,
            highlightbackground=self.cor_primaria
        )
        self.canvas.pack()
        
        # Desenhar esteira inicial
        self.desenhar_esteira()
        
    def desenhar_esteira(self):
        """Desenha a esteira e suas linhas"""
        self.canvas.delete("esteira")
        
        # Tamanho fixo
        largura = 700
        altura = 180
        
        # Faixa da esteira
        y_centro = altura // 2
        self.canvas.create_rectangle(
            0, y_centro - 40, largura, y_centro + 40,
            fill="#3e3e4e", outline=self.cor_primaria, width=2, tags="esteira"
        )
        
        # Linhas de movimento (simular esteira rolando)
        for i in range(-5, 15):
            x = (i * 80 + self.posicao_esteira) % largura
            self.canvas.create_line(
                x, y_centro - 40, x, y_centro + 40,
                fill="#5e5e6e", width=2, tags="esteira"
        )
        
        # Área de inspeção (scanner)
        x_scanner = largura * 0.7
        self.canvas.create_rectangle(
            x_scanner - 4, y_centro - 50, x_scanner + 4, y_centro + 50,
            fill=self.cor_primaria, outline="", tags="esteira"
        )
        self.canvas.create_text(
            x_scanner, y_centro - 65,
            text="🔍 SCANNER",
            font=("Arial", 9, "bold"),
            fill=self.cor_primaria,
            tags="esteira"
        )
        
        # Saídas (aprovado/reprovado)
        # Saída superior - APROVADO
        self.canvas.create_rectangle(
            largura - 80, 15, largura - 15, 60,
            fill=self.cor_sucesso, outline="", tags="esteira"
        )
        self.canvas.create_text(
            largura - 47, 37,
            text="✅\nOK",
            font=("Arial", 8, "bold"),
            fill=self.cor_fundo,
            tags="esteira"
        )
        
        # Saída inferior - REPROVADO
        self.canvas.create_rectangle(
            largura - 80, altura - 60, largura - 15, altura - 15,
            fill=self.cor_erro, outline="", tags="esteira"
        )
        self.canvas.create_text(
            largura - 47, altura - 37,
            text="❌\nREP",
            font=("Arial", 8, "bold"),
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
        largura = 700
        altura = 180
        y_centro = altura // 2
        x_scanner = largura * 0.7
        
        # Move a peça (mais rápido)
        self.peca_x += 10
        
        # Redesenha a peça
        self.canvas.delete("peca")
        
        # Cor da peça (cores reais)
        cores_validas = {
            'azul': '#4a9eff',
            'verde': '#50c878',
            'vermelho': '#ff4444',
            'amarelo': '#ffcc00',
            'roxo': '#9966cc',
            'laranja': '#ff8c00',
            'rosa': '#ff69b4',
            'marrom': '#8b4513',
            'preto': '#1a1a1a',
            'branco': '#f0f0f0',
            'cinza': '#808080'
        }
        cor_peca = cores_validas.get(self.peca_atual['cor'].lower(), '#888888')
        
        # Tamanho baseado no comprimento (10-20cm = 15-35 pixels de largura)
        comprimento = self.peca_atual['comprimento']
        largura_peca = int(15 + (comprimento - 10) * 2)  # 10cm=15px, 20cm=35px
        largura_peca = max(10, min(largura_peca, 40))  # Limitar entre 10-40px
        
        # Altura baseada no peso (95-105g = 15-25 pixels)
        peso = self.peca_atual['peso']
        altura_peca = int(15 + (peso - 95) * 1)  # 95g=15px, 105g=25px
        altura_peca = max(12, min(altura_peca, 30))  # Limitar entre 12-30px
        
        # Desenha a peça (retângulo com dimensões variáveis)
        self.canvas.create_rectangle(
            self.peca_x - largura_peca, y_centro - altura_peca,
            self.peca_x + largura_peca, y_centro + altura_peca,
            fill=cor_peca, outline="#ffffff", width=2, tags="peca"
        )
        
        # Texto: ID e Peso
        self.canvas.create_text(
            self.peca_x, y_centro - 3,
            text=f"#{self.peca_atual['id']}",
            font=("Arial", 8, "bold"),
            fill="#ffffff",
            tags="peca"
        )
        self.canvas.create_text(
            self.peca_x, y_centro + 7,
            text=f"{self.peca_atual['peso']}g",
            font=("Arial", 7),
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
        largura = 700
        altura = 180
        
        feedback = self.canvas.create_text(
            largura // 2, altura // 2 - 50,
            text=texto,
            font=("Arial", 20, "bold"),
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
        """Cria os botões de controle - Menu Interativo"""
        frame = tk.LabelFrame(
            parent,
            text="📋 MENU INTERATIVO",
            font=("Arial", 11, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.X, pady=(0, 10))
        
        # 1. Cadastrar nova peça (MANUAL)
        btn_cadastrar = tk.Button(
            frame,
            text="1. 🔧  Cadastrar Nova Peça",
            font=("Arial", 10, "bold"),
            bg=self.cor_primaria,
            fg=self.cor_fundo,
            command=self.cadastrar_peca_manual,
            cursor="hand2",
            relief=tk.RAISED,
            bd=2,
            anchor="w",
            padx=8,
            height=1
        )
        btn_cadastrar.pack(fill=tk.X, pady=(0, 4))
        
        # 2. Listar peças aprovadas/reprovadas
        btn_listar = tk.Button(
            frame,
            text="2. 📋  Listar Peças Aprovadas/Reprovadas",
            font=("Arial", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            command=self.listar_pecas,
            cursor="hand2",
            relief=tk.GROOVE,
            bd=2,
            anchor="w",
            padx=8,
            height=1
        )
        btn_listar.pack(fill=tk.X, pady=(0, 4))
        
        # 3. Remover peça cadastrada
        btn_remover = tk.Button(
            frame,
            text="3. 🗑   Remover Peça Cadastrada",
            font=("Arial", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            command=self.remover_peca,
            cursor="hand2",
            relief=tk.GROOVE,
            bd=2,
            anchor="w",
            padx=8,
            height=1
        )
        btn_remover.pack(fill=tk.X, pady=(0, 4))
        
        # 4. Listar caixas fechadas
        btn_caixas = tk.Button(
            frame,
            text="4. 📦  Listar Caixas Fechadas",
            font=("Arial", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            command=self.mostrar_caixas,
            cursor="hand2",
            relief=tk.GROOVE,
            bd=2,
            anchor="w",
            padx=8,
            height=1
        )
        btn_caixas.pack(fill=tk.X, pady=(0, 4))
        
        # 5. Gerar relatório final
        btn_relatorio = tk.Button(
            frame,
            text="5. 📊  Gerar Relatório Final",
            font=("Arial", 10, "bold"),
            bg=self.cor_card,
            fg=self.cor_texto,
            command=self.mostrar_relatorio,
            cursor="hand2",
            relief=tk.GROOVE,
            bd=2,
            anchor="w",
            padx=8,
            height=1
        )
        btn_relatorio.pack(fill=tk.X, pady=(0, 8))
        
        # Separador
        tk.Frame(frame, height=1, bg=self.cor_primaria).pack(fill=tk.X, pady=5)
        
        # EXTRA: Gerar peça aleatória (demonstração rápida)
        self.btn_gerar = tk.Button(
            frame,
            text="🎲  DEMO: Gerar Peça Aleatória",
            font=("Arial", 9),
            bg="#45475a",
            fg=self.cor_texto,
            command=self.gerar_peca_aleatoria,
            cursor="hand2",
            relief=tk.FLAT,
            bd=2,
            height=1
        )
        self.btn_gerar.pack(fill=tk.X)
    
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
    
    def cadastrar_peca_manual(self):
        """Abre janela para cadastrar peça manualmente"""
        if self.animacao_ativa:
            messagebox.showwarning("Aguarde", "Aguarde a peça atual terminar o processamento!")
            return
        
        # Cria janela de cadastro
        janela = tk.Toplevel(self.root)
        janela.title("🔧 Cadastrar Nova Peça")
        janela.geometry("420x400")
        janela.configure(bg=self.cor_fundo)
        janela.resizable(False, False)
        
        # Frame principal
        frame = tk.Frame(janela, bg=self.cor_card, padx=15, pady=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        tk.Label(
            frame,
            text="📋 CADASTRAR NOVA PEÇA",
            font=("Arial", 13, "bold"),
            bg=self.cor_card,
            fg=self.cor_primaria
        ).pack(pady=(0, 15))
        
        # ID
        tk.Label(
            frame,
            text=f"ID da Peça: #{self.proximo_id}",
            font=("Arial", 10),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(anchor=tk.W, pady=(0, 8))
        
        # Peso
        tk.Label(
            frame,
            text="Peso (gramas):",
            font=("Arial", 9),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(anchor=tk.W, pady=(3, 0))
        
        entrada_peso = tk.Entry(frame, font=("Arial", 10), width=35)
        entrada_peso.pack(fill=tk.X, pady=(0, 8))
        
        # Cor
        tk.Label(
            frame,
            text="Cor (azul, verde, vermelho, etc):",
            font=("Arial", 9),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(anchor=tk.W, pady=(3, 0))
        
        entrada_cor = tk.Entry(frame, font=("Arial", 10), width=35)
        entrada_cor.pack(fill=tk.X, pady=(0, 8))
        
        # Comprimento
        tk.Label(
            frame,
            text="Comprimento (centímetros):",
            font=("Arial", 9),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(anchor=tk.W, pady=(3, 0))
        
        entrada_comprimento = tk.Entry(frame, font=("Arial", 10), width=35)
        entrada_comprimento.pack(fill=tk.X, pady=(0, 15))
        
        # Função para processar
        def processar_cadastro():
            try:
                peso = float(entrada_peso.get())
                cor = entrada_cor.get().strip()
                comprimento = float(entrada_comprimento.get())
                
                if not cor:
                    messagebox.showerror("Erro", "Preencha a cor!")
                    return
                
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
                
                # Fecha janela
                janela.destroy()
                
                # Inicia animação
                self.peca_x = 50
                self.animacao_ativa = True
                self.animar_esteira()
                self.atualizar_info_peca()
                
            except ValueError:
                messagebox.showerror("Erro", "Peso e comprimento devem ser números!")
        
        # Botões
        frame_btns = tk.Frame(frame, bg=self.cor_card)
        frame_btns.pack(fill=tk.X)
        
        btn_cancelar = tk.Button(
            frame_btns,
            text="Cancelar",
            font=("Arial", 10),
            bg=self.cor_erro,
            fg=self.cor_fundo,
            command=janela.destroy,
            cursor="hand2",
            width=12
        )
        btn_cancelar.pack(side=tk.LEFT, padx=(0, 5))
        
        btn_processar = tk.Button(
            frame_btns,
            text="Processar Peça",
            font=("Arial", 10, "bold"),
            bg=self.cor_primaria,
            fg=self.cor_fundo,
            command=processar_cadastro,
            cursor="hand2",
            width=15
        )
        btn_processar.pack(side=tk.RIGHT)
    
    def listar_pecas(self):
        """Lista todas as peças aprovadas e reprovadas"""
        # Cria janela
        janela = tk.Toplevel(self.root)
        janela.title("📋 Peças Aprovadas e Reprovadas")
        janela.geometry("700x600")
        janela.configure(bg=self.cor_fundo)
        
        # Frame principal com scroll
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
            pady=15,
            wrap=tk.WORD
        )
        texto.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=texto.yview)
        
        # Gera conteúdo
        conteudo = "=" * 70 + "\n"
        conteudo += "  LISTAGEM DE PEÇAS\n"
        conteudo += "=" * 70 + "\n\n"
        
        # Aprovadas
        conteudo += f"✅ PEÇAS APROVADAS ({len(self.pecas_aprovadas)}):\n"
        conteudo += "-" * 70 + "\n"
        
        if self.pecas_aprovadas:
            conteudo += f"{'ID':<6} {'Peso (g)':<12} {'Cor':<15} {'Comprimento (cm)':<18}\n"
            conteudo += "-" * 70 + "\n"
            for peca in self.pecas_aprovadas:
                conteudo += f"#{peca['id']:<5} {peca['peso']:<12.2f} {peca['cor']:<15} {peca['comprimento']:<18.2f}\n"
        else:
            conteudo += "Nenhuma peça aprovada.\n"
        
        conteudo += "\n"
        
        # Reprovadas
        conteudo += f"❌ PEÇAS REPROVADAS ({len(self.pecas_reprovadas)}):\n"
        conteudo += "-" * 70 + "\n"
        
        if self.pecas_reprovadas:
            conteudo += f"{'ID':<6} {'Peso (g)':<12} {'Cor':<15} {'Comprimento (cm)':<18}\n"
            conteudo += "-" * 70 + "\n"
            for peca in self.pecas_reprovadas:
                conteudo += f"#{peca['id']:<5} {peca['peso']:<12.2f} {peca['cor']:<15} {peca['comprimento']:<18.2f}\n"
                conteudo += "       Motivos da reprovação:\n"
                for motivo in peca['motivos_reprovacao']:
                    conteudo += f"       • {motivo}\n"
                conteudo += "\n"
        else:
            conteudo += "Nenhuma peça reprovada.\n"
        
        texto.insert('1.0', conteudo)
        texto.config(state=tk.DISABLED)
    
    def remover_peca(self):
        """Remove uma peça cadastrada"""
        if not self.pecas_cadastradas:
            messagebox.showinfo("Remover Peça", "Não há peças cadastradas no sistema.")
            return
        
        # Cria janela
        janela = tk.Toplevel(self.root)
        janela.title("🗑️ Remover Peça")
        janela.geometry("500x400")
        janela.configure(bg=self.cor_fundo)
        
        # Frame principal
        frame = tk.Frame(janela, bg=self.cor_card, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(
            frame,
            text="🗑️  REMOVER PEÇA CADASTRADA",
            font=("Arial", 14, "bold"),
            bg=self.cor_card,
            fg=self.cor_erro
        ).pack(pady=(0, 15))
        
        # Lista de peças
        tk.Label(
            frame,
            text="Peças cadastradas:",
            font=("Arial", 10),
            bg=self.cor_card,
            fg=self.cor_texto
        ).pack(anchor=tk.W, pady=(0, 5))
        
        # Frame com scroll para lista
        frame_lista = tk.Frame(frame, bg=self.cor_card)
        frame_lista.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        lista = tk.Listbox(
            frame_lista,
            font=("Courier", 9),
            bg="#2e2e3e",
            fg=self.cor_texto,
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE
        )
        lista.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=lista.yview)
        
        # Preencher lista
        for peca in self.pecas_cadastradas:
            status = "APROVADA" if peca['aprovado'] else "REPROVADA"
            texto = f"ID #{peca['id']} | {status} | {peca['peso']}g | {peca['cor']}"
            lista.insert(tk.END, texto)
        
        # Função para remover
        def confirmar_remocao():
            selecao = lista.curselection()
            if not selecao:
                messagebox.showwarning("Atenção", "Selecione uma peça para remover!")
                return
            
            indice = selecao[0]
            peca = self.pecas_cadastradas[indice]
            
            resposta = messagebox.askyesno(
                "Confirmar Remoção",
                f"Tem certeza que deseja remover a peça #{peca['id']}?\n\n"
                f"Peso: {peca['peso']}g\n"
                f"Cor: {peca['cor']}\n"
                f"Comprimento: {peca['comprimento']}cm"
            )
            
            if resposta:
                # Remover das listas
                self.pecas_cadastradas.remove(peca)
                
                if peca in self.pecas_aprovadas:
                    self.pecas_aprovadas.remove(peca)
                elif peca in self.pecas_reprovadas:
                    self.pecas_reprovadas.remove(peca)
                
                # Atualizar estatísticas
                self.atualizar_estatisticas()
                
                messagebox.showinfo("Sucesso", f"Peça #{peca['id']} removida com sucesso!")
                janela.destroy()
        
        # Botões
        frame_btns = tk.Frame(frame, bg=self.cor_card)
        frame_btns.pack(fill=tk.X, pady=(10, 0))
        
        btn_cancelar = tk.Button(
            frame_btns,
            text="Cancelar",
            font=("Arial", 10),
            bg=self.cor_card,
            fg=self.cor_texto,
            command=janela.destroy,
            cursor="hand2",
            width=12
        )
        btn_cancelar.pack(side=tk.LEFT, padx=(0, 5))
        
        btn_remover = tk.Button(
            frame_btns,
            text="Remover Peça",
            font=("Arial", 10, "bold"),
            bg=self.cor_erro,
            fg=self.cor_fundo,
            command=confirmar_remocao,
            cursor="hand2",
            width=15
        )
        btn_remover.pack(side=tk.RIGHT)
    
    def gerar_peca_aleatoria(self):
        """Gera uma peça com dados aleatórios (DEMO)"""
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





