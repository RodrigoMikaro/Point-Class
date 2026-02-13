# Point-Class
Você trabalha como professor de escola. Para facilitar seu trabalho com pontos no plano de coordenadas, você decide criar uma classe correspondente.

Escreva uma classe Point. Seu método __init__ aceita e armazena as coordenadas coordenadas x e y de um ponto. Todas as instâncias criadas devem ser armazenadas na lista points - um atributo da classe Point.

A classe Point deve fornecer os seguintes métodos:

distance_to_origin - retorna a distância do ponto até a origem
distance_to_point - aceita o point e retorna a distância do ponto atual até o point.
distance_to_x_axis - retorna a distância até o eixo X.
distance_to_y_axis - retorna a distância até o eixo Y
Exemplo:

point = Point(3, 4)

point.distance_to_origin() == 5

point_2 = Point(-5, -1)

point.distance_to_point(point_2) == 9.43
point.distance_to_x_axis == 4
point.distance_to_y_axis == 3

find_closest_point - retorna o ponto mais próximo do atual entre outros pontos criados. Se não houver outros pontos, ele retorna None.
point = Point(3, 4)
point_2 = Point(-5, -1)
point_3 = Point(4, 4)
point_4 = Point(1, 1)

closest_point = point.find_closest_point()

(closest_point.x, closest_point.y) == (4, 4)
closest_point is point_3  # True

Se o resultado do método for um número de ponto flutuante, arredonde-o para a segunda casa decimal.

