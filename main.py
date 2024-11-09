# Configurações inicias
import pygame
import random

pygame.init()
pygame.display.set_caption('Snake')
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
dt = 0

#cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# parametros da cobrinha
tamanhoQuadrado = 20
velocidadeJogo = 15

def gerarComida():
    comidaX = round(random.randrange(0, largura - tamanhoQuadrado) / 20.0 ) * 20.0
    comidaY = round(random.randrange(0, altura - tamanhoQuadrado) / 20.0 ) * 20.0
    return comidaX, comidaY

def desenharComida(tamanho, comidaX, comidaY):
    pygame.draw.rect(tela, verde, [comidaX, comidaY, tamanho, tamanho])

def desenharCobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])

def desenharPontuacao(pontuacao):
    fonte = pygame.font.SysFont("Melvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelho)
    tela.blit(texto, [1, 1])

def selecionarVelocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidadeX = 0
        velocidadeY = tamanhoQuadrado
    elif tecla == pygame.K_UP:
        velocidadeX = 0
        velocidadeY = - tamanhoQuadrado
    elif tecla == pygame.K_RIGHT:
        velocidadeX = tamanhoQuadrado
        velocidadeY = 0
    elif tecla == pygame.K_LEFT:
        velocidadeX = - tamanhoQuadrado
        velocidadeY = 0

    return velocidadeX, velocidadeY


def rodarJogo():
    fimJogo = False

    x = largura / 2
    y = altura / 2 

    velocidadeX = 0
    velocidadeY = 0

    tamanhoCobra = 1
    pixels = []

    comidaX, comidaY = gerarComida()

    while not fimJogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fimJogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidadeX, velocidadeY = selecionarVelocidade(evento.key)


        # desenharComida
        desenharComida(tamanhoQuadrado, comidaX, comidaY)

        # Atualizar posição da cobra
        x += velocidadeX
        y += velocidadeY

        # desenharCobrinha
        pixels.append([x, y])
        if len(pixels) > tamanhoCobra:
            del pixels[0]

        # se a cobrinha bateu no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fimJogo = True

        desenharCobra(tamanhoQuadrado, pixels)
        desenharPontuacao(tamanhoCobra - 1)


        pygame.display.update()

        # Criar uma nova comida
        if x == comidaX and y == comidaY:
            tamanhoCobra += 1
            comidaX, comidaY = gerarComida()

        dt = relogio.tick(velocidadeJogo)
        # desenharPontuação
        

# Criar loop infinito






# Criar a lógica de terminar o jogo
# o que acontece:
# cobra bateu na parede
# cobra bateu na própria cobra



# Pegar as interações do usuários
# fechar a tela
# apertar a tecla do teclado para mover a cobra

if __name__ == "__main__":
    rodarJogo()