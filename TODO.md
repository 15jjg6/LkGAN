TODO:
=====
- Better memory management so that the process isn't killed due to lack of memory
- Update module names - either fix getters and setters to return instead of modifying or clarify them
- create config file for creating experiment
- Split running experiment and LKGAN code into two separate files
- Clean up comment code
	- Commented out code make into an option
 	- Make comments explaining everything for your own notes?
- Update code to use tf.v2


Math Related Ideas:
===================
- How to best choose k and alpha using the gradient descent
- take derivative of loss fun'n with respect to alpha and k

for k<2 it seems to be working better, so changing the k value excites the system for different input values. It's changing how much the ln function has an effect on the output of the generator.

Instead of moving k from 1-3 calculate gradients with respect to k and update it based on gradient at that point. Move in direction of minimizing loss function. Or change loss function randomly in the neighbourhood. 

changing k changes magnitude of gradient updates. 