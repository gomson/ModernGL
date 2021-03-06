from PIL import Image
from OpenGL.GLUT import *
import ModernGL as GL
import struct, time

width, height = 800, 600
start = time.time()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutCreateWindow('')

GL.Init()

vert = GL.NewVertexShader('''
	#version 330

	in vec2 vert;

	in vec3 vert_color;
	out vec3 frag_color;

	uniform vec2 scale;
	uniform float rotation;

	void main() {
		frag_color = vert_color;
		mat2 rot = mat2(cos(rotation), sin(rotation), -sin(rotation), cos(rotation));
		gl_Position = vec4((rot * vert) * scale, 0.0, 1.0);
	}
''')

frag = GL.NewFragmentShader('''
	#version 330
	
	in vec3 frag_color;
	out vec4 color;

	void main() {
		color = vec4(frag_color, 1.0);
	}
''')

prog = GL.NewProgram([vert, frag])

vbo = GL.NewVertexBuffer(struct.pack('15f', 1.0, 0.0, 1.0, 0.0, 0.0, -0.5, 0.86, 0.0, 1.0, 0.0, -0.5, -0.86, 0.0, 0.0, 1.0))
vao = GL.NewVertexArray(prog, vbo, '2f3f', ['vert', 'vert_color'])

GL.SetUniform(prog['scale'], height / width * 0.75, 0.75)

def display():
	GL.Clear(240, 240, 240)
	GL.SetUniform(prog['rotation'], time.time() - start)
	GL.RenderTriangles(vao, 3)
	glutSwapBuffers()

glutDisplayFunc(display)
glutIdleFunc(display)
glutMainLoop()
