# Graphics Workshop

_This repo contains a selection of projects designed to help you learn the basics of computer graphics. We'll be writing shaders to render interactive two-dimensional and three-dimensional scenes._

_Each of these projects aims to introduce an important graphics technique that is extensively used in real-world applications. The code is designed to run in real time on modern GPUs, without requiring any extra software. Feel free to take creative liberties to produce a result that you find aesthetically pleasing!_

<br>

## Contents

- [**Getting started**](#getting-started)
- [**Projects**](#projects) — Introduction to each of the projects
  - [**Quilt patterns**](#quilt-patterns)
  - [**Procedural landscapes**](#procedural-landscapes)
  - [**Rasterization and shading**](#rasterization-and-shading)
  - [**Stylized rendering**](#stylized-rendering)
  - [**Ray tracing**](#ray-tracing)
- [**Workflow**](#workflow) — Recommended way to work through the workshop
- [**Deployment**](#deployment) — Explanation of how automated deployment is set up
- [**Debugging tips**](#debugging-tips)

<br>

## Getting started

This workshop covers fragment shaders ([GLSL](https://en.wikipedia.org/wiki/OpenGL_Shading_Language)), procedural texture generation, rasterization, lighting calculations, and real-time ray tracing.

All of the projects will be developed in a harness that runs the graphics code in a web browser, using a standard technology called WebGL. This allows us to use modern web development tools to iterate quickly and easily share your work with others. However, you will not need to write JavaScript code yourself, as all of the wrapper code has been provided for you.

To get started, **make sure that you have [Node.js v14](https://nodejs.org/en/) and [NPM](https://www.npmjs.com/) installed**. **Fork this repository**, and then **clone it to your computer**. Then, **run the following commands**:

```
$ npm install
...
added 16 packages from 57 contributors and audited 16 packages in 1.459s

3 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities


$ npm run dev

  vite v2.1.5 dev server running at:

  > Local:    http://localhost:3000/
  > Network:  http://10.250.14.217:3000/

  ready in 555ms.
```

_Explanation:_ The first command installs dependencies in the `node_modules/` folder, and the second command starts the development server. You can now visit `http://localhost:3000/` in your browser. Whenever you change a file and save it, the website will automatically update.

<br>

## Projects

Here is an introduction to each of the projects.

If you are new to graphics or shading languages, I would recommend trying the "quilt patterns" project first. You should also complete "rasterization and shading" before starting the "stylized rendering" and "ray tracing" projects.

### Quilt patterns

This project shows how you can use GPU shaders to render interesting, procedural patterns on a 2D grid. It also serves as a hand-on introduction to the wonderful yet frightening world of GPU shaders.

<p align="center">
<a href="#quilt-patterns">
<img src="https://i.imgur.com/5QsIZUc.png" width="600">
</a>
</p>

Before starting, make sure that you are able to open the development server. You should see an oscillating color gradient in your web browser.

1. Look at the provided skeleton code. This is known as a _fragment shader_, and it runs on the GPU. The fragment shader is run on every pixel of the screen, and the pixel number is passed into the code as `gl_FragCoord.xy`. The code outputs by assigning to `gl_FragColor`, which is the color at that pixel. It is a `vec4` or 4-dimensional vector with red, green, blue, and transparency channels.
2. Make sure you understand the starter code before continuing. What do the `coord` and `color` variables represent? What do the `abs()` and `sin()` functions do?
3. Uncomment the numbered sections of the starter code, _one at a time_. Observe the change in output on your screen. Make sure that you understand what each block of code is doing before proceeding to the next one! When you're done, you should now see a moving black-and-white grid pattern.
4. **Task 1:** Make the quilt pattern more colorful! Modify the code so that instead of generating random greyscale colors with the variable `c`, it generates random RGB colors instead.
5. **Task 2:** Right now, there's just a single pattern that's flown through, but there could be many more. Find a way to use the `seed` variable, which you can modify using the "Parameters" panel at the top right of the screen, to change the shape of the pattern. (_Hint:_ You'll probably want to adjust the condition `if (mod(2.0 * cell.x + cell.y, 5.0) == 1.0)` to change the quilt's geometry.)

Feel free to experiment and get creative! For example, add stripes or other shapes besides triangles. If you're looking for inspiration, try doing a Google search for "quilt patterns."

_Project skeleton is located in `shaders/quilt.frag.glsl`._

### Procedural landscapes

This project involves generating an organic procedural landscape, similar to what you might see in open world games like Minecraft.

<p align="center">
<a href="#procedural-landscapes">
<img src="https://i.imgur.com/elM7R8w.png" width="600">
</a>
</p>

To view in your browser, choose the "project" setting in the controls pane on the top-right and select this project.

1. To generate natural appearances, we will be using a popular graphics primitive called [_simplex noise_](https://en.wikipedia.org/wiki/Simplex_noise). Feel free to read online about the theory behind this algorithm. The function `float snoise(vec2)` takes in a 2-vector on the screen and outputs a smooth scalar noise value at that location.
2. Try changing the "seed" at the top-right of the screen. You should see the rendered output take a new shape, as noise values at different locations are roughly independent.
3. Uncomment the first block of code, one line at a time. What do you notice visually as higher-frequency noise scales are added to the color? By combining various _octaves_ of noise at different amplitudes, you can change the texture's appearance.
4. Uncomment the second block of code, and observe how thresholding (in particular, the `mix` and `smoothstep` functions) are used to interpolate colors between elevation values.
5. Finally, uncomment the third block of code to generate land objects.
6. **Task:** In addition to elevation, add another parameter such as _temperature_ that is independently sampled from the noise map. Experiment with using temperature to change the shading and indicate map biomes.

_Project skeleton is located in `shaders/landscape.frag.glsl`._

### Rasterization and shading

This project renders a 3D triangle mesh using the _rasterization_ method that is very popular in real-time computer graphics. This is the same algorithm that most video games are built upon.

<p align="center">
<a href="#rasterization-and-shading">
<img src="https://i.imgur.com/aLXzTUM.png" width="600">
</a>
</p>

Rasterization works by breaking up a 3D surface into triangles, then drawing each triangle on the screen independently and interpolating variables between them.

Three-dimensional graphics can be much more complex than its two-dimensional counterpart. Unlike in the past projects, the fragment shader will now be evaluated once for each _fragment_ of a triangle, rather than once for every pixel. For this project, we will be focus on shading. See the [Scratchapixel article on the Phong illumination model](https://www.scratchapixel.com/lessons/3d-basic-rendering/phong-shader-BRDF) for background reading.

1. The project starts out by giving you a teapot. You can click and drag on the screen to move your camera position and see different angles of the teapot. This object is stored as a _triangle mesh_, which is a common format in computer graphics.
2. Try changing the value of `mesh` to see your code rendering different shapes besides the teapot. Also, you can play with `kd` to change the color of the object.
3. **Task:** Right now, the starter code has a function `illuminate()` which takes in the position of a light and returns how much color that light contributes to the current pixel. At the moment, the rendered result looks a little "flat" because the code only implements the diffuse component of the [Phong reflectance model](https://en.wikipedia.org/wiki/Phong_reflection_model). Based on the Wikipedia article, and using the comments as a guide, update the code to also add the Phong specular component. Your task is complete when the teapot looks similar to the image above.

If you're curious to learn more about lighting models, try upgrading your Phong shader to a microfacet model such the [Cook-Torrance BRDF](http://www.codinglabs.net/article_physically_based_rendering_cook_torrance.aspx). If you do, you may also want to implement [sRGB gamma correction](https://en.wikipedia.org/wiki/Gamma_correction).

_Project skeleton is located in `shaders/shading.frag.glsl`._

### Stylized rendering

This project explores stylized rendering, also known as [non-photorealistic rendering](https://en.wikipedia.org/wiki/Non-photorealistic_rendering). This is an area of graphics that gives up being faithful to real life, but enables much more creative expression in mimicking expressive styles.

<p align="center">
<a href="#stylized-rendering">
<img src="https://i.imgur.com/jWSXA8g.png" width="600">
</a>
</p>

The code for this project is very similar to that of the last rasterization and shading project. However, after doing lighting calculations, we do not output the color immediately. Instead, we discretize it and shade in different styles based on a thresholded value of the luma intensity. Here, we mimic the art style found in comic books.

1. **Task:** Once again, fill in your code for specular highlights in the `illuminate()` function, similar to last time. How does this change the output's appearance as you rotate the camera view? You may need to tweak some parameters to obtain an aesthetically pleasing result.

_Project skeleton is located in `shaders/contours.frag.glsl`._

### Ray tracing

This project is a real-time ray tracer implemented as a GPU shader. Ray tracing is the gold standard in photorealistic rendering. Here's how the Academy Award-winning textbook _Physically Based Rendering_ describes it:

> `pbrt` is based on the _ray-tracing_ algorithm. Ray tracing is an elegant technique that has its origins in lens making; Carl Friedrich Gauß traced rays through lenses by hand in the 19th century. Ray-tracing algorithms on computers follow the path of infinitesimal rays of light through the scene until they intersect a surface. This approach gives a simple method for finding the first visible object as seen from any particular position and direction and is the basis for many rendering algorithms.

<p align="center">
<a href="#ray-tracing">
<img src="https://i.imgur.com/1xaJmxY.png" width="600">
</a>
</p>

You might find this [non-technical introductory video by Disney](https://youtu.be/frLwRLS_ZR0) to provide helpful context.

1. To parallelize our ray tracer and run it on a GPU shader, we revert back to running our fragment shader once for every pixel in the screen, like in the 2D graphics examples. However, this time, our shader will do some geometry calculations by shooting rays from the camera for each pixel. The `trace()` function models this behavior by returning the color corresponding to a given ray.
2. To model geometry, the starter code has set up a simple scene involving three spheres and one circle forming the checkered floor. This geometry is located in the `intersect()` function, which computes the first intersection point (represented by a `Hit` struct) of any ray in the space. Following the pattern shown here, add a fourth sphere to the scene with a different position, color, and radius.
3. The `calcLighting()` function uses `illuminate()`, which contains a simple implementation of a Phong shader, to compute the lighting at a given point by adding up the contributions of two point lights. Modify this code to add a third point light at a different location, with your choice of intensity. (For inspiration, see [three-point lighting](https://en.wikipedia.org/wiki/Three-point_lighting).)
4. **Task:** Implement shadows. In the `illuminate()` function, before doing lighting calculations, add a conditional statement checks if the ray from the point to the light source is obstructed or not. If it is obstructed, then you should immediately return `vec3(0.0)` to simulate shadows. [Hint: You will need to use the `intersect()` function with a new `Ray` object that you construct, starting from the point `pos`.]

If you're interested in learning more about ray tracing, check out [rpt](https://github.com/ekzhang/rpt/), which is a physically-based path tracer written in Rust with a lot more features.

_Project skeleton is located in `shaders/raytracing.frag.glsl`._

<br>

## Workflow

Open your code editor in one window, and **keep the website on the side** while you're writing your shader code. It's extremely useful to see what happens to the output in real time as you edit your code. Your browser should instantly update (using [Vite](https://vitejs.dev/)'s hot module replacement feature) whenever you change a file.

The project has a [Tweakpane](https://cocopon.github.io/tweakpane/) component in the top-right corner of the screen. You can use this to change what project is being displayed and modify parameters for that display. It persists settings when you refresh your browser.

For 3D projects, the main `<canvas>` element has an event listener for mouse and touch events, which should allow you to move the camera by clicking and dragging. Data is passed in through the appropriate uniform variables.

When you're done with the workshop, each project should render without errors or visual artifacts, and the outputs should be interesting.

<br>

## Deployment

This repository comes with a Continuous Integration workflow (through GitHub Actions) that compiles the code on the `main` branch, then pushes the built HTML to your repository's `gh-pages` branch. It lets you share a web link that updates whenever you push code changes.

<p align="center">
<a href="#deployment">
<img src="https://i.imgur.com/NufzXDw.png" width="600">
</a>
</p>

If this isn't enabled already, go to the "Pages" section under the "Settings" tab of your repository and set the deploy target to the `gh-pages` branch. Then, after the next `git push`, you will be see your work at `https://<YOUR_USERNAME>.github.io/graphics-workshop/`.

<br>

## Debugging tips

If you're stuck debugging OpenGL shaders, try setting `gl_FragColor` to the result of an intermediate variable and visually examining the output.

If there's a function you're confused about, you can search online through the Khronos documentation. You can also try reading [The Book of Shaders](https://thebookofshaders.com/), which is an excellent technical resource.

[ShaderToy](https://www.shadertoy.com/) is an online community for creating and sharing shaders through WebGL, and you should feel free to take inspiration from their featured demos.

<br>

<sup>
All code is licensed under the <a href="LICENSE">MIT license</a>.
</sup>
