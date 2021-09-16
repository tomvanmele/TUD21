import compas
import compas_rhino
from compas.geometry import Translation
from compas.datastructures import Mesh
from compas.geometry import boolean_union_mesh_mesh
from compas.geometry import boolean_difference_mesh_mesh
from compas_rhino.artists import MeshArtist

compas_rhino.clear()

data = compas.json_load('booleans.json')

A = data['A']
B = data['B']

V, F = boolean_union_mesh_mesh(A.to_vertices_and_faces(), B.to_vertices_and_faces())

C = Mesh.from_vertices_and_faces(V, F)
C.transform(Translation.from_vector([4, 0, 0]))

V, F = boolean_difference_mesh_mesh(A.to_vertices_and_faces(), B.to_vertices_and_faces())

D = Mesh.from_vertices_and_faces(V, F)
D.transform(Translation.from_vector([8, 0, 0]))

data['C'] = C
data['D'] = D

compas.json_dump(data, 'booleans.json')

MeshArtist(A).draw_faces(color=(255, 0, 0), join_faces=True)
MeshArtist(B).draw_faces(color=(0, 255, 0), join_faces=True)
MeshArtist(C).draw_faces(color=(0, 255, 255), join_faces=True)
MeshArtist(D).draw_faces(color=(0, 255, 255), join_faces=True)
