import ModernGL as GL
import GLWindow as WND
import struct

WND.Init()
GL.Init()

vert = GL.NewVertexShader('''
	#version 330

	in vec3 vert;

	uniform float znear;
	uniform float zfar;
	uniform float fovy;
	uniform float ratio;

	uniform vec3 center;
	uniform vec3 eye;
	uniform vec3 up;

	mat4 perspective() {
		float zmul = (-2.0 * znear * zfar) / (zfar - znear);
		float ymul = 1.0 / tan(fovy * 3.14159265 / 360);
		float xmul = ymul / ratio;

		return mat4(
			xmul, 0.0, 0.0, 0.0,
			0.0, ymul, 0.0, 0.0,
			0.0, 0.0, -1.0, -1.0,
			0.0, 0.0, zmul, 0.0
		);
	}

	mat4 lookat() {
		vec3 forward = normalize(center - eye);
		vec3 side = normalize(cross(forward, up));
		vec3 upward = cross(side, forward);
		return mat4(
			side.x, upward.x, -forward.x, 0,
			side.y, upward.y, -forward.y, 0,
			side.z, upward.z, -forward.z, 0,
			-dot(eye, side), -dot(eye, upward), dot(eye, forward), 1
		);
	}

	void main() {
		gl_Position = perspective() * lookat() * vec4(vert, 1.0);
	}
''')

frag = GL.NewFragmentShader('''
	#version 330
	
	out vec4 color;

	void main() {
		color = vec4(0.04, 0.04, 0.04, 1.0);
	}
''')

prog = GL.NewProgram([vert, frag])

GL.SetUniform(prog['znear'], 0.1)
GL.SetUniform(prog['zfar'], 1000.0)
GL.SetUniform(prog['ratio'], 16 / 9)
GL.SetUniform(prog['fovy'], 60)

GL.SetUniform(prog['eye'], 3, 3, 3)
GL.SetUniform(prog['center'], 0, 0, 0)
GL.SetUniform(prog['up'], 0, 0, 1)

grid = bytes()

for i in range(0, 65):
	grid += struct.pack('6f', i - 32, -32.0, 0.0, i - 32, 32.0, 0.0)
	grid += struct.pack('6f', -32.0, i - 32, 0.0, 32.0, i - 32, 0.0)

vbo = GL.NewVertexBuffer(grid)
vao = GL.NewVertexArray(prog, vbo, '3f', ['vert'])

while WND.Update():
	GL.Clear(240, 240, 240)
	GL.RenderLines(vao, 65 * 4) 