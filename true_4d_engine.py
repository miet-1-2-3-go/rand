"""
true_4d_engine.py

Requirements:
    pip install numpy matplotlib

Run:
    python true_4d_engine.py
"""

import numpy as np
import itertools
import math
from functools import partial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers 3D projection
from matplotlib.animation import FuncAnimation

# ----------------------------
# Utilities: 4D points & matrices
# ----------------------------
def make_rotation_matrix_4d(i, j, theta):
    """
    Return a 4x4 rotation matrix that rotates in the (i,j) plane by angle theta.
    i, j are indices in {0,1,2,3} corresponding to (x,y,z,w).
    The rotation affects only i and j coordinates.
    """
    R = np.eye(4)
    c = math.cos(theta)
    s = math.sin(theta)
    R[i, i] = c
    R[j, j] = c
    R[i, j] = -s
    R[j, i] = s
    return R

def apply_matrix(points, M):
    """
    Apply 4x4 matrix M to an (N,4) array of 4D points.
    """
    return points.dot(M.T)

# ----------------------------
# 4D objects (example: tesseract)
# ----------------------------
def make_tesseract(scale=1.0):
    """
    Create the 16 vertices of a unit tesseract centered at origin.
    Returns:
        vertices: (16,4) ndarray
        edges: list of (i,j) pairs
    """
    verts = np.array(list(itertools.product([-1, 1], repeat=4)), dtype=float) * scale
    edges = []
    n = len(verts)
    for i in range(n):
        for j in range(i + 1, n):
            # edge if vertices differ in exactly one coordinate
            if np.sum(np.abs(verts[i] - verts[j]) > 1e-6) == 1:
                edges.append((i, j))
    return verts, edges

def make_4simplex(scale=1.0):
    """
    4D simplex (5-cell) example: 5 vertices (regular simplex).
    Returns vertices and edges.
    """
    # Simple construction: unit vectors plus negative average
    v = [np.zeros(4) for _ in range(5)]
    for i in range(4):
        v[i][i] = 1.0
    v[4] = -np.sum(np.array(v[:4]), axis=0)
    verts = np.array(v) * scale
    edges = [(i, j) for i in range(len(verts)) for j in range(i+1, len(verts))]
    return verts, edges

# ----------------------------
# 4D -> 3D projection
# ----------------------------
def project_4d_to_3d(points4d, camera_w=3.0, eps=1e-6):
    """
    Perspective projection from 4D to 3D with camera located at w = camera_w
    Projects (x,y,z,w) -> (x', y', z') where x' = x * (camera_w / (camera_w - w)), etc.
    points4d: (N,4) array
    Returns: (N,3) array
    """
    w = points4d[:, 3]
    denom = (camera_w - w)
    # prevent division by zero / extreme values
    denom = np.where(np.abs(denom) < eps, np.sign(denom) * eps, denom)
    factor = camera_w / denom
    projected = points4d[:, :3] * factor[:, np.newaxis]
    return projected

# ----------------------------
# Rendering utilities (matplotlib 3D)
# ----------------------------
def draw_edges_3d(ax, points3d, edges, color_by_w=None, linewidth=1.0):
    """
    Draw edges in a 3D axes.
    color_by_w: optional (N,) array to color vertices/edges (e.g., using w coordinate).
    """
    for (i, j) in edges:
        p1 = points3d[i]
        p2 = points3d[j]
        xs = [p1[0], p2[0]]
        ys = [p1[1], p2[1]]
        zs = [p1[2], p2[2]]
        ax.plot(xs, ys, zs, linewidth=linewidth, color='black')

    # optionally show vertices and color them by w
    if color_by_w is not None:
        sc = ax.scatter(points3d[:, 0], points3d[:, 1], points3d[:, 2],
                        c=color_by_w, cmap='coolwarm', s=30, depthshade=True)
        return sc
    else:
        ax.scatter(points3d[:, 0], points3d[:, 1], points3d[:, 2], c='red', s=20)
        return None

# ----------------------------
# Engine: holds world state, does 4D transforms
# ----------------------------
class FourDEngine:
    def __init__(self, vertices4d, edges, camera_w=3.0):
        self.base_vertices = vertices4d.copy()  # (N,4)
        self.edges = edges
        self.camera_w = camera_w
        self.transform = np.eye(4)   # current 4D transform (4x4)
        self.translation = np.zeros(4)  # optional 4D translation

    def reset_transform(self):
        self.transform = np.eye(4)
        self.translation = np.zeros(4)

    def apply_rotation(self, plane_idx_pair, theta):
        """Compose a rotation about given (i,j) plane by theta radians."""
        R = make_rotation_matrix_4d(plane_idx_pair[0], plane_idx_pair[1], theta)
        self.transform = R.dot(self.transform)

    def apply_scaling(self, s):
        S = np.eye(4) * s
        S[3,3] = 1.0 if s != 0 else 0.0  # keep w scaling reasonable if desired
        self.transform = S.dot(self.transform)

    def apply_translation(self, t4):
        self.translation += np.array(t4)

    def get_transformed_vertices(self):
        transformed = apply_matrix(self.base_vertices, self.transform)
        transformed = transformed + self.translation[np.newaxis, :]
        return transformed

    def project_to_3d(self):
        verts4 = self.get_transformed_vertices()
        verts3 = project_4d_to_3d(verts4, camera_w=self.camera_w)
        return verts3, verts4  # also return original 4D verts for coloring, etc.

# ----------------------------
# Example: animate a rotating tesseract
# ----------------------------
def run_demo_tesseract():
    verts4, edges = make_tesseract(scale=1.0)
    engine = FourDEngine(verts4, edges, camera_w=3.0)

    # Matplotlib 3D setup
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1,1,1])
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title("Tesseract: true 4D math → projected to 3D (rotate camera with mouse)")

    # Animation state
    # define which planes we'll rotate in and speed multipliers
    rotations = [
        ((0, 3), 0.03),  # x-w
        ((1, 2), 0.015), # y-z
        ((1, 3), 0.02),  # y-w
    ]

    scatter = None

    def update(frame):
        nonlocal scatter
        ax.cla()
        ax.set_box_aspect([1,1,1])
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_zlim(-3, 3)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # update rotations by composing small increments
        for (plane, speed) in rotations:
            engine.apply_rotation(plane, speed)

        verts3, verts4 = engine.project_to_3d()

        # color by w (4th coord) so you can see how 4th-dim values map to projection
        wvals = verts4[:, 3]
        # draw edges and colored vertices
        scatter = draw_edges_3d(ax, verts3, edges, color_by_w=wvals)

        # optional: draw a simple grid or axes in projected 3D
        # ax.plot([0,0],[0,0],[0,2], color='gray')

        return scatter,

    anim = FuncAnimation(fig, update, frames=600, interval=30, blit=False)
    plt.show()


# ----------------------------
# Optional: CLI entry
# ----------------------------
if __name__ == "__main__":
    run_demo_tesseract()
