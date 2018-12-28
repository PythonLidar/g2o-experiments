import numpy as np
import g2o
import pangolin as pango
import OpenGL.GL as gl

optimizer = g2o.SparseOptimizer()
optimizer.set_verbose(True)

optimizer.load("data/garage.g2o")

vertices = [i.estimate().t for i in optimizer.vertices().values()]

pango.CreateWindowAndBind('Main', 640, 480)
gl.glEnable(gl.GL_DEPTH_TEST)

# Define Projection and initial ModelView matrix
scam = pango.OpenGlRenderState(
  pango.ProjectionMatrix(640, 480, 420, 420, 320, 240, 0.2, 2000000),
  pango.ModelViewLookAt(-2, 2, -2, 0, 0, 0, pango.AxisDirection.AxisY))
handler = pango.Handler3D(scam)

# Create Interactive View in window
dcam = pango.CreateDisplay()
dcam.SetBounds(0.0, 1.0, 0.0, 1.0, -640.0/480.0)
dcam.SetHandler(handler)

while not pango.ShouldQuit():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
  gl.glClearColor(0.15, 0.15, 0.15, 1.0)
  dcam.Activate(scam)

  gl.glPointSize(5)
  gl.glColor3f(1.0,1.0,1.0)

  pango.DrawLines(vertices)

  pango.FinishFrame()
