######################
#  Géométrie plane   #
######################
import math
# Objets
class Droite:
    """
    Droite d'équation ax+by+c=0
    """
    def __init__(self,a,b,c):
        self.isHorizontale,self.isVertivcale=False,False
        assert not( a==0 and b==0)
        if a==0: self.isHorizontale=True
        if b==0: self.isVerticale=True 
        self.a,self.b,self.c=a,b,c
    def vecteur_directeur(self):
        """
        Le vecteur directeur de cette Droite
        """
        return Vecteur(-self.b,self.a)
    def vecteur_normal(self):
        """
        Le vecteur orthogonal à cette Droite
        """
        return Vecteur(self.a,self.b)
    def estOrthogonale(self,d):
        """
        Teste l'orthogonalité de cette Droite avec la Droite d
        """
        return produit_scalaire(self.vecteur_directeur(),d.vecteur_orthogonal())==0
    def x (self,y):
        """
        Abcisse x d'un point de la Droite connaissant son ordonnée y
        """
        if self.isHorizontale:
            return None
        else:
            return (-self.b*y-self.c)/self.a
    def droite_normalisée(self):
        """
        Droite identique à cette Droite avec un coéfficient a=1
        """
        if self.isHorizontale:
            return (Droite(0,1,self.c/self.b))
        else:
            return (Droite(1.,self.b/self.a,self.c/self.a))
    def y (self,x):
        """
        Ordonnée y d'un point de la Droite connaissant son abssice x
        """
        if self.isVerticale:
            return None
        else:
            return (-self.a*x-self.c)/self.b
    def contient(self,p):
        """
        Teste si le Point p est sur cette Droite
        """
        return (self.a*p.x + self.b*p.y + self.c) == 0
    def intersection(self,d):
        """
        Point d'intersection de cette Droite avec la droite d
        """
        assert produit_scalaire(self.vecteur_normal(),d.vecteur_directeur())!=0   # droites non parallèles
        D=d.a*self.b-self.a*d.b
        y=(self.a*d.c - d.a*self.c)/D
        x=(-self.c-self.b*y)/self.a
        return Point(x,y)
    def projeté (self,p):
        """
        Point projeté du Point p sur cette Droite
        """    
        return projeté(p,self)
    def affiche(self):
        print ("Droite :",self.a,self.b,self.c)

class Vecteur:
    """
    Vecteur de coordonnées u et v
    """
    def __init__(self,u,v):
        self.u,self.v=u,v
    def vecteur_orthogonal(self):
        """
        Renvoi le vecteur orthogonal à ce Vecteur
        """
        return Vecteur(-self.v,self.u)
    def est_orthogonal (self,v):
        """
        Teste si ce Vecteur est Orthogonal au vecteur v
        """
        return produit_scalaire(self,v.vecteur_orthogonal())==0.
    def affiche(self):
        print ("Vecteur :",self.u,self.v)
    

class Point:
    """
    Point de coordonnées x et y
    """
    def __init__(self,x,y):
        self.x,self.y=x,y
    def droite_point(self,q):
        """
        Droite passant par ce Point et un autre Point q
        """
        assert not((self.x == q.x) and (self.y == q.y)) , (q.x,q.y)
        if self.y != q.y :
            a=1
            b=-(self.x-q.x)/(self.y-q.y)
        else :
            b=1
            a=-(self.y-q.y)/(self.x-q.x)
        c=-a*self.x-b*self.y
        return Droite(a,b,c)
    def droite_vecteur_directeur(self,v):
        """
        Droite passant par ce Point et de Vecteur directeur v
        """
        b=-v.u
        a=v.v
        c=-a*self.x-b*self.y
        return Droite(a,b,c)
    def est_sur(self,d):
        """
        Teste si ce Point est sur la Droite d
        """
        return (d.contient(self))
    def affiche(self):
        print ("Point :",self.x,self.y)
    def projeté(self,d):
        """
        Point projeté de ce Point sur le Droite d
        """
        return projeté(self,d)

class Segment():
    """
    Segment de droite orienté ayant pour début le Point début et pour extémité le Point extrémité
    """
    def __init__(self,début,extrémité):
        self.début,self.extrémité=début,extrémité
    def norme(self):
        return distance(self.début,self.extrémité)
    def vecteur_directeur(self):
        return self.début.droite_point(self.extrémité).vecteur_directeur()
    def vecteur_orthogonal(self):
        return self.vecteur_directeur().vecteur_orthogonal()
    def contient(self,p):
        d=self.début.droite_point(self.extrémité)
        return d.contient(p)
    def est_orthogonal(self,s):
        """
        Teste si ce Segment est orthogonal au Sgement s
        """
        return self.vecteur_directeur().est_orthogonal(s.vecteur.orthogonal())    
    def milieu(self):
        """
        Le Point milieu de ce Segment
        """
        return (Point((self.début.x+self.extrémité.x)/2,(self.début.y+self.extrémité.y)/2))
    def médiatrice(self):
        """
        La Droite médiatrice de ce Segment
        """
        return self.milieu().droite_vecteur_directeur(self.vecteur_orthogonal())
    def affiche(self):
        print ("Segment : ",end="") ; self.début.affiche();  print(" vers ",end=""); self.extrémité.affiche()

