# ModernGL

[![PyPI](https://img.shields.io/pypi/l/ModernGL.svg)](https://pypi.python.org/pypi/ModernGL)
[![PyPI](https://img.shields.io/pypi/pyversions/ModernGL.svg)](https://pypi.python.org/pypi/ModernGL)
[![PyPI](https://img.shields.io/pypi/v/ModernGL.svg)](https://pypi.python.org/pypi/ModernGL)
[![github](https://img.shields.io/github/tag/cprogrammer1994/ModernGL.svg)](https://github.com/cprogrammer1994/ModernGL)<br>
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.me/ModernGL)
[![Chat](https://badges.gitter.im/cprogrammer1994/ModernGL.svg)](https://gitter.im/cprogrammer1994/ModernGL?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![PyPI](https://img.shields.io/pypi/status/ModernGL.svg)](https://pypi.python.org/pypi/ModernGL)

## Description

OpenGL is a great environment for developing portable, platform independent,
interactive 2D and 3D graphics applications. The API implementation in Python
is cumbersome, resulting in applications with high latency. To solve this
problem we have developed ModernGL, a wrapper over OpenGL that simplifies the
creation of simple graphics applications like scientific simulations, small
games or user interfaces. Usually, acquiring in-depth knowledge of OpenGL
requires a steep learning curve. In contrast, ModernGL is easy to learn and
use, moreover it is capable of rendering with the same performance and
quality, with less code written.

## Sample

```py

ModernGL.Init()

prog = ModernGL.NewProgram([
	ModernGL.NewVertexShader('''
		#version 330 core
		in vec2 vert;
		void main() {
			gl_Position = vec4(vert, 0.0, 1.0);
		}
	'''),
	ModernGL.NewFragmentShader('''
		#version 330 core
		out vec4 color;
		void main() {
			color = vec4(0.2, 0.6, 0.9, 1.0);
		}
	'''),
])

vbo = ModernGL.NewVertexBuffer(struct.pack('6f', 0, 0, 1, 0, 0, 1))
vao = ModernGL.NewVertexArray(prog, vbo, '2f', ['vert'])

ModernGL.RenderTriangles(vao, 3)

```

## How to install

```
pip install ModernGL
```

-----

for **Ubuntu**:
```
apt-get install python3-dev
apt-get install libgl1-mesa-dev
pip3 install ModernGL
```

-----

some examples depend on: **PyQt5** and **GLWindow**
```
pip3 install PyQt5
pip install GLWindow
```

**PyQt5** is platform independent. **GLWindow** is windows only.

## How to use

Please follow the [Examples](https://github.com/cprogrammer1994/ModernGL/tree/master/Examples) or [Tutorials](https://github.com/cprogrammer1994/ModernGL/tree/master/Tutorials).

## Links

[Examples](https://github.com/cprogrammer1994/ModernGL/tree/master/Examples)<br>
[Documentation](https://pythonhosted.org/ModernGL/)<br>
[Questions](https://gitter.im/cprogrammer1994/ModernGL)<br>
[PyPI](https://pypi.python.org/pypi/ModernGL/)<br>
[Github Repository](https://github.com/cprogrammer1994/ModernGL/)<br>
[Github Page](http://cprogrammer1994.github.io/ModernGL/)<br>
[Github Docs](https://github.com/cprogrammer1994/ModernGL/wiki)<br>

# Pull requests are welcome!

# Documentation

Use the builtin `help()` for the latest docs.

The [Documentation](https://pythonhosted.org/ModernGL/) will be updated soon.

# Examples

Please follow the [Examples](https://github.com/cprogrammer1994/ModernGL/tree/master/Examples).

# Supported Versions

## Python

![Python-3.4](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/Python-34.png)
![Python-3.5](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/Python-35.png)
![Python-3.6](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/Python-36.png)

## OpenGL

![OpenGL-3.0](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-30.png)
![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
![OpenGL-3.3](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-33.png)<br>
![OpenGL-4.0](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-40.png)
![OpenGL-4.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-41.png)
![OpenGL-4.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-42.png)
![OpenGL-4.3](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-43.png)
![OpenGL-4.4](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-44.png)
![OpenGL-4.5](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-45.png)

Checkout the [OpenGL Registry](https://www.opengl.org/registry/) for core specifications.

## minimum OpenGL support per method

Method | Version
--- | ---
BuildMipmaps | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
Clear | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DebugInfo | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DebugVar | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteComputeShader | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteFramebuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteIndexBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteProgram | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteShader | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteStorageBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteTexture | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteUniformBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteVertexArray | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DeleteVertexBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DisableAttributes | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DisableBlend | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DisableCullFace | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DisableDepthTest | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
DisableMultisample | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
EnableAttributes | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
EnableBlend | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
EnableCullFace | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
EnableDepthTest | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
EnableMultisample | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
EnableOnly | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
ExampleMethod | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
GetInfo | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
Init | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
LineSize | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewAdvancedVertexArray | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewComputeShader | ![OpenGL-4.3](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-43.png)
NewFragmentShader | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewFramebuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewGeometryShader | ![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
NewIndexBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewProgram | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewStorageBuffer | ![OpenGL-4.3](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-43.png)
NewTessControlShader | ![OpenGL-4.0](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-40.png)
NewTessEvaluationShader | ![OpenGL-4.0](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-40.png)
NewTexture | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewTransformProgram | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewUniformBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewVertexArray | ![OpenGL-4.0](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-40.png)
NewVertexBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
NewVertexShader | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
PointSize | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
ReadDepthPixel | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
ReadDepthPixels | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
ReadPixel | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
ReadPixels | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
ReadStorageBuffer | ![OpenGL-4.3](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-43.png)
RenderLineLoop | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
RenderLineStrip | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
RenderLineStripAdjacency | ![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
RenderLines | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
RenderLinesAdjacency | ![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
RenderPoints | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
RenderTriangleFan | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
RenderTriangleStrip | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
RenderTriangleStripAdjacency | ![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
RenderTriangles | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
RenderTrianglesAdjacency | ![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
RunComputeShader | ![OpenGL-4.3](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-43.png)
SetTextureFiltered | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
SetTextureMipmapped | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
SetTexturePixelated | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
SetUniform | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
TransformLineLoop | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
TransformLineStrip | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
TransformLineStripAdjacency | ![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
TransformLines | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
TransformLinesAdjacency | ![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
TransformPoints | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
TransformTriangleFan | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
TransformTriangleStrip | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
TransformTriangleStripAdjacency | ![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
TransformTriangles | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
TransformTrianglesAdjacency | ![OpenGL-3.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-32.png)
UpdateIndexBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
UpdateStorageBuffer | ![OpenGL-4.3](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-43.png)
UpdateTexture | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
UpdateUniformBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
UpdateVertexBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
UseFramebuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
UseStorageBuffer | ![OpenGL-4.3](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-43.png)
UseTexture | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
UseTextureAsImage | ![OpenGL-4.2](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-42.png)
UseUniformBuffer | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)
Viewport | ![OpenGL-3.1](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Badges/OpenGL-31.png)

# Cross-platform

- tested on Ubuntu 16.04
- tested on Windows 7
- tested on Windows 10

![Ubuntu](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Ubuntu.png)
![Win7](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Win7.png)
![Win10](https://raw.githubusercontent.com/cprogrammer1994/ModernGL/master/docs/Images/Win10.png)
