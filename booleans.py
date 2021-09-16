import compas
from compas.geometry import Box
from compas.geometry import Sphere
from compas.geometry import Translation
from compas.datastructures import Mesh
from compas.geometry import boolean_union_mesh_mesh
from compas_view2.app import App

box = Box.from_width_height_depth(2, 2, 2)
sphere = Sphere([1, 1, 1], 1)

A = Mesh.from_shape(box)
B = Mesh.from_shape(sphere, u=32, v=32)

A.quads_to_triangles()
B.quads_to_triangles()

V, F = boolean_union_mesh_mesh(A.to_vertices_and_faces(), B.to_vertices_and_faces())

C = Mesh.from_vertices_and_faces(V, F)
C.transform(Translation.from_vector([4, 0, 0]))

data = {}

data['A'] = A
data['B'] = B

compas.json_dump(data, 'booleans.json')

viewer = App()

viewer.add(A, facecolor=(1, 0, 0))
viewer.add(B, facecolor=(0, 1, 0), opacity=0.5)
viewer.add(C, facecolor=(0, 1, 1))

viewer.run()
