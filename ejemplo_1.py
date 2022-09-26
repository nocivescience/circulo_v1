from manim import *
import itertools as it
class Balones(VGroup):
    CONFIG={
        'cantidad':12,
        'colors':[RED,ORANGE,GREEN,YELLOW,BLUE_D]
    }
    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        radios=self.get_radios()
        posiciones=self.get_positions()
        circles=self.get_circles(radios,posiciones)
        self.add(circles)
    def get_radios(self):
        return [
            np.random.uniform(.05,.5) for _ in range(self.CONFIG['cantidad'])
        ]
    def get_positions(self):
        return np.array([
            [
                np.random.uniform(-config['frame_width']/2,config['frame_width']/2),
                np.random.uniform(-config['frame_height']/2,config['frame_height']/2)
                ,0]
            for _ in range(self.CONFIG['cantidad'])
        ])
    def get_circles(self,radios,posiciones):
        colors_circles=it.cycle(self.CONFIG['colors'])
        circles=VGroup()
        for radio,pos,i  in zip(radios,posiciones, it.count(1)):
            circle=Circle(radius=radio,color=next(colors_circles)).move_to(pos)
            texto=Tex(i).set_height(radio).move_to(circle.get_center())
            circle.radio=radio
            circle.center=pos
            circle.velocity=np.array([0,5,0])
            circle.set_fill(next(colors_circles),opacity=1)
            circle.set_stroke(BLACK,opacity=0)
            def update_circle(mob,dt):
                if abs(mob.center[1])+mob.radio>config['frame_height']/2:
                    mob.velocity[1]*=-1
                mob.center+=dt*np.random.random()*mob.velocity
                mob.move_to(mob.center)
            texto.set_color(BLACK)
            circle.add(texto)
            circle.add_updater(update_circle)
            circles.add(circle)
        return circles
class BalonScene(Scene):
    def construct(self):
        circles=Balones()
        self.play(Create(circles))
        self.wait(10)