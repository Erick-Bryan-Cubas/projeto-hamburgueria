# Projeto Hamburgueria

Este é o projeto final do curso de Desenvolvimento Web. O objetivo é criar uma página de venda para uma hamburgueria, utilizando HTML, CSS e JavaScript.

## Descrição do Projeto

O projeto consiste em desenvolver uma página web para uma hamburgueria, com as seguintes funcionalidades:

- Exibir o logo da hamburgueria.
- Mostrar imagens dos produtos com seus respectivos preços.
- Incluir um botão de contato via WhatsApp.
- Ícones de redes sociais (Instagram e Facebook).
- Botão "Fazer Pedido" que redireciona para a página de pedido.
- Na página de pedido, exibir o cardápio e permitir que o usuário selecione as quantidades desejadas.
- Botão "Finalizar Pedido" que redireciona para uma página de agradecimento, com detalhes do pedido e status de preparação.

## Funcionalidades

1. **Página Inicial**:
   - Logo da hamburgueria.
   - Imagens dos produtos com preços.
   - Botão de contato via WhatsApp.
   - Ícones das redes sociais (Instagram e Facebook).
   - Botão "Fazer Pedido" que redireciona para a página de pedido em uma nova aba.

2. **Página de Pedido**:
   - Exibição do cardápio.
   - Seleção das quantidades desejadas.
   - Cálculo do frete:
     - Frete grátis para compras acima de R$ 80,00.
     - Frete fixo de R$ 15,00 para compras abaixo de R$ 80,00.
   - Botão "Finalizar Pedido" que redireciona para a página de agradecimento em uma nova aba.

3. **Página de Agradecimento**:
   - Agradecimento pela compra.
   - Informações do pedido.
   - Status de preparação com estimativa de tempo para entrega.

## Regras de Negócio

- Todos os redirecionamentos devem abrir em uma nova aba.
- Frete grátis para compras acima de R$ 80,00. Para valores abaixo de R$ 80,00, o frete é fixo de R$ 15,00.

## Estrutura do Projeto

- **index.html**: Página inicial com logo, produtos, preços, botão de contato e ícones de redes sociais.
- **pedido.html**: Página de pedido com cardápio e seleção de quantidades.
- **agradecimento.html**: Página de agradecimento com detalhes do pedido e status de preparação.
- **styles.css**: Arquivo de estilos para a página.
- **script.js**: Arquivo JavaScript para funcionalidades dinâmicas.
