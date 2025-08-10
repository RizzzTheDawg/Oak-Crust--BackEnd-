document.getElementById("btnCtg").addEventListener("click",function(){ document.querySelector(".popupContentCatg").style.display= "flex";
})
document.getElementById("close-btn").addEventListener("click",function(){ document.querySelector(".popupContentCatg").style.display= "none";
})


document.getElementById("btnOrd").addEventListener("click",function(){ document.querySelector(".popupContentOrd").style.display= "flex";
})
document.getElementById("close-btn-Ord").addEventListener("click",function(){ document.querySelector(".popupContentOrd").style.display= "none";
})


document.getElementById("btnPrd").addEventListener("click",function(){ document.querySelector(".popupContentPrd").style.display= "flex";
})
document.getElementById("close-btn-Prd").addEventListener("click",function(){ document.querySelector(".popupContentPrd").style.display= "none";
})


document.getElementById("btnHst").addEventListener("click",function(){ document.querySelector(".popupContentHst").style.display= "flex";
})


document.getElementById("btnCrt").addEventListener("click",function(){ document.querySelector(".popupContentCrt").style.display= "flex";
})
document.getElementById("close-btn-crt2").addEventListener("click",function(){ document.querySelector(".popupContentCrt").style.display= "none";
})


document.getElementById("btnAdd").addEventListener("click",function(){ document.querySelector(".popupContentAdd").style.display= "flex";
})
document.getElementById("close-btn-Add").addEventListener("click",function(){ document.querySelector(".popupContentAdd").style.display= "none";
})

function onClick(change) {
  const totalElement = document.getElementById('totalClick');
  let current = parseInt(totalElement.innerText);
  
  let newTotal = current + change;
  if (newTotal < 0) newTotal = 0;

  totalElement.innerText = newTotal;
}

document.querySelector('.btn-submit').addEventListener('click', function() {
    const category = document.getElementById('category').value;
    const itemName = document.getElementById('itemName').value;
    const price = document.getElementById('price').value;

    if (!category || !itemName || !price) {
        alert("Please fill out all fields.");
        return;
    }

    console.log(`Category: ${category}, Name: ${itemName}, Price: ${price}`);
    // Here you can send data to backend
});