class Cercle():
    def __init__(self,centre,rayon):
        self.centre,self.rayon=centre,rayon
    def périmètre(self):
        """
        Périmètre de ce Cercle
        """
        return math.pi*2.*self.rayon
    def surface(self):
        """
        Surface de ce Cercle
        """
        return math.pi*self.rayon*self.rayon
    def contient(self,p):
        """
        Teste si le Point P est à l'intérieur ou sur le bord de ce Cercle
        """
        return distance(self.centre,p)<=self.rayon
    def projeté(self,d):
        """
        Point projeté du centre de ce Cercle sur la Droite d
        """
        return d.projeté(self.centre)
    def distance_centre(self,d):
        """
        Distance de ce Cercle à la Droite d (distance du centre à son Point projeté sur d)
        """
        return distance(self.centre,self.projeté(d))
    def isSécante(self,d):
        """
        Teste si la Droite d est sécante à ce Cercle
        """
        return self.distance_centre(self,d) <= self.rayon

# Fonctions
def projeté(p,d):
    """
    Le Point projeté du Point p sur la Droite d
    """
    vecteur_projection=d.vecteur_normal()
    droite_projection=p.droite_vecteur_directeur(vecteur_projection)
    return d.intersection(droite_projection)
def symétrique_central(pcentre,p):
    """
    Le Point symétrique central du Point P par rapoort au Point pcentre
    """
    return Point(2*pcentre.x-p.x,2*pcentre.y-p.y)
def symétrique_orthogonal(p,d):
    """
    Le Point symétrique orthogonal du Point P par rapport à la Droite d
    """
    return symétrique_central(projeté(p,d),p)
def distance (p,q):
    """
    Distance euclidienne entre les deux Points p et q du plan
    """
    return ((p.x-q.x)**2 + (p.y-q.y)**2)**.5 
def produit_scalaire(v,w):
    """
    Prouit scalaire des deux Vecteurs v et w
    """
    return (v.u*w.u + w.v*w.v)

""""
Droite(1,2,3).vecteur_directeur().affiche()
d1=Point(1,2).droite_point(Point(41,3))
d1.affiche()
print (Point(41,3).est_sur(d1))
print (Point(1,2).est_sur(d1))
print (d1.contient(Point(41,3)))
print (d1.contient(Point(1,2)))
d2=Point(1,4).droite_point(Point(41,3))
print (Point(41,3).est_sur(d2))
print (Point(1,4).est_sur(d2))
d2.affiche()
d1.intersection(d2).affiche()
d2.intersection(d1).affiche()
projeté(Point(75,23),d2).affiche()
symétrique_orthogonal(d2,Point(56,890)).affiche()
print (distance (Point(42,5),Point(67,23)))
print (distance (Point(0,0),Point(1,1)))
Segment(Point(0,0),Point(1,1)).affiche()
Segment(Point(0,0),Point(1,1)).milieu().affiche()
print (distance(Segment(Point(0,0),Point(1,1)).milieu(),Point(0,0)))
"""
p=Point(6,5)  # un Point p
centre=Point(5,1) # un Point centre de symétrie
sym_cent=symétrique_central(centre,p) # le symétrique central par rapport au Point centre
sym_cent.affiche()   
assert distance(p,centre)==distance(sym_cent,centre) 
assert distance(p,sym_cent)==2*distance(p,centre)
assert Segment(p,sym_cent).contient(centre) 
q=Point(11,-8) # un autre Point q
delta=q.droite_point(centre) # la droite passant par les Points q et centre
sym_ortho=symétrique_orthogonal(p,delta) # le symétrique orhtogoal du point p par rapport à la Droite delta
sym_ortho.affiche()
h=Segment(p,sym_ortho).milieu()  # le Point h projeté de du Point p sur la Droite deltat
h.affiche ()
p.projeté(delta).affiche()   # on le vérifie
assert distance(p,sym_ortho)==2*distance(h,p) # on vérifie que delat est la médiatice du Segment(p,sym_ortho)
Segment(p,sym_ortho).médiatrice().droite_normalisée().affiche()
delta.droite_normalisée().affiche()
assert Cercle(Point(0,0),1.).périmètre()==2.*math.pi
assert Cercle(Point(0,0),1.).surface()==math.pi
assert Cercle(Point(0,0),1.).contient(Point(0.5,.5))
assert Cercle(Point(10,10),1.).contient(Point(10.5,9.7))
assert Cercle(centre,distance(centre,p)).contient(p)
assert Cercle(centre,distance(centre,p)).contient(sym_cent)


