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


document.getElementById("btnAdd").addEventListener("click",function(){ document.querySelector(".popupContenAdd").style.display= "flex";
})
document.getElementById("close-btn-Add").addEventListener("click",function(){ document.querySelector(".popupContenAdd").style.display= "none";
})

function onClick(change) {
  const totalElement = document.getElementById('totalClick');
  let current = parseInt(totalElement.innerText);
  
  let newTotal = current + change;
  if (newTotal < 0) newTotal = 0;

  totalElement.innerText = newTotal;
}
