#code by top
import pygame
pygame.init()
pygame.display.init()
sx,sy=int(input('x ')),int(input('y '))
pygame.display.set_mode((sx,sy))
screen=pygame.display.get_surface()
screen.fill((255,255,255))
pygame.display.update()
n=int(input('n- '))


def hexagon(t,x,y,r):
    rr=(r*(3**(1/2))/2)
    a=(x,y-r)
    b=(x+rr,y-(r/2))
    c=(x+rr,y+(r/2))
    d=(x,y+r)
    e=(x-rr,y+(r/2))
    f=(x-rr,y-(r/2))
    o=(x,y)
    if t==1:
        pygame.draw.polygon(screen,(255,0,0),[o,f,a,b])
        pygame.draw.polygon(screen,(0,255,0),[o,b,c,d])
        pygame.draw.polygon(screen,(0,0,255),[o,d,e,f])
    elif t==2:
        pygame.draw.polygon(screen,(255,0,0),[o,c,d,e])
        pygame.draw.polygon(screen,(0,255,0),[o,e,f,a])
        pygame.draw.polygon(screen,(0,0,255),[o,a,b,c])
    pygame.display.update()


r=(sx+sy)/6
for i in range(n):
    if i%2==0:
        hexagon(1,sx/2,sy/2,r)
    else:
        hexagon(2,sx/2,sy/2,r)
    r=r/2
