function addFigurePins(elementId, ...pins) {
    figureElement = document.querySelector(elementId);
    figureElement.classList.add('imgpin-parent');
    for (let i = 0; i < pins.length; i++) {
        pinDef = pins[i];
        pin = document.createElement('div');
        pin.classList.add('imgpin');
        pin.style.left = `${pinDef.x}%`;
        pin.style.top = `${pinDef.y}%`;
        pin.title = pinDef.title;
        pin.innerText = `${i + 1}`;
        figureElement.appendChild(pin);
    }
}
