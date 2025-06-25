# Ping Pong Game using PyOpenGL
Our game is a simple ball with bat game known as the Ping-Pong game

## About Game
1. The bat will be moved according to the movement of the mouse.
2. The ball will move randomly in the created window.
3. When the ball hits the right, left, or top wall (we will refer to the window border as a wall), it will return.
4. When it hits the bottom wall, it will not only return but it will also increase the score of the computer
5. But if the player can hold it with the bat, his score will be increased.
   
   ![Game Interface](https://github.com/faiyaz-masrur/ping-pong-game-with-opengl/blob/930049890698bbd91ee672d86717fed6417eaa88/game%20interface%20screenshot.png)

## How to start
1. Install Python from any Python environment management system (I recommend conda). 
2. Install a Python IDE (I recommend PyCharm).
3. Start a new project (for the first time)
   
   ![Pycharm settings](https://github.com/faiyaz-masrur/ping-pong-game-with-opengl/blob/89a2c9965bc0715fbfdcea0ac27b60f746e30447/Pycharm_settings.png)  
   Choose the Python environment manager that is on your system.  
   Tick the **“Make available to all projects”** option. That way, you can start from the same virtual environment in the new projects from now on.  
   Remember the name of the project for later use.  
   Press the create button.  
5. Now, in this virtual environment, we will install OpenGL.  
   Go to the terminal and type the following command.
   ```
   pip install PyOpenGL PyOpenGL_accelerate
   ```
6. Start a new project (Using previously set up virtual environment)
7. Download and copy this [FreeGLUT.dll file](https://github.com/faiyaz-masrur/ping-pong-game-with-opengl/blob/89a2c9965bc0715fbfdcea0ac27b60f746e30447/freeglut64.vc14.dll) to your project alongside **main.py**.
8. After that, copy and paste the game code from [ping_pong_game.py](https://github.com/faiyaz-masrur/ping-pong-game-with-opengl/blob/8001993a54ad95ad36271d471b9a58c1e92d8f10/ping_pong_game.py) and run the **main.py**.

