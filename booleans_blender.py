import compas
import compas_blender
from compas.geometry import Translation
from compas.datastructures import Mesh
from compas.geometry import boolean_intersection_mesh_mesh
from compas_blender.artists import MeshArtist

compas_blender.clear()

FILE = '/Users/vanmelet/Code/TUD21/booleans.json'

data = compas.json_load(FILE)

A = data['A']
B = data['B']
C = data['C']
D = data['D']

V, F = boolean_intersection_mesh_mesh(A.to_vertices_and_faces(), B.to_vertices_and_faces())

E = Mesh.from_vertices_and_faces(V, F)
E.transform(Translation.from_vector([10, 0, 0]))

data['E'] = E

compas.json_dump(data, FILE)

MeshArtist(A).draw_mesh()
MeshArtist(B).draw_mesh()
MeshArtist(C).draw_mesh()
MeshArtist(D).draw_mesh()
MeshArtist(E).draw_mesh()
