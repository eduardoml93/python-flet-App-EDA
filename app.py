import flet as ft
import pandas as pd
import io
import requests
from typing import Optional
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class EDAApp:
    def __init__(self):
        self.df: Optional[pd.DataFrame] = None
        self.separator = ","
        
    def create_app(self, page: ft.Page):
        # Configurações da página
        page.title = "EDA - Análise Exploratória de Dados"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 20
        page.window_width = 1200
        page.window_height = 800
        page.window_resizable = True
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        # Título principal
        title = ft.Text(
            "📊 EDA - Análise Exploratória de Dados",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_800,
            text_align=ft.TextAlign.CENTER
        )
        
        # Subtítulo
        subtitle = ft.Text(
            "Faça upload de um arquivo CSV ou use um link para análise exploratória",
            size=16,
            color=ft.Colors.GREY_700,
            text_align=ft.TextAlign.CENTER
        )
        
        # Campo de URL
        url_field = ft.TextField(
            label="URL do arquivo CSV",
            hint_text="https://exemplo.com/arquivo.csv",
            value="https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv",
            width=600,
            border_color=ft.Colors.BLUE_200,
        )
        
        # Seletor de separador
        separator_dropdown = ft.Dropdown(
            label="Separador",
            value=",",
            width=150,
            options=[
                ft.dropdown.Option(",", "Vírgula (,)"),
                ft.dropdown.Option(";", "Ponto e vírgula (;)"),
                ft.dropdown.Option("\t", "Tabulação"),
                ft.dropdown.Option("|", "Pipe (|)"),
            ],
            border_color=ft.Colors.BLUE_200,
        )
        
        # Botão de análise
        analyze_button = ft.ElevatedButton(
            "🔍 Analisar Dados",
            on_click=lambda e: self.analyze_data(page, url_field.value, separator_dropdown.value),
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_600,
                padding=20,
            ),
            width=200,
        )
        
        # Container de resultados
        self.results_container = ft.Container(
            content=ft.Text("Os resultados da análise aparecerão aqui...", 
                           color=ft.Colors.GREY_500, size=16),
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.GREY_50,
            border=ft.border.all(1, ft.Colors.GREY_300),
            visible=False
        )
        
        # Layout principal
        main_column = ft.Column(
            controls=[
                title,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                subtitle,
                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                
                # Seção de entrada
                ft.Container(
                    content=ft.Column([
                        ft.Text("📥 Entrada de Dados", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                        ft.Row([
                            url_field,
                            separator_dropdown,
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                        ft.Row([
                            analyze_button
                        ], alignment=ft.MainAxisAlignment.CENTER),
                    ]),
                    padding=30,
                    border_radius=15,
                    bgcolor=ft.Colors.WHITE,
                    border=ft.border.all(2, ft.Colors.BLUE_200),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.Colors.BLUE_100,
                        offset=ft.Offset(0, 5),
                    )
                ),
                
                ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                
                # Container de resultados
                self.results_container,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
        
        page.add(
    ft.Column(
        controls=[main_column],
        scroll=True,
        expand=True,
    )
)
    
    def analyze_data(self, page: ft.Page, url: str, separator: str):
        """Analisa os dados do CSV"""
        try:
            # Mostra loading
            self.results_container.content = ft.ProgressBar(width=400)
            self.results_container.visible = True
            page.update()
            
            # Faz download dos dados
            response = requests.get(url)
            response.raise_for_status()
            
            # Lê o CSV
            csv_content = response.content.decode('utf-8')
            self.df = pd.read_csv(io.StringIO(csv_content), sep=separator)
            
            # Cria a análise
            analysis_content = self.create_analysis_content()
            self.results_container.content = analysis_content
            self.results_container.visible = True
            
            page.update()
            
        except Exception as e:
            error_content = ft.Column([
                ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED, size=48),
                ft.Text(f"Erro ao analisar dados: {str(e)}", 
                       color=ft.Colors.RED, size=16, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            
            self.results_container.content = error_content
            self.results_container.visible = True
            page.update()
    
    def create_analysis_content(self) -> ft.Column:
        """Cria o conteúdo da análise com prévia automática das primeiras linhas"""
        if self.df is None:
            return ft.Text("Nenhum dado para analisar")
        
        # --- Prévia dos dados (10 primeiras linhas) ---
        preview_df = self.df.head(10)
        
        headers = [ft.Text(col, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700) 
                for col in preview_df.columns]
        
        rows = []
        for _, row in preview_df.iterrows():
            row_data = [ft.Text(str(val)[:50] + "..." if len(str(val)) > 50 else str(val), size=12) 
                        for val in row]
            rows.append(row_data)
        
        preview_table = ft.DataTable(
            columns=[ft.DataColumn(header) for header in headers],
            rows=[ft.DataRow(cells=[ft.DataCell(cell) for cell in row]) for row in rows],
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=10,
        )
        
        preview_container = ft.Container(
            content=ft.Column([
                ft.Text("👁️ Prévia das 10 Primeiras Linhas", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.Column(
                    [preview_table],
                    scroll=ft.ScrollMode.AUTO,  # <-- substituindo SingleChildScrollView
                    height=550,
                )
            ]),
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.GREY_50,
            border=ft.border.all(1, ft.Colors.BLUE_200)
        )
        
        # --- Informações básicas ---
        basic_info = ft.Container(
            content=ft.Column([
                ft.Text("📋 Informações Básicas", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                ft.Text(f"📊 Total de registros: {len(self.df):,}", size=16),
                ft.Text(f"📈 Total de colunas: {len(self.df.columns)}", size=16),
                ft.Text(f"💾 Tamanho em memória: {self.df.memory_usage(deep=True).sum() / 1024:.2f} KB", size=16),
            ]),
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.BLUE_200),
        )
        
        # --- Tipos de dados ---
        dtype_info = ft.Container(
            content=ft.Column([
                ft.Text("🔍 Tipos de Dados", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                *[ft.Text(f"• {col}: {dtype}", size=14) for col, dtype in self.df.dtypes.items()],
            ]),
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.BLUE_200),
        )
        
        # --- Estatísticas descritivas ---
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            stats_df = self.df[numeric_cols].describe()
            stats_content = []
            for col in numeric_cols:
                col_stats = stats_df[col]
                stats_content.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"📊 {col}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                            ft.Text(f"• Média: {col_stats['mean']:.2f}", size=14),
                            ft.Text(f"• Mediana: {col_stats['50%']:.2f}", size=14),
                            ft.Text(f"• Desvio padrão: {col_stats['std']:.2f}", size=14),
                            ft.Text(f"• Mín: {col_stats['min']:.2f}", size=14),
                            ft.Text(f"• Máx: {col_stats['max']:.2f}", size=14),
                        ]),
                        padding=15,
                        border_radius=8,
                        bgcolor=ft.Colors.GREEN_50,
                        border=ft.border.all(1, ft.Colors.GREEN_200),
                    )
                )
            
            stats_container = ft.Container(
                content=ft.Column([
                    ft.Text("📈 Estatísticas Descritivas", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                    ft.Row(stats_content, wrap=True, spacing=10),
                ]),
                padding=20,
                border_radius=10,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.BLUE_200),
            )
        else:
            stats_container = ft.Container(
                content=ft.Text("📈 Nenhuma coluna numérica encontrada para estatísticas", color=ft.Colors.GREY_500),
                padding=20,
                border_radius=10,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.BLUE_200),
            )
        
        # --- Colunas categóricas ---
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            cat_content = []
            for col in categorical_cols[:5]:
                unique_vals = self.df[col].value_counts().head(10)
                cat_content.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"🏷️ {col}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                            ft.Text(f"• Valores únicos: {self.df[col].nunique()}", size=14),
                            ft.Text(f"• Top 10 valores:", size=14, weight=ft.FontWeight.BOLD),
                            *[ft.Text(f"  - {val}: {count:,}", size=12) for val, count in unique_vals.items()],
                        ]),
                        padding=15,
                        border_radius=8,
                        bgcolor=ft.Colors.PURPLE_50,
                        border=ft.border.all(1, ft.Colors.PURPLE_200),
                    )
                )
            
            categorical_container = ft.Container(
                content=ft.Column([
                    ft.Text("🏷️ Análise Categórica", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                    ft.Row(cat_content, wrap=True, spacing=10),
                ]),
                padding=20,
                border_radius=10,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.BLUE_200),
            )
        else:
            categorical_container = ft.Container(
                content=ft.Text("🏷️ Nenhuma coluna categórica encontrada", color=ft.Colors.GREY_500),
                padding=20,
                border_radius=10,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.BLUE_200),
            )
        
        # --- Valores nulos ---
        null_counts = self.df.isnull().sum()
        null_content = []
        for col, null_count in null_counts.items():
            if null_count > 0:
                null_percent = (null_count / len(self.df)) * 100
                null_content.append(
                    ft.Text(f"• {col}: {null_count:,} ({null_percent:.1f}%)", size=14, color=ft.Colors.ORANGE_700)
                )
        
        if null_content:
            null_container = ft.Container(
                content=ft.Column([
                    ft.Text("⚠️ Valores Nulos", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700),
                    *null_content,
                ]),
                padding=20,
                border_radius=10,
                bgcolor=ft.Colors.ORANGE_50,
                border=ft.border.all(1, ft.Colors.ORANGE_200),
            )
        else:
            null_container = ft.Container(
                content=ft.Text("✅ Nenhum valor nulo encontrado", color=ft.Colors.GREEN_600, size=16),
                padding=20,
                border_radius=10,
                bgcolor=ft.Colors.GREEN_50,
                border=ft.border.all(1, ft.Colors.GREEN_200),
            )
        
        # --- Monta a coluna final ---
        return ft.Column([
            ft.Text("📊 Resultados da Análise", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800, text_align=ft.TextAlign.CENTER),
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            
            preview_container,
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            
            basic_info,
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            
            dtype_info,
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            
            stats_container,
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            
            categorical_container,
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            
            null_container,
        ], spacing=20)

def main(page: ft.Page):
    app = EDAApp()
    app.create_app(page)

if __name__ == "__main__":
    ft.app(target=main)