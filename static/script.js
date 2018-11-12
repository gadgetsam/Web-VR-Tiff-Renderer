/* globals BABYLON */

//https://storage.googleapis.com/webxr/butterfly_wing_small.tif
var shader = function () {
    BABYLON.Effect.ShadersStore["customVertexShader"] = "precision highp float;\r\n" +

        "// Attributes\r\n" +
        "attribute vec3 position;\r\n" +
        "attribute vec3 normal;\r\n" +
        "attribute vec2 uv;\r\n" +

        "// Uniforms\r\n" +
        "uniform mat4 worldViewProjection;\r\n" +

        "// Varying\r\n" +
        "varying vec2 vUV;\r\n" +

        "void main(void) {\r\n" +
        "    vec4 outPosition = worldViewProjection * vec4(position, 1.0);\r\n" +
        "    gl_Position = outPosition;\r\n" +

        "    vUV = uv;\r\n" +
        "}\r\n";

    BABYLON.Effect.ShadersStore["customFragmentShader"] = "precision highp float;\r\n" +

        "varying vec2 vUV;\r\n" +

        "// Refs\r\n" +
        "uniform sampler2D textureSampler;\r\n" +
        "uniform float alphaCutoff;\r\n" +

        "void main(void) {\r\n" +
        "    vec3 color = texture2D(textureSampler, vUV).rgb;\r\n" +
        "    \r\n" +
        "    if (color.r+color.b+color.g < 3.0*alphaCutoff) {\r\n" +
        "        discard;\r\n" +
        "    }\r\n" +
        "    \r\n" +
        "    gl_FragColor = vec4(color.rgb, 1.);\r\n" +
        "}\r\n";
}
window.addEventListener('DOMContentLoaded', function () {

    var scaleUp = false;
    var scaleDown = false;
    var leftMovement = false;
    var rightMovement = false;
    // get the canvas DOM element
    var canvas = document.getElementById('renderCanvas');
    var parentAll;
    var unparentAll;
    // load the 3D engine
    var engine = new BABYLON.Engine(canvas, true, {preserveDrawingBuffer: true, stencil: true});
    // engine.enableOfflineSupport = false;

    // createScene function that creates and return the scene
    var createScene = function () {
        // create a basic BJS Scene object

        var scene = new BABYLON.Scene(engine);

        //   var sphere = BABYLON.MeshBuilder.CreateDisc("sphere", {tesselation:3}, scene);
        //   sphere.scaling = new BABYLON.Vector3(0, 0, 0);
        // sphere.material = new BABYLON.StandardMaterial("", scene)
        // sphere.material.disableLighting = true;


        // var environment = scene.createDefaultEnvironment({groundYBias: 1});
        // environment.setMainColor(BABYLON.Color3.FromHexString("#74b9ff"))
        scene.ambientColor = new BABYLON.Color3(0.3, 0.3, 0.3);

        var camera = new BABYLON.ArcRotateCamera("Camera", 3 * Math.PI / 2, Math.PI / 2, 5, BABYLON.Vector3.Zero(), scene);
        camera.attachControl(canvas, false);
        var counter = 0;
        var vrHelper = scene.createDefaultVRExperience({createDeviceOrientationCamera: false});
        var webVRCamera = vrHelper.webVRCamera;
        var leftControllerEnabled = false;
        var rightControllerEnabled = false;

        function pad(n, width, z) {
            z = z || '0';
            n = n + '';
            return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
        }

        vrHelper.enableInteractions();
        vrHelper.webVRCamera.minZ = 0;
        vrHelper.raySelectionPredicate = (mesh) => {
            return mesh.isPickable
        }
        var spheres = []

        var lastPosition = 0;
        var distance = 0
        var numInstances = 0
        var scaleMesh = new BABYLON.AbstractMesh("", scene)

        var currentPosition = new BABYLON.Vector3(0, 0, 0)
        scene.registerBeforeRender(function () {

            if (scaleDown) {
                if (scaleMesh.scaling.x > .5 && scaleMesh.scaling.y > .5 && scaleMesh.scaling.z > .5) {
                    scaleMesh.scaling.x -= .01;
                    scaleMesh.scaling.y -= .01;
                    scaleMesh.scaling.z -= .01;


                }
            }
            if (scaleUp) {

                scaleMesh.scaling.x += .01;
                scaleMesh.scaling.y += .01;
                scaleMesh.scaling.z += .01;


            }
            if (rightControllerEnabled) {

                if (true) {
                    // var newInstance = sphere.createInstance("i"+counter);
                    var m = new BABYLON.Matrix();
                    mesh2.getWorldMatrix().invertToRef(m);
                    var v = BABYLON.Vector3.TransformCoordinates(webVRCamera.rightController.devicePosition, m);

                    if (lastPosition == 0) {

                        lastPosition = v.clone();
                        console.log(lastPosition)
                    }
                    currentPosition = v
                    var delta = currentPosition.subtract(lastPosition)
                    distance = delta.length()
                    numInstances = distance / .05;
                    delta.scaleInPlace(1 / Math.ceil(numInstances))
                    // console.log(numInstances)
                    for (var x = 0; x < numInstances; x++) {
                        SPS.particles[counter].position.copyFrom(lastPosition);
                        // SPS.particles[counter].color = new BABYLON.Color3(1, 0, 0);
                        // SPS.particles[counter].quaternion.copyFrom(lastPosition);
                        lastPosition.addInPlace(delta)
                        SPS.setParticles(counter, counter + 1);
                        counter++
                    }
                    // console.log(distance);

                    // newInstance.scaling = new BABYLON.Vector3( .01 , .01, .01);
                    // console.log(counter);
                    // console.log(newInstance)
                    // spheres.push(newInstance)
                }

                lastPosition = currentPosition

            }
            else {
                lastPosition = 0

            }


//     
        });
//           var manager = new BABYLON.GUI.GUI3DManager(scene);
//   var button = new BABYLON.GUI.HolographicButton("reset");
//   manager.addControl(button);

//   // Must be done AFTER addControl in order to overwrite the default content
//   button.imageUrl = "https://cdn.glitch.com/90d8f616-ec1b-4687-9260-2666135dc97e%2Fbrush.png?1530435035100";
//   button.text = "Clear Drawing";

//   button.onPointerUpObservable.add(function(state){
//     console.log(state);
//     // Removal code here
//     for(var x=0; x<counter; x++){
//         SPS.particles[x].position.copyFrom(new BABYLON.Vector3(1000,1000,1000));


//     }
//     counter =0
//     SPS.setParticles()

//   });
        // sphere.position.x = 30.0 * Math.sin(k);
        // sphere.position.z = 20.0 * Math.sin(k * 6.0);
        // sphere.position.y = 8.0 * Math.sin(k * 8.0) + sphereAltitude;
        // k += 0.02;
        var light = new BABYLON.HemisphericLight("light1", new BABYLON.Vector3(1, 0, 1), scene);
        light.intensity = 0.7;
        // Default Environment


        var particleNb = 22000;
        var SPS = new BABYLON.SolidParticleSystem('SPS', scene, {particleIntersection: true});
        // SPS.computeBoundingBox = false;
        // SPS.computeParticleColor = false;
        // SPS.billboard = true;
        // SPS.computeParticleRotation = false;
        // SPS.computeParticleTexture = false;
        var disc = BABYLON.MeshBuilder.CreateBox("disc", {width: 0.01, height: .01, depth: .01}, scene);
      var myMaterial = new BABYLON.StandardMaterial("myMaterial", scene);
      myMaterial.emissiveColor = new BABYLON.Color3(1, 255, 0);

      disc.material = myMaterial
        SPS.addShape(disc, particleNb)
        disc.dispose();


        var mesh2 = SPS.buildMesh();
        mesh2.hasVertexAlpha = true;
        SPS.isAlwaysVisible = true;
        SPS.computeParticleTexture = false;

        // position things
        mesh2.position.y = 0.0;
        mesh2.position.x = -10.0;
        SPS.initParticles();


        var pl = new BABYLON.PointLight("pl", BABYLON.Vector3.Zero(), scene);
        pl.diffuse = new BABYLON.Color3(1, 1, 1);
        pl.specular = new BABYLON.Color3(1, 1, 1);
        pl.intensity = 0.8;
        shader();
        var numImages1 = configuration["numImages"]
        var imagesToRender = 20;
        var url = "static/wing/";
        var extension = ".png"

        var boxes = []
        var parentForAll =BABYLON.MeshBuilder.CreatePlane("box23", {}, scene);
        parentForAll.position = new BABYLON.Vector3(0,0,0)
        parentForAll.isVisible = false;


        var shaderMaterials = []

        for (var x = 1; x < numImages1-1; x+=1) {
            var shaderMaterial = new BABYLON.ShaderMaterial("shader", scene, {
                    vertex: "custom",
                    vertex: "custom",
                    fragment: "custom",
                },
                {
                    attributes: ["position", "normal", "uv", "alphaCutoff"],
                    uniforms: ["world", "worldView", "worldViewProjection", "view", "projection"]
                }
            );


            var mainTexture = new BABYLON.Texture("static/data/test/" + x + ".png", scene);
            shaderMaterial.setTexture("textureSampler", mainTexture);
            shaderMaterial.setFloat("time", 0);
            shaderMaterial.setFloat("alphaCutoff", .3)
            shaderMaterial.setVector3("cameraPosition", BABYLON.Vector3.Zero());
            shaderMaterial.backFaceCulling = false;
            shaderMaterials.push(shaderMaterial);

            var box = BABYLON.MeshBuilder.CreatePlane("box", {width:configuration["width"]/numImages1, height:configuration["height"]/numImages1}, scene);
            box.parent = parentForAll
            box.material = shaderMaterial;
            box.setPositionWithLocalVector(new BABYLON.Vector3(0, 0, 1-(x / numImages1)));
            box.isPickable = false;
            boxes.push(box);

        }
        boxes[boxes.length-1].isVisible = false
        boxes[0].isVisible = false

        parentAll = function (controllerMesh) {
            // boxes.forEach((box, index) => {
            //
            //     controllerMesh.addChild(box)
            // })
            controllerMesh.addChild(parentForAll)
            controllerMesh.addChild(mesh2)
        }
        unparentAll = function (controllerMesh) {
            // boxes.forEach((box, index) => {
                controllerMesh.removeChild(parentForAll)
            // })
            controllerMesh.removeChild(mesh2)
        }

        var plane = BABYLON.Mesh.CreatePlane("plane", 1);
        plane.position = new BABYLON.Vector3(0.1, 2, 0.1)
        var advancedTexture = BABYLON.GUI.AdvancedDynamicTexture.CreateForMesh(plane);
        var panel = new BABYLON.GUI.StackPanel();
        advancedTexture.addControl(panel);
        var header = new BABYLON.GUI.TextBlock();
        header.text = "Change threshold";
        header.height = "240px";
        header.width = "1500px"
        header.color = "white";
        header.textHorizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_CENTER;
        header.fontSize = "120"
        panel.addControl(header);
        var slider = new BABYLON.GUI.Slider();
        slider.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_CENTER;
        slider.minimum = 0;
        slider.maximum = 1;
        slider.color = "green";
        slider.value = .3;
        slider.height = "500px";
        slider.width = "2000px";
        panel.addControl(slider);

        slider.onValueChangedObservable.add(function (value) {


            console.log(value);
            for (var x = 0; x < boxes.length - 1; x++) {
                shaderMaterials[x].setFloat("alphaCutoff", value)
            }
        });

        var onControllerAttached = function (webVRController) {

            // var moveMesh = BABYLON.MeshBuilder.CreatePlane("box", {width: .1}, scene);
            //             // parentAll(moveMesh)
            //             // plane.setPositionWithLocalVector(webVRCamera.devicePosition.add(new BABYLON.Vector3(-1, 0, -1)));
            //             // moveMesh.setPositionWithLocalVector(webVRCamera.devicePosition.add(new BABYLON.Vector3(-.5, 0, -1)));
            //             // unparentAll(moveMesh);
            //             // moveMesh.dispose();
            console.log(webVRController.hand + " controller ready.");
            if (webVRController.hand == "right") {
                webVRCamera.rightController.onTriggerStateChangedObservable.add(function (stateObject) {
                    rightControllerEnabled = stateObject["pressed"] // {x: 0.1, y: -0.3}

                });

            }
            if (webVRController.hand == "left") {
                console.log("Test")


                webVRCamera.leftController.onRightButtonStateChangedObservable.add(function (stateObject) {
                    scaleDown = stateObject["pressed"]
                    parentAll(scaleMesh)


                    // var scaleMesh = BABYLON.MeshBuilder.CreateAbstractMesh()


                });
                webVRCamera.leftController.onLeftButtonStateChangedObservable.add(function (stateObject) {
                    scaleUp = stateObject["pressed"]
                    parentAll(scaleMesh)
                });


                console.log("test2")
                webVRCamera.leftController.onTriggerStateChangedObservable.add(function (stateObject) {
                    if (stateObject["pressed"] && !leftMovement && !rightMovement) {
                        parentAll(webVRCamera.leftController.mesh)
                        console.log("test")
                        leftMovement = true;
                    }
                    if (!stateObject["pressed"]) {
                        unparentAll(webVRCamera.leftController.mesh)
                        leftMovement = false
                    }// {x: 0.1, y: -0.3}

                });
                webVRCamera.leftController.onSecondaryButtonStateChangedObservable.add(function (stateObject) {
                    console.log(stateObject)
                    if (stateObject["pressed"]&&leftMovement ) {
                        console.log("Menu pressed")
                        parentForAll.setPositionWithLocalVector(webVRCamera.leftController.position)
                            mesh2.setPositionWithLocalVector(webVRCamera.leftController.position)

                    }

                });
            }
        }
        vrHelper.onControllerMeshLoaded.add(onControllerAttached);
        vrHelper.onEnteringVRObservable.add(() => {

            console.log("ran")
        })
        return scene;
    };


    // call the createScene function
    var scene = createScene();

    // run the render loop
    engine.runRenderLoop(function () {
        scene.render();
    });

    // the canvas/window resize event handler
    window.addEventListener('resize', function () {
        engine.resize();
    });

});