function move() {
    const gameState = {
        left: [3, 3],  // missionaries, cannibals on left
        right: [0, 0], // right side
        boat: "left"   // or "right"
    };

    fetch('/validate', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(gameState)
    })
    .then(res => res.json())
    .then(data => {
        if (data.valid) {
            alert("Valid Move");
        } else {
            alert("Invalid Move: " + data.message);
        }
    });
}
let boat=[];
let boatSide='left';
function selectCharater(element,side){
    if(boat.length<2){
        boat.push(element.innerText);
        element.style.opacity=0.5;
        console.log("selected",boat);
    document.getElementById("boat-passengers").innertext=boat.map(e=>e.innerText).join(",");
    }
    else{
        alert("Boat can carry only 2 prople!");
    }
}