# Software-based black frame insertion / software strobing to reduce motion blur
Strobes an overlay rectangle over screen to reduce display motion blur at expense of reduced framerate displayed and flickering on any display type (LCD or CRT).

Causes more flickering than the natural strobing on a CRT (because the entire screen/area is revealed at once instead of just a line), more uneasy on the eyes than crt, but it does reduce blur at the expense of framerate shown and slight discomfort...

Demo of black frame insertion at Blur Busters (works on any hz monitor including 60hz standard) https://www.testufo.com/blackframes

![Image of strobing](https://github.com/ArtDor2/strobing/blob/master/strobing%20demo.png)

TO-DO:
- [ ] try alpha for black fill for reduced flicker
- [ ] fix stuttering
- - [ ] improve performance screen.fill (try use black image instead?)
- [ ] be able to exit with Esc
- [ ] be able to drag strobing window, resize?
- [ ] strobing window auto resize to fit application, or fullscreen
- [ ] add options for startup: how many frames to strobe
- [ ] compile stand alone executable
